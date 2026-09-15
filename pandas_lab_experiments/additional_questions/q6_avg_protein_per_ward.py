"""Additional Question 6: Average protein reading per ward"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q6: AVERAGE PROTEIN READING PER WARD")
print("=" * 70)

print(f"\nMissing Protein_Reading values: {df['Protein_Reading'].isnull().sum()}")

if df["Protein_Reading"].isnull().sum() > 0:
    protein_mean = df["Protein_Reading"].mean()
    print(f"Filling missing values with mean: {protein_mean:.2f}")
    df["Protein_Reading"] = df["Protein_Reading"].fillna(protein_mean)

avg_protein = df.groupby("Ward")["Protein_Reading"].agg(["mean", "min", "max", "count", "std"])
avg_protein.columns = ["Average", "Minimum", "Maximum", "Count", "Std_Dev"]
avg_protein = avg_protein.round(2)

print("\nProtein Reading Statistics by Ward:")
print("-" * 60)
print(avg_protein.to_string())

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

sorted_protein = avg_protein.sort_values("Average", ascending=False)
print("\nWards ranked by average protein (highest to lowest):")
for i, (ward, row) in enumerate(sorted_protein.iterrows(), 1):
    print(f"  {i}. {ward}: {row['Average']:.2f} mg/dL (n={int(row['Count'])})")

highest = avg_protein["Average"].idxmax()
lowest = avg_protein["Average"].idxmin()

print(f"\nHighest average protein: {highest} ({avg_protein.loc[highest, 'Average']:.2f} mg/dL)")
print(f"Lowest average protein: {lowest} ({avg_protein.loc[lowest, 'Average']:.2f} mg/dL)")

print("\n" + "=" * 60)
print("DETAILED BREAKDOWN BY WARD")
print("=" * 60)
for ward in sorted(df["Ward"].unique()):
    ward_data = df[df["Ward"] == ward]
    print(f"\n{ward}:")
    for _, row in ward_data.iterrows():
        print(f"  {row['Patient_ID']}: {row['Protein_Reading']:.1f} mg/dL")
