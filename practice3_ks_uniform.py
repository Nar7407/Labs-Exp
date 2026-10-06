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


def empirical_cdf_edges(sample, k=12):
    counts, edges = np.histogram(sample, bins=k, range=(0.0, 1.0))
    return counts, edges


def main():
    banner("PRACTICE 3 : One-Sample K-S Test against the Uniform Distribution")

    rng = np.random.default_rng(11)
    n = 200
    sample = rng.random(n)

    print(f"Generated {n} values from rng.random() (i.e. U(0, 1) by construction).")
    print(f"min = {sample.min():.4f}, max = {sample.max():.4f}")
    print(f"mean = {sample.mean():.4f} (expected 0.5), sd = {sample.std(ddof=1):.4f} (expected 0.2887)")

    print("\n--- Uniformity of the sample ---")
    print("-" * 72)
    counts, edges = empirical_cdf_edges(sample)
    width = edges[1] - edges[0]
    expected_per_bin = n * width
    print(f"{'bin':>12}{'observed':>10}{'expected':>10}")
    for i in range(len(counts)):
        print(f"{f'[{edges[i]:.3f},{edges[i + 1]:.3f})':>12}{counts[i]:>10}{expected_per_bin:>10.2f}")
    print(f"{'TOTAL':>12}{counts.sum():>10}{n:>10.2f}")

    print("\n--- Test 1 : K-S vs uniform (the required one-sample test) ---")
    print("-" * 72)
    d, p = stats.kstest(sample, "uniform", alternative="two-sided")
    report("kstest(sample, 'uniform')", d, p,
           "The sample comes from a uniform distribution on [0, 1]",
           "The sample does NOT come from a uniform distribution on [0, 1]")

    print(f"\nAsymptotic significance level for n = {n}: alpha_eff = {1 / np.sqrt(n):.4f}")
    crit = stats.kstwo.ppf(1 - ALPHA, n)
    print(f"Critical D (exact, n = {n})   : {crit:.4f}")
    print(f"Observed D                     : {d:.4f}")
    print(f"Conclusion : D {'>' if d > crit else '<='} crit -> "
          f"{'sample is NOT uniform' if d > crit else 'sample is consistent with uniformity'}")

    print("\n--- Test 2 : same sample vs a normal distribution (contrast of the two uses) ---")
    print("-" * 72)
    d2, p2 = stats.kstest(sample, "norm", args=(sample.mean(), sample.std(ddof=1)))
    report("kstest(sample, 'norm')", d2, p2,
           "The sample comes from a normal distribution",
           "The sample does NOT come from a normal distribution")
    print("\nThe K-S statistic measures the LARGEST gap between the empirical CDF and"
          "\nthe theoretical CDF, so it is sensitive to any departure - location,"
          "\nspread or shape - unlike a t-test which only compares means.")

    print("\n--- Test 3 : deliberately broken sample, to show a rejection ---")
    print("-" * 72)
    skewed = rng.beta(2, 5, n)
    d3, p3 = stats.kstest(skewed, "uniform")
    report("kstest(bias-skewed sample, 'uniform')", d3, p3,
           "The skewed sample comes from U(0, 1)",
           "The skewed sample does NOT come from U(0, 1)")
    print(f"This skewed sample's mean is {skewed.mean():.4f}, far from 0.5, so the"
          "\nK-S test rejects uniformity - confirming the test has power.")

    print("\nNote : kstest estimates no parameters here (uniform has none free), so the standard exact/asymptotic p-values are valid. With estimated parameters, use stats.kstest(..., method='permutation') - the plug-in p-value would be too optimistic.")


if __name__ == "__main__":
    main()
