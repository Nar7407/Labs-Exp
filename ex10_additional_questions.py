import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_data_from_csv():
    glucose_csv = os.path.join(SCRIPT_DIR, "glucose_readings.csv")
    abnormality_csv = os.path.join(SCRIPT_DIR, "ward_abnormality.csv")

    if not os.path.exists(glucose_csv):
        pd.DataFrame({
            "Monitoring Day": [0, 3, 6, 9, 12, 15, 18, 21, 24],
            "Phase": ["Baseline", "Baseline", "Rising", "Rising", "Peak",
                      "Peak", "Peak", "Recovery", "Recovery"],
            "Glucose Reading (mg/dL)": [108, 122, 138, 151, 166, 182, 158, 144, 128],
            "Protein Reading (mg/dL)": [12, 14, 18, 24, 30, 34, 26, 20, 15],
        }).to_csv(glucose_csv, index=False)
        print(f"Created {glucose_csv}")

    if not os.path.exists(abnormality_csv):
        pd.DataFrame(
            [[22, 35, 48, 61, 30],
             [28, 42, 55, 67, 36],
             [18, 31, 51, 73, 44],
             [32, 46, 63, 69, 41]],
            index=["Ward A", "Ward B", "Ward C", "Ward D"],
            columns=["S1", "S2", "S3", "S4", "S5"]).to_csv(abnormality_csv)
        print(f"Created {abnormality_csv}")

    glucose_df = pd.read_csv(glucose_csv)
    abnormality_df = pd.read_csv(abnormality_csv, index_col=0)
    abnormality_df.index.name = "Ward"
    abnormality_df.columns.name = "Section"
    return glucose_df, abnormality_df


def main():
    glucose_df, abnormality_df = load_data_from_csv()
    print("Glucose data loaded from CSV:")
    print(glucose_df, "\n")

    plt.figure(figsize=(11, 6))
    sns.lineplot(data=glucose_df, x="Monitoring Day",
                 y="Glucose Reading (mg/dL)",
                 marker="o", markersize=8, linestyle="--", linewidth=2.5,
                 color="tab:red", label="Glucose (mg/dL)")
    sns.lineplot(data=glucose_df, x="Monitoring Day",
                 y="Protein Reading (mg/dL)",
                 marker="s", markersize=8, linestyle="-.", linewidth=2.5,
                 color="tab:blue", label="Protein (mg/dL)")

    THRESHOLD = 150
    plt.axhline(y=THRESHOLD, color="green", linestyle=":", linewidth=2,
                label=f"Threshold ({THRESHOLD} mg/dL)")
    above = glucose_df[glucose_df["Glucose Reading (mg/dL)"] > THRESHOLD]
    plt.scatter(above["Monitoring Day"], above["Glucose Reading (mg/dL)"],
                color="darkgreen", s=120, zorder=5, marker="*",
                label="Readings above threshold")

    plt.title("Glucose and Protein Readings with Threshold Indicator")
    plt.xlabel("Monitoring Day")
    plt.ylabel("Reading Value")
    plt.legend(fontsize=9)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_glucose_protein_plot.png"), dpi=150, bbox_inches="tight")
    print("Saved: ex10_glucose_protein_plot.png")
    plt.show()

    print("\nReadings above the 150 mg/dL threshold:")
    print(above.to_string(index=False))

    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))

    sns.heatmap(abnormality_df, annot=True, fmt="d", cmap="viridis",
                linewidths=0.5, ax=axes[0],
                cbar_kws={"label": "Abnormality Index (AI)"})
    axes[0].set_title("Heat Map with 'viridis' Palette")
    axes[0].set_xlabel("Hospital Section")
    axes[0].set_ylabel("Ward")

    filtered = abnormality_df.where(abnormality_df >= 50)
    sns.heatmap(filtered, annot=True, fmt=".0f", cmap="Reds",
                linewidths=0.5, ax=axes[1],
                cbar_kws={"label": "Abnormality Index (AI >= 50)"})
    axes[1].set_title("Heat Map - Only Sections with AI >= 50")
    axes[1].set_xlabel("Hospital Section")
    axes[1].set_ylabel("Ward")

    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_ward_heatmaps.png"), dpi=150, bbox_inches="tight")
    print("Saved: ex10_ward_heatmaps.png")
    plt.show()

    print("\nEffect of palette: 'viridis' separates mid-range values better")
    print("(uniform brightness), but 'YlOrRd' communicates severity more")
    print("intuitively (darker/redder = more abnormal).")

    avg_by_ward = abnormality_df.mean(axis=1).round(2)
    print("\nAverage AI per ward:")
    print(avg_by_ward.to_string())
    top_ward = avg_by_ward.idxmax()
    print(f"Ward with the HIGHEST average abnormality: {top_ward} "
          f"(avg AI = {avg_by_ward.max()})")

    order = ["Baseline", "Rising", "Peak", "Recovery"]
    plt.figure(figsize=(9, 6))
    sns.boxplot(data=glucose_df, x="Phase", y="Glucose Reading (mg/dL)",
                hue="Phase", palette="Set2", order=order)
    sns.swarmplot(data=glucose_df, x="Phase", y="Glucose Reading (mg/dL)",
                  color="black", size=6, order=order)
    plt.title("Glucose Distribution Across Monitoring Phases")
    plt.xlabel("Monitoring Phase")
    plt.ylabel("Glucose Reading (mg/dL)")
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_additional_boxplot_swarm.png"), dpi=150, bbox_inches="tight")
    plt.show()

    print("\nAdvantage of Seaborn over Matplotlib:")
    print("1. DataFrame-aware API: columns are referenced by name, so no")
    print("   manual list extraction or index bookkeeping is needed.")
    print("2. Built-in statistics: means with confidence-interval bands,")
    print("   regression fits, box/violin quartiles and KDE curves are")
    print("   computed automatically - Matplotlib would need NumPy/pandas")
    print("   aggregation code for each of these.")
    print("3. Far less code: a single sns.heatmap(...) call replaces the")
    print("   imshow + colorbar + tick-label + annotation plumbing that")
    print("   raw Matplotlib requires.")
    print("4. Attractive defaults: colour palettes, styles and legends are")
    print("   tuned for statistical graphics and are easy to switch.")
    print("5. Figure-level functions (catplot, relplot, pairplot, FacetGrid)")
    print("   build multi-panel, faceted charts in one line.")


if __name__ == "__main__":
    main()
