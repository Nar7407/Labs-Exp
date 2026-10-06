import os
import numpy as np
import pandas as pd
from scipy import stats

pd.set_option("display.width", 100)

ALPHA = 0.05
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

DATASETS = {
    "titanic": (
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv",
        "titanic",
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


def chi_square_independence(df, row, col, row_name, col_name):
    banner(f"Chi-Square Test of Independence : {row_name} vs {col_name}")

    table = pd.crosstab(df[row], df[col])
    print(f"\nContingency table (observed counts):")
    print(table)

    chi2, p, dof, expected = stats.chi2_contingency(table)
    print(f"\nExpected counts (under independence):")
    print(pd.DataFrame(
        expected, index=table.index, columns=table.columns).round(2))

    expected = expected[expected > 0]
    ok_share = (expected >= 5).mean()
    print(f"\nCells with expected count >= 5 : {ok_share:.1%} "
        f"({'assumption satisfied' if ok_share >= 0.8 else 'assumption VIOLATED - interpret with care'})")

    h0 = f"{row_name} and {col_name} are independent (survival does not depend on {row_name.lower()})"
    h1 = f"{row_name} and {col_name} are associated (survival depends on {row_name.lower()})"
    report(f"chi2_contingency({row_name}, {col_name})", chi2, p, h0, h1,
        extra=f"Degrees of freedom : {dof}")

    if p < ALPHA:
        print(f"Association strength (Cramér's V) : "
              f"{((chi2 / table.to_numpy().sum()) / min(table.shape[0] - 1, table.shape[1] - 1)) ** 0.5:.4f}")
    return table, chi2, p, dof


def correlations(df):
    banner("Correlation : age vs fare (missing values dropped)")
    sub = df[["age", "fare"]].dropna()
    print(f"\nRows used after dropna() : {len(sub)} of {len(df)} "
        f"({len(df) - len(sub)} rows had a missing age)")
    print(sub.describe().round(3))

    r_pearson, p_pearson = stats.pearsonr(sub["age"], sub["fare"])
    rho_spearman, p_spearman = stats.spearmanr(sub["age"], sub["fare"])
    r_kendall, p_kendall = stats.kendalltau(sub["age"], sub["fare"])

    print(f"\n{'':<12}{'coefficient':>12}{'p-value':>12}")
    print(f"{'Pearson r':<12}{r_pearson:>12.4f}{p_pearson:>12.3e}")
    print(f"{'Spearman rho':<12}{rho_spearman:>12.4f}{p_spearman:>12.3e}")
    print(f"{'Kendall tau':<12}{r_kendall:>12.4f}{p_kendall:>12.3e}")

    h0 = "age and fare are linearly unrelated in the passenger population (rho = 0)"
    h1 = "age and fare are related (rho != 0)"
    for name, coef, p in (("Pearson", r_pearson, p_pearson),
                        ("Spearman", rho_spearman, p_spearman)):
        report(f"{name} correlation test (age vs fare)", coef, p, h0, h1)

    banner("Do Pearson and Spearman agree?")
    print(f"Pearson  r  = {r_pearson:+.4f}   (linear, sensitive to outliers)")
    print(f"Spearman rho= {rho_spearman:+.4f}   (monotonic, rank-based, robust)")
    print(f"Absolute difference |r - rho| = {abs(r_pearson - rho_spearman):.4f}")


if __name__ == "__main__":
    df = load_dataset("titanic")
    print(f"\nDataset shape : {df.shape}")
    print(f"Columns       : {list(df.columns)}")

    chi_square_independence(df, "sex", "survived", "sex", "survived")
    chi_square_independence(df, "pclass", "survived", "pclass", "survived")
    correlations(df)
