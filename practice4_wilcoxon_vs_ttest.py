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


def paired_comparison(before, after, title):
    banner(title)

    n = len(before)
    before = np.asarray(before, dtype=float)
    after = np.asarray(after, dtype=float)
    diff = before - after

    print(f"{'pair':>6}{'before':>10}{'after':>10}{'diff':>10}{'|diff|':>9}{'rank':>7}{'rank*sign':>11}")
    w = stats.wilcoxon(before, after).statistic
    ranks = stats.rankdata(np.abs(diff))
    signs = np.sign(diff)
    for i in range(n):
        print(f"{i + 1:>6}{before[i]:>10.2f}{after[i]:>10.2f}{diff[i]:>10.2f}"
              f"{abs(diff[i]):>9.2f}{ranks[i]:>7.1f}{ranks[i] * signs[i]:>11.1f}")

    print(f"\nn = {n}")
    print(f"mean difference   = {diff.mean():.4f}  (sd = {diff.std(ddof=1):.4f}, "
          f"se = {stats.sem(diff):.4f})")
    print(f"median difference = {np.median(diff):.4f}")

    h0 = "The treatment has no effect (median/mean paired difference = 0)"
    h1 = "The treatment changes the measured quantity (difference != 0)"

    print("\n--- Assumption of the paired t-test: normality of the DIFFERENCES ---")
    print("-" * 72)
    w_sh, p_sh = stats.shapiro(diff)
    print(f"Shapiro-Wilk on differences : W = {w_sh:.4f}, p = {p_sh:.4f} -> "
          f"{'symmetric/normal enough' if p_sh >= ALPHA else 'NOT normal'}")
    print("Skewness of differences     : "
          f"{stats.skew(diff):.4f}   (Wilcoxon only needs approximate symmetry)")
    print("\nAssumption of the Wilcoxon test: the differences are at least ordinal and")
    print("symmetric about their median - it discards magnitude information by ranking.")

    print("\n--- Paired t-Test (parametric) ---")
    print("-" * 72)
    t, p_t = stats.ttest_rel(before, after)
    ci = stats.t.interval(1 - ALPHA, n - 1, loc=diff.mean(), scale=stats.sem(diff))
    report("ttest_rel(before, after)", t, p_t, h0, h1,
           extra=f"95% CI of the mean difference : [{ci[0]:.4f}, {ci[1]:.4f}]")

    print("\n--- Wilcoxon Signed-Rank (non-parametric) ---")
    print("-" * 72)
    p_w = stats.wilcoxon(before, after).pvalue
    report("wilcoxon(before, after)", w, p_w, h0, h1,
           extra="scipy returns the smaller of W+ and W-, so the statistic is "
                 "non-negative; the p-value is what matters.")

    print("\n--- Comparison of the two conclusions ---")
    print("-" * 72)
    agree = (p_t < ALPHA) == (p_w < ALPHA)
    print(f"paired t-test p     = {p_t:.6g} -> {'significant' if p_t < ALPHA else 'not significant'}")
    print(f"Wilcoxon     p      = {p_w:.6g} -> {'significant' if p_w < ALPHA else 'not significant'}")
    print(f"Conclusions agree   : {'YES' if agree else 'NO'}")
    print(f"p-value gap         : {abs(p_t - p_w):.6g}")
    w_minus = -np.sum(ranks * (signs < 0))
    total = n * (n + 1) / 2
    rb = 1 - 2 * w_minus / total
    print(f"rank-biserial r     : {rb:+.4f}  (effect size for the signed-rank test)")

    if agree:
        print("\nBoth tests reach the same verdict here, so the choice between them does")
        print("not change the scientific conclusion.")
    elif p_w < p_t:
        print("\nThe Wilcoxon is significant while the t-test is not: the t-test's normality")
        print("assumption is doing the damage, and the non-parametric test is the correct")
        print("choice for this data shape.")
    else:
        print("\nThe t-test is significant while the Wilcoxon is not: with a small sample and large ranking variance the Wilcoxon simply has lower power here. Neither result is 'wrong' - they test slightly different nulls (mean vs median).")
    return p_t, p_w, agree


def main():
    banner("PRACTICE 4 : Wilcoxon Signed-Rank vs Paired t-Test")

    before = np.array([148, 152, 149, 155, 151, 158, 146, 157, 150, 153], dtype=float)

    diff_a = np.array([7.0, 8.5, 6.5, 9.0, 7.5, 8.0, 6.0, 8.8, 7.2, 9.2])
    paired_comparison(before, before - diff_a,
                      "CASE A : symmetric, near-normal differences")

    # Case B: one grossly mis-measured patient. The outlier inflates the sd of the
    # differences, which is exactly what the t-test's standard error is built from,
    # while the Wilcoxon only ranks them and is unaffected.
    diff_b = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 20.0])
    paired_comparison(before, before - diff_b,
                      "CASE B : one gross outlier in the differences")

    banner("WHEN TO USE WHICH")
    print("Paired t-test")
    print("  needs    : differences approximately normal, or n large (> ~30).")
    print("  answers  : 'did the MEAN change?'")
    print("  sensitive: to outliers and to skew in the differences.")
    print("Wilcoxon signed-rank")
    print("  needs    : a continuous or ordinal paired scale, differences roughly symmetric.")
    print("  answers  : 'did the typical (median) value change?'")
    print("  sensitive: to outliers, but needs the shape to be at least symmetric.")
    print("\nNeither test cares that the two columns are separate groups - pairing is what makes the difference analysis powerful, and that is why ttest_rel/wilcoxon must be fed matched pairs, never two unrelated samples.")


if __name__ == "__main__":
    main()