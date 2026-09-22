import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def classify_ai(value):
    if value < 30:
        return "Low Abnormality"
    elif value < 50:
        return "Moderate Abnormality"
    elif value < 70:
        return "High Abnormality"
    else:
        return "Severe Abnormality"


def main():
    glucose_df = pd.DataFrame({
        "Monitoring Day": [0, 3, 6, 9, 12, 15, 18, 21, 24],
        "Phase": ["Baseline", "Baseline", "Rising", "Rising", "Peak",
                  "Peak", "Peak", "Recovery", "Recovery"],
        "Glucose Reading (mg/dL)": [108, 122, 138, 151, 166, 182, 158, 144, 128],
    })
    print("Patient Glucose Monitoring Data:")
    print(glucose_df, "\n")

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=glucose_df,
                 x="Monitoring Day", y="Glucose Reading (mg/dL)",
                 hue="Phase", style="Phase",
                 markers={"Baseline": "o", "Rising": "s",
                          "Peak": "^", "Recovery": "D"},
                 dashes=False, palette="Set1", linewidth=2.5)
    sns.lineplot(data=glucose_df, x="Monitoring Day",
                 y="Glucose Reading (mg/dL)",
                 color="grey", alpha=0.35, linewidth=1.2, legend=False)

    plt.axhline(y=140, color="red", linestyle="--", linewidth=1.5,
                label="Critical Level (140 mg/dL)")

    max_row = glucose_df.loc[glucose_df["Glucose Reading (mg/dL)"].idxmax()]
    plt.scatter(max_row["Monitoring Day"], max_row["Glucose Reading (mg/dL)"],
                color="darkred", s=150, zorder=5, marker="*",
                label=f"Maximum ({int(max_row['Monitoring Day'])} mg/dL)")
    plt.annotate(f"Peak: {max_row['Glucose Reading (mg/dL)']} mg/dL "
                 f"on Day {int(max_row['Monitoring Day'])}",
                 xy=(max_row["Monitoring Day"],
                     max_row["Glucose Reading (mg/dL)"]),
                 xytext=(max_row["Monitoring Day"] - 8,
                         max_row["Glucose Reading (mg/dL)"] + 6),
                 arrowprops=dict(arrowstyle="->", color="darkred"))

    plt.title("Patient Glucose Variation Across Monitoring Phases")
    plt.xlabel("Monitoring Day")
    plt.ylabel("Glucose Reading (mg/dL)")
    plt.legend(title="Phase", loc="lower right", fontsize=9)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_ai_glucose_variation.png"), dpi=150, bbox_inches="tight")
    plt.show()

    abnormality_df = pd.DataFrame(
        [[22, 35, 48, 61, 30],
         [28, 42, 55, 67, 36],
         [18, 31, 51, 73, 44],
         [32, 46, 63, 69, 41]],
        index=["Ward A", "Ward B", "Ward C", "Ward D"],
        columns=["S1", "S2", "S3", "S4", "S5"])
    abnormality_df.index.name = "Ward"
    abnormality_df.columns.name = "Section"
    print("\nWard-wise Abnormality Index:")
    print(abnormality_df, "\n")

    plt.figure(figsize=(9, 6))
    sns.heatmap(abnormality_df, annot=True, fmt="d", cmap="YlOrRd",
                linewidths=0.5, linecolor="white",
                cbar_kws={"label": "Abnormality Index (AI)"})
    plt.title("Ward-wise Abnormality Index Heat Map")
    plt.xlabel("Hospital Section")
    plt.ylabel("Ward")
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_ai_ward_heatmap.png"), dpi=150, bbox_inches="tight")
    plt.show()

    max_cell = abnormality_df.stack().idxmax()
    max_value = abnormality_df.stack().max()
    severe_cells = abnormality_df[abnormality_df >= 70].stack()

    print("\n--- Heat Map Analysis ---")
    print(f"Ward/Section with highest abnormality : {max_cell[0]} / {max_cell[1]}")
    print(f"Maximum AI value                      : {max_value}")
    print(f"Number of cells with AI >= 70         : {len(severe_cells)}")
    for (ward, section), value in severe_cells.items():
        print(f"    {ward} / {section} -> AI = {value} ({classify_ai(value)})")

    print("\nCell-by-cell classification:")
    for (ward, section), value in abnormality_df.stack().items():
        print(f"    {ward} / {section} -> AI = {value:2d} : {classify_ai(value)}")

    print("\n--- Interpretation ---")
    print("Glucose: the reading rises from the Baseline phase and peaks at")
    print(f"{max_row['Glucose Reading (mg/dL)']} mg/dL on Day "
          f"{int(max_row['Monitoring Day'])} (Peak phase). It stays above the")
    print("140 mg/dL critical line from Day 9 through Day 21. YES - the patient")
    print("requires clinical attention during the later (Peak and early")
    print("Recovery) phases, since readings remain critically high.")
    print("Heat map: Section S4 of every ward is High/Severe, with Ward C / S4")
    print("(AI = 73) the single worst cell - it needs priority attention.")
    print("Ward B / S4 and Ward D / S4 (AI = 67, 69) are close behind.")


if __name__ == "__main__":
    main()
