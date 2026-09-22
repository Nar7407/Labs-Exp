import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(seed=42)


def task1_strip_swarm():
    n_per_group = 25
    methods = (["Self-Study"] * n_per_group +
               ["Coaching"] * n_per_group +
               ["Group Study"] * n_per_group)
    scores = np.concatenate([
        rng.normal(62, 10, n_per_group),
        rng.normal(72, 8, n_per_group),
        rng.normal(68, 9, n_per_group),
    ]).clip(0, 100).round()

    df = pd.DataFrame({"Study Method": methods, "Exam Score": scores})

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), sharey=True)

    sns.stripplot(x="Study Method", y="Exam Score", data=df,
                  ax=axes[0], palette="Set2", size=6, jitter=0.25,
                  hue="Study Method")
    axes[0].set_title("Stripplot: Exam Scores by Study Method")
    axes[0].set_xlabel("Study Method")
    axes[0].set_ylabel("Exam Score")

    sns.swarmplot(x="Study Method", y="Exam Score", data=df,
                  ax=axes[1], palette="Set1", size=6,
                  hue="Study Method")
    axes[1].set_title("Swarmplot: Exam Scores by Study Method")
    axes[1].set_xlabel("Study Method")
    axes[1].set_ylabel("Exam Score")

    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_practice_task1_strip_swarm.png"), dpi=150, bbox_inches="tight")
    plt.show()


def task2_lineplot_hue():
    months = list(range(1, 13))
    product_a = [120, 132, 125, 140, 150, 162, 158, 170, 180, 175, 190, 205]
    product_b = [90, 85, 95, 88, 102, 98, 110, 115, 108, 120, 118, 128]
    product_c = [60, 70, 65, 80, 78, 90, 95, 92, 105, 100, 112, 120]

    df = pd.DataFrame({
        "Month": months * 3,
        "Sales": product_a + product_b + product_c,
        "Product": ["Product A"] * 12 + ["Product B"] * 12 + ["Product C"] * 12,
    })

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="Month", y="Sales", hue="Product",
                 marker="o", linewidth=2.5, palette="bright")
    plt.title("Monthly Sales Trends of Three Products")
    plt.xlabel("Month (1-12)")
    plt.ylabel("Units Sold")
    plt.xticks(months)
    plt.legend(title="Product")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_practice_task2_lineplot.png"), dpi=150, bbox_inches="tight")
    plt.show()


def task3_facetgrid_hist():
    branches = ["CSBS", "EXCP", "VLSI"] * 30
    marks = np.concatenate([
        rng.normal(72, 8, 30),
        rng.normal(65, 10, 30),
        rng.normal(78, 6, 30),
    ]).clip(0, 100).round()

    df = pd.DataFrame({"Branch": branches, "Marks": marks})

    g = sns.FacetGrid(df, col="Branch", col_wrap=3, height=4)
    g.map(sns.histplot, "Marks", bins=10, kde=True, color="steelblue")
    g.set_axis_labels("Marks", "Number of Students")
    g.set_titles(col_template="{col_name} Branch")
    g.figure.suptitle("Distribution of Marks by Branch (FacetGrid)",
                      y=1.05, fontsize=13, fontweight="bold")
    g.savefig(os.path.join(SCRIPT_DIR, "ex10_practice_task3_facetgrid_hist.png"), dpi=150, bbox_inches="tight")
    plt.show()


def task4_pointplot_hue():
    data_rows = []
    for branch, base in [("CSBS", 72), ("EXCP", 65), ("VLSI", 78)]:
        for gender, shift in [("Male", -3), ("Female", 3)]:
            scores = rng.normal(base + shift, 6, 25).clip(0, 100).round()
            data_rows += [{"Branch": branch, "Gender": gender, "Marks": m}
                          for m in scores]

    df = pd.DataFrame(data_rows)

    plt.figure(figsize=(9, 6))
    sns.pointplot(data=df, x="Branch", y="Marks", hue="Gender",
                  palette="deep", capsize=0.1,
                  markers=["o", "s"], linestyles=["-", "--"], errorbar=None)
    plt.title("Average Marks by Branch and Gender (Point Plot)")
    plt.xlabel("Branch")
    plt.ylabel("Average Marks")
    plt.legend(title="Gender")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_practice_task4_pointplot.png"), dpi=150, bbox_inches="tight")
    plt.show()

    avg = df.groupby(["Branch", "Gender"])["Marks"].mean().round(2)
    print("Average marks by Branch and Gender:")
    print(avg)


def task5_confusion_heatmap():
    matrix = rng.integers(low=5, high=60, size=(4, 4))

    classes = ["Class 0", "Class 1", "Class 2", "Class 3"]
    plt.figure(figsize=(7, 6))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues",
                linewidths=0.5, linecolor="white",
                xticklabels=classes, yticklabels=classes,
                cbar_kws={"label": "Count"})
    plt.title("4x4 Confusion-Matrix-Style Heat Map (Integer Annotations)")
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_practice_task5_confusion_heatmap.png"), dpi=150, bbox_inches="tight")
    plt.show()

    print("Matrix used:")
    print(matrix)


if __name__ == "__main__":
    print("=" * 60)
    print("Practice Task 1: Stripplot vs Swarmplot")
    print("=" * 60)
    task1_strip_swarm()

    print("\n" + "=" * 60)
    print("Practice Task 2: Sales Line Plot with hue")
    print("=" * 60)
    task2_lineplot_hue()

    print("\n" + "=" * 60)
    print("Practice Task 3: FacetGrid Histograms")
    print("=" * 60)
    task3_facetgrid_hist()

    print("\n" + "=" * 60)
    print("Practice Task 4: Point Plot with Two Categories")
    print("=" * 60)
    task4_pointplot_hue()

    print("\n" + "=" * 60)
    print("Practice Task 5: 4x4 Confusion-Style Heat Map")
    print("=" * 60)
    task5_confusion_heatmap()
