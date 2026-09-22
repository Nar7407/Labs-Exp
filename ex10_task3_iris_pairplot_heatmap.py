import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IRIS_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def load_iris():
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iris.csv")
    if os.path.exists(local_path):
        return pd.read_csv(local_path)
    return pd.read_csv(IRIS_URL)


def main():
    df = load_iris()
    print(f"Loaded Iris dataset: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Columns: {list(df.columns)}")

    numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

    g = sns.pairplot(df, vars=numeric_cols, hue="species",
                     palette="bright", diag_kind="kde",
                     plot_kws={"alpha": 0.7, "s": 25})
    g.fig.suptitle("Task 3: Iris Pairplot Coloured by Species",
                   y=1.02, fontsize=14, fontweight="bold")
    g.savefig(os.path.join(SCRIPT_DIR, "ex10_task3_iris_pairplot.png"), dpi=150, bbox_inches="tight")
    plt.show()

    corr_matrix = df[numeric_cols].corr()
    print("\nCorrelation Matrix:")
    print(corr_matrix.round(3))

    plt.figure(figsize=(7, 6))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
                vmin=-1, vmax=1, square=True, linewidths=0.5)
    plt.title("Iris: Correlation Heat Map of Numerical Features")
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_task3_iris_heatmap.png"), dpi=150, bbox_inches="tight")
    plt.show()

    stacked = corr_matrix.unstack()
    strongest = stacked[stacked.index.get_level_values(0) !=
                        stacked.index.get_level_values(1)].idxmax()

    print("\n--- Strongest Correlation ---")
    print(f"Pair of measurements : {strongest[0]} <-> {strongest[1]}")
    print(f"Correlation value    : {stacked[strongest]:.3f}")



