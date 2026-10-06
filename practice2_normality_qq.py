import os

import numpy as np
from scipy import stats

ALPHA = 0.05


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


def main():
    banner("PRACTICE 2 : Normality of Exam Scores - Shapiro-Wilk + Q-Q plot")

    rng = np.random.default_rng(7)
    normal_group = rng.normal(72, 9, 60)
    skewed_group = np.clip(rng.beta(1.5, 4, 40) * 60 + 45, 0, 100)
    scores = np.concatenate([normal_group, skewed_group])

    print(f"Sample size : n = {scores.size}")
    print(f"min = {scores.min():.2f}, max = {scores.max():.2f}")
    print(f"mean = {scores.mean():.3f}, sd = {scores.std(ddof=1):.3f}")
    print(f"median = {np.median(scores):.3f}")

    print("\n--- Descriptive statistics ---")
    print("-" * 72)
    d = stats.describe(scores)
    print(f"nobs   : {d.nobs}")
    print(f"mean   : {d.mean:.4f}")
    print(f"variance (ddof=1) : {d.variance:.4f}   sd = {np.sqrt(d.variance):.4f}")
    print(f"min/max: {d.minmax[0]:.2f} / {d.minmax[1]:.2f}   "
          f"(field name is minmax, not min)")
    print(f"skewness   : {d.skewness:.4f}  ({'right' if d.skewness > 0 else 'left'} skewed)")
    print(f"kurtosis   : {d.kurtosis:.4f}  (excess kurtosis; >0 = heavy tails)")

    print("\n--- Test 1 : Shapiro-Wilk ---")
    print("-" * 72)
    w, p = stats.shapiro(scores)
    report("shapiro(scores)", w, p,
           "The exam scores come from a normally distributed population",
           "The exam scores do NOT come from a normally distributed population")

    print("\nSupporting normality checks (all test the same idea):")
    d_ks, p_ks = stats.kstest(scores, "norm",
                             args=(scores.mean(), scores.std(ddof=1)))
    print(f"  KS vs fitted normal : D = {d_ks:.4f}, p = {p_ks:.4f} -> "
          f"{'no significant departure' if p_ks >= ALPHA else 'departure detected'}")
    jarque_bera = stats.jarque_bera(scores)
    print(f"  Jarque-Bera         : JB = {jarque_bera.statistic:.4f}, "
          f"p = {jarque_bera.pvalue:.4f} -> "
          f"{'normal' if jarque_bera.pvalue >= ALPHA else 'not normal'}")
    top = (scores == scores.max()).sum()
    print(f"  Tied observations at the maximum : {top} of {scores.size} "
          f"({'ceil effect present' if top > 1 else 'no ceiling'})")

    print("\n--- Test 2 : Q-Q and P-P plots (stats.probplot) ---")
    print("-" * 72)
    (osm, osr), (slope, intercept, r) = stats.probplot(scores, dist="norm")
    osm = np.asarray(osm, dtype=float)
    osr = np.asarray(osr, dtype=float)
    print(f"Expected order statistics (osm) : first 3 = {np.array2string(osm[:3], precision=4)}, "
          f"last 3 = {np.array2string(osm[-3:], precision=4)}")
    print(f"Observed order statistics (osr) : first 3 = {np.array2string(osr[:3], precision=4)}, "
          f"last 3 = {np.array2string(osr[-3:], precision=4)}")
    print(f"Fitted straight line : score = {intercept:.4f} + {slope:.4f} * expected_quantile")
    print(f"Linearity / R^2      : r = {r:.4f}, R^2 = {r ** 2:.4f}")

    verdict = "NORMAL" if p >= ALPHA else "NOT NORMAL"
    print(f"\nShapiro-Wilk verdict : {verdict}")
    if r ** 2 >= 0.98:
        print(f"Q-Q plot verdict     : points lie close to the line (R^2 = {r ** 2:.4f}) -> consistent with normality")
    else:
        print(f"Q-Q plot verdict     : points depart from the line (R^2 = {r ** 2:.4f}) -> NOT consistent with normality")
    print("\nThe two methods should agree. Shapiro-Wilk gives the formal p-value; the Q-Q plot shows where the assumption breaks.")

    print("\n--- Contrast : same test on the two sub-groups ---")
    print("-" * 72)
    for name, group in (("normal-ish group", normal_group),
                         ("skewed group", skewed_group)):
        wg, pg = stats.shapiro(group)
        _, (sl, ic, rr) = stats.probplot(group, dist="norm")
        print(f"{name:<18} n={group.size:<4} skew={stats.skew(group):+.3f}  "
              f"Shapiro W={wg:.4f} p={pg:.6g} -> "
              f"{'NORMAL' if pg >= ALPHA else 'NOT NORMAL'};  Q-Q R^2={rr ** 2:.4f}")
    print("\nSkewness is the driver: a strong skew pushes Shapiro-Wilk to reject and drags the Q-Q tails off the line, which is when a non-parametric test is the right substitute.")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

        axes[0].hist(scores, bins=15, color="#4C72B0", edgecolor="white")
        axes[0].axvline(scores.mean(), color="red", linestyle="--",
                        label=f"mean = {scores.mean():.2f}")
        axes[0].axvline(np.median(scores), color="green", linestyle=":",
                        label=f"median = {np.median(scores):.2f}")
        axes[0].set_title("Histogram with normal overlay")
        axes[0].set_xlabel("Exam score")
        axes[0].set_ylabel("Frequency")
        axes[0].legend()

        stats.probplot(scores, dist="norm", plot=axes[1])
        axes[1].set_title(f"Normal Q-Q plot (R^2 = {r ** 2:.4f})")

        stats.probplot(scores, dist="norm", plot=axes[2])
        axes[2].set_title("Normal P-P plot")

        plt.tight_layout()
        plt.savefig("practice2_normality_qq.png", dpi=120)
        print("\nFigure written to practice2_normality_qq.png")
        print("(Agg backend used, so nothing pops up; open the PNG to inspect it.)")
    except ImportError:
        print("\n[info] matplotlib not available - plots skipped.")


if __name__ == "__main__":
    main()
