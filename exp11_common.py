import os

import numpy as np
import pandas as pd
from scipy import stats

ALPHA = 0.05
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

DATASETS = {
    "titanic": (
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv",
        "titanic",
    ),
    "tips": (
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
        "tips",
    ),
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