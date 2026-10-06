import os
import itertools

import numpy as np
import pandas as pd
from scipy import stats

ALPHA = 0.05
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

DATASETS = {
    "penguins": (
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv",
        "penguins",
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


def shapiro_by_species(df):
    banner("3.1  Shapiro-Wilk Normality Test : flipper_length_mm by species")
    print("H0 : flipper length within each species is normally distributed")
    print("H1 : it is not normally distributed\n")

    normal = {}
    for species, g in df.groupby("species"):
        x = g["flipper_length_mm"].dropna().to_numpy()
        w, p = stats.shapiro(x)
        normal[species] = p >= ALPHA
        descriptives(f"{species:<22}", x)
        report(f"shapiro(flipper_length_mm | {species})", w, p,
               f"{species} flipper length is normally distributed",
               f"{species} flipper length is NOT normally distributed",
               extra=f"Verdict: {'NORMAL - parametric tests valid' if p >= ALPHA else 'NOT NORMAL - prefer non-parametric tests'}")
    print("\nNormal distribution per species :")
    for s, ok in normal.items():
        print(f"  {s:<15} -> {'yes' if ok else 'no'}")
    return normal


def mannwhitney_by_pair(df):
    banner("3.2  Mann-Whitney U Test : flipper_length_mm, every pair of species")
    species = sorted(df["species"].unique())
    print("H0 : flipper length distributions are identical across the two species")
    print("H1 : they differ (in median / location)\n")

    for a, b in itertools.combinations(species, 2):
        xa = df.loc[df["species"] == a, "flipper_length_mm"].dropna().to_numpy()
        xb = df.loc[df["species"] == b, "flipper_length_mm"].dropna().to_numpy()
        descriptives(f"{a}", xa)
        descriptives(f"{b}", xb)
        u, p = stats.mannwhitneyu(xa, xb, alternative="two-sided")
        report(f"mannwhitneyu(flipper | {a}, flipper | {b})", u, p,
               f"flipper length distribution is the same for {a} and {b}",
               f"flipper length distribution differs between {a} and {b}",
               extra=f"medians: {a} = {np.median(xa):.1f} mm, "
                     f"{b} = {np.median(xb):.1f} mm")
        n1, n2 = len(xa), len(xb)
        rb = 2 * u / (n1 * n2) - 1
        print(f"Rank-biserial effect size = {rb:+.3f} "
              f"({'larger in ' + b if rb < 0 else 'larger in ' + a})")
        print()


def kruskal_bill_length(df):
    banner("3.3  Kruskal-Wallis Test : bill_length_mm across all three species")
    species = sorted(df["species"].unique())
    groups = [df.loc[df["species"] == s, "bill_length_mm"].dropna().to_numpy()
              for s in species]
    for s, g in zip(species, groups):
        descriptives(f"{s:<22}", g)

    h0 = "bill_length_mm distributions are the same across all three species"
    h1 = "at least one species differs from the others"
    h, p = stats.kruskal(*groups)
    report("kruskal(bill_length_mm by species)", h, p, h0, h1,
           extra=f"Groups compared : {species}")

    if p < ALPHA:
        print("\nKruskal-Wallis is significant, so follow it with pairwise Mann-Whitney")
        print("tests (with Bonferroni-corrected alpha) to locate the difference:")
        m = len(list(itertools.combinations(species, 2)))
        alpha_bonf = ALPHA / m
        print(f"Bonferroni-corrected alpha = {ALPHA} / {m} = {alpha_bonf:.4f}\n")
        for a, b in itertools.combinations(species, 2):
            xa = df.loc[df["species"] == a, "bill_length_mm"].dropna().to_numpy()
            xb = df.loc[df["species"] == b, "bill_length_mm"].dropna().to_numpy()
            u, p_pair = stats.mannwhitneyu(xa, xb, alternative="two-sided")
            print(f"  {a:<12} vs {b:<12} medians {np.median(xa):5.1f} / "
                  f"{np.median(xb):5.1f}  p = {p_pair:.3e}  "
                  f"-> {'significant' if p_pair < alpha_bonf else 'not significant'}")

    f, p_anova = stats.f_oneway(*groups)
    print(f"\nFor reference, one-way ANOVA on the same data : F = {f:.4f}, "
          f"p = {p_anova:.6g} -> {decision(p_anova)}")
    print(f"Kruskal-Wallis conclusion matches ANOVA : {decision(p) == decision(p_anova)}")
    return h, p


def ks_two_sample_islands(df):
    banner("3.4  Two-Sample Kolmogorov-Smirnov Test : body_mass_g by island")
    islands = sorted(df["island"].unique())
    print(f"Islands available : {islands}\n")
    pairs = [tuple(pair) for pair in itertools.combinations(islands, 2)]
    for i1, i2 in pairs:
        x1 = df.loc[df["island"] == i1, "body_mass_g"].dropna().to_numpy()
        x2 = df.loc[df["island"] == i2, "body_mass_g"].dropna().to_numpy()
        if len(x1) < 5 or len(x2) < 5:
            print(f"Skipping {i1} vs {i2}: too few observations for a reliable KS test.")
            continue
        descriptives(f"{i1}", x1)
        descriptives(f"{i2}", x2)
        d, p = stats.ks_2samp(x1, x2)
        report(f"ks_2samp(body_mass_g | {i1}, body_mass_g | {i2})", d, p,
               f"body mass distributions on {i1} and {i2} are identical",
               f"body mass distributions on {i1} and {i2} differ",
               extra=f"medians: {i1} = {np.median(x1):.0f} g, "
                     f"{i2} = {np.median(x2):.0f} g")


def main():
    banner("EXPERIMENT 11 - TASK 3 : Penguins - Non-Parametric Hypothesis Tests")
    df = load_dataset("penguins")
    print(f"\nDataset shape : {df.shape}")
    print(f"Columns       : {list(df.columns)}")
    print("\nRows with any missing value : "
          f"{df[['flipper_length_mm', 'bill_length_mm', 'body_mass_g']].isna().any(axis=1).sum()}")
    df = df.dropna(subset=["flipper_length_mm", "bill_length_mm", "body_mass_g"])
    print(f"After dropna on the three measurements : {df.shape}")

    shapiro_by_species(df)
    mannwhitney_by_pair(df)
    kruskal_bill_length(df)
    ks_two_sample_islands(df)

    banner("TASK 3 SUMMARY (alpha = 0.05)")
    print("1. Shapiro-Wilk per species checks normality before choosing the test.")
    print("2. Mann-Whitney U compares flipper length pairwise between species.")
    print("3. Kruskal-Wallis replaces one-way ANOVA for bill length across species.")
    print("4. Two-sample KS compares body-mass distribution across islands.")


if __name__ == "__main__":
    main()
