import os
import pandas as pd

import numpy as np
from scipy import stats

ALPHA = 0.05
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

DATASETS = {
    "tips": (
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
        "tips",
    ),
}


def load_dataset(name):
    url, seaborn_name = DATASETS[name]
    os.makedirs(CACHE_DIR, exist_ok=True)
    cached = os.path.join(CACHE_DIR, f"{name}.csv")
    if os.path.exists(cached):
        return pd.read_csv(cached)
    try:
        df = pd.read_csv(url)
    except Exception as exc:
        print(f"[info] could not download {name} ({exc}); using seaborn copy")
        import seaborn as sns
        return sns.load_dataset(seaborn_name)
    df.to_csv(cached, index=False)
    print(f"[info] downloaded {name} -> {cached}")
    return df


def banner(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def decision(p, alpha=ALPHA):
    return "Reject H0" if p < alpha else "Fail to reject H0"


def report(test_name, stat, p, h0, h1, alpha=ALPHA, extra=""):
    print(f"\n--- {test_name} " + "-" * max(0, 60 - len(test_name)))
    print(f"H0 (null)        : {h0}")
    print(f"H1 (alternative) : {h1}")
    if stat is not None:
        print(f"Test statistic   : {stat:.6f}")
    print(f"p-value          : {p:.6g}")
    print(f"Significance (a): {alpha}")
    print(f"Decision         : {decision(p, alpha)} "
          f"(p {'<' if p < alpha else '>='} {alpha})")
    if extra:
        print(extra)
    print("Interpretation   : " + (
        f"evidence AGAINST H0 at alpha={alpha}"
        if p < alpha else
        f"insufficient evidence against H0 at alpha={alpha}"
    ))


def descriptives(label, sample):
    x = np.asarray(sample, dtype=float)
    n = x.size
    mean = x.mean()
    sd = x.std(ddof=1)
    sem = stats.sem(x)
    ci = stats.t.interval(0.95, n - 1, loc=mean, scale=sem) if n > 1 else (np.nan, np.nan)
    print(f"{label:<26} n={n:<4} mean={mean:8.3f}  sd={sd:7.3f}  "
          f"95% CI = [{ci[0]:.3f}, {ci[1]:.3f}]")
    return mean, sd


def one_sample_ttest(df):
    banner("2.1  One-Sample t-Test : mean total bill vs $20")
    bills = df["total_bill"].to_numpy()
    descriptives("total_bill", bills)

    h0 = "The population mean total bill equals $20"
    h1 = "The population mean total bill differs from $20"

    t, p = stats.ttest_1samp(bills, popmean=20)
    report("ttest_1samp(total_bill, popmean=20)", t, p, h0, h1,
           extra=f"Sample mean = {bills.mean():.3f}")

    t_less, p_less = stats.ttest_1samp(bills, popmean=20, alternative="less")
    print(f"\nOne-sided H1 'mean < $20' : t = {t_less:.4f}, p = {p_less:.6g} -> "
          f"{decision(p_less)}")

    ci = stats.t.interval(1 - ALPHA, len(bills) - 1, loc=bills.mean(),
                          scale=stats.sem(bills))
    print(f"95% CI of the mean : [{ci[0]:.3f}, {ci[1]:.3f}]  "
          f"({'excludes' if not (ci[0] <= 20 <= ci[1]) else 'contains'} 20)")

    print("\nNote : normality here is backed by n = %d (CLT), so the t-test is valid."
          % len(bills))
    print("      As a cross-check, a KS test against the fitted normal:")
    ks_stat, ks_p = stats.kstest(bills, "norm", args=(bills.mean(), bills.std(ddof=1)))
    print(f"      D = {ks_stat:.4f}, p = {ks_p:.6g} -> "
          f"{'no significant departure from normality' if ks_p >= ALPHA else 'some departure detected'}")
    return t, p


def levene_and_independent_ttest(df):
    banner("2.2  Homogeneity of Variance (Levene) then Independent-Sample t-Test : smoker vs tip")
    smoker = df.loc[df["smoker"] == "Yes", "tip"].to_numpy()
    non = df.loc[df["smoker"] == "No", "tip"].to_numpy()
    descriptives("tip | smoker=Yes", smoker)
    descriptives("tip | smoker=No", non)

    lev, p_lev = stats.levene(smoker, non)
    report("levene(tip smoker, tip non-smoker)", lev, p_lev,
           "Tips have equal variance for smokers and non-smokers",
           "Tips have different variance for smokers and non-smokers")

    sh_s = stats.shapiro(smoker)
    sh_n = stats.shapiro(non)
    print(f"\nNormality within groups (Shapiro-Wilk):")
    print(f"  smoker=Yes  : W = {sh_s.statistic:.4f}, p = {sh_s.pvalue:.6g}")
    print(f"  smoker=No   : W = {sh_n.statistic:.4f}, p = {sh_n.pvalue:.6g}")

    h0 = "The mean tip is the same for smokers and non-smokers"
    h1 = "The mean tip differs between smokers and non-smokers"

    t_std, p_std = stats.ttest_ind(smoker, non, equal_var=True)
    report("ttest_ind equal_var=True (Student)", t_std, p_std, h0, h1)

    if p_lev < ALPHA:
        print("\nLevene rejected homogeneity, so the pooled-variance t-test is NOT")
        print("safe. Using Welch's unequal-variance t-test instead:")
        t_w, p_w = stats.ttest_ind(smoker, non, equal_var=False)
        report("ttest_ind equal_var=False (Welch)", t_w, p_w, h0, h1)

    u, p_u = stats.mannwhitneyu(smoker, non, alternative="two-sided")
    report("mannwhitneyu(tip smoker, tip non-smoker) - cross-check", u, p_u, h0, h1,
           extra="Non-parametric alternative; included to confirm the t-test conclusion.")
    return t_std, p_std, p_lev


def one_way_anova(df):
    banner("2.3  One-Way ANOVA : total bill across the four days")
    days = sorted(df["day"].unique())
    groups = [df.loc[df["day"] == d, "total_bill"].to_numpy() for d in days]
    for d, g in zip(days, groups):
        descriptives(f"total_bill | {d}", g)

    h0 = "Mean total bill is equal across all four days"
    h1 = "At least one day has a mean total bill different from the others"

    f, p = stats.f_oneway(*groups)
    report("f_oneway(total_bill by day)", f, p, h0, h1,
           extra=f"Groups compared : {days}")

    print("\nAssumption checks for ANOVA:")
    for d, g in zip(days, groups):
        sh = stats.shapiro(g)
        print(f"  Shapiro-Wilk {d:<4} : W = {sh.statistic:.4f}, p = {sh.pvalue:.4f} "
              f"-> {'normal' if sh.pvalue >= ALPHA else 'not normal'}")
    lev, p_lev = stats.levene(*groups)
    print(f"  Levene (4 groups)      : stat = {lev:.4f}, p = {p_lev:.4f} -> "
          f"{'equal variances' if p_lev >= ALPHA else 'unequal variances'}")

    if p < ALPHA:
        print("\nANOVA is significant, so a post-hoc test is needed to see WHICH day differs.")
        h_stat, p_kw = stats.kruskal(*groups)
        report("kruskal(total_bill by day) - non-parametric alternative", h_stat, p_kw, h0, h1)
        eta_sq = (stats.f_oneway(*groups)[0] /
                  (stats.f_oneway(*groups)[0] + sum(len(g) for g in groups) - len(groups)))
        print(f"\nEffect size (eta squared) = {eta_sq:.4f} "
              f"({'small' if eta_sq < 0.06 else 'moderate' if eta_sq < 0.14 else 'large'})")
    else:
        print("\nANOVA not significant - the four day means can be treated as indistinguishable.")
    return f, p


def paired_ttest():
    banner("2.4  Paired (Dependent) t-Test : synthetic before/after blood pressure")
    rng = np.random.default_rng(42)
    n = 10
    before = np.array([148, 152, 149, 155, 151, 158, 146, 157, 150, 153], dtype=float)
    after = before - 8 + rng.normal(0, 2.0, n)
    print("patient : " + "".join(f"{i + 1:>6}" for i in range(n)))
    print("before  : " + "".join(f"{v:>6.1f}" for v in before))
    print("after   : " + "".join(f"{v:>6.1f}" for v in after))
    print("diff    : " + "".join(f"{v:>6.1f}" for v in after - before))

    descriptives("before", before)
    descriptives("after", after)
    diff = before - after
    descriptives("before - after", diff)

    sh = stats.shapiro(diff)
    print(f"\nNormality of the paired DIFFERENCES (the real assumption of a paired")
    print(f"t-test) : W = {sh.statistic:.4f}, p = {sh.pvalue:.4f} -> "
          f"{'normal' if sh.pvalue >= ALPHA else 'not normal - use Wilcoxon'}")

    h0 = "The treatment has no effect: mean before-after difference = 0"
    h1 = "The treatment changes blood pressure: mean difference != 0"
    t, p = stats.ttest_rel(before, after)
    report("ttest_rel(before, after)", t, p, h0, h1,
           extra=f"Mean reduction = {diff.mean():.2f} mmHg, "
                 f"sd of differences = {diff.std(ddof=1):.2f}")

    ci = stats.t.interval(1 - ALPHA, n - 1, loc=diff.mean(), scale=stats.sem(diff))
    print(f"95% CI of the mean reduction : [{ci[0]:.2f}, {ci[1]:.2f}] mmHg")

    w, p_w = stats.wilcoxon(before, after)
    report("wilcoxon(before, after) - paired non-parametric check", w, p_w, h0, h1)
    cohens_d = diff.mean() / diff.std(ddof=1)
    print(f"\nPaired effect size (Cohen's d_z) = {cohens_d:.3f}")
    return t, p


def main():
    banner("EXPERIMENT 11 - TASK 2 : Tips - Parametric Hypothesis Tests")
    df = load_dataset("tips")
    print(f"\nDataset shape : {df.shape}")
    print(f"Columns       : {list(df.columns)}")
    print(f"smoker values : {df['smoker'].unique().tolist()}")
    print(f"day values    : {sorted(df['day'].unique())}")

    one_sample_ttest(df)
    levene_and_independent_ttest(df)
    one_way_anova(df)
    paired_ttest()

    banner("TASK 2 SUMMARY (alpha = 0.05)")
    print("1. One-sample t-test  : mean total bill vs $20 - decide from the printed p.")
    print("2. Levene first       : it chooses Student vs Welch for the t-test.")
    print("3. One-way ANOVA      : tests any difference across the four days.")


if __name__ == "__main__":
    main()
