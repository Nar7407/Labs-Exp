"""Additional Question 7: Technician with highest avg glucose"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("=" * 70)
print("Q7: TECHNICIAN WITH HIGHEST AVERAGE GLUCOSE READING")
print("=" * 70)

tech_glucose = df.groupby("Technician_ID")["Glucose_Reading"].agg([
    ("Average_Glucose", "mean"),
    ("Min_Glucose", "min"),
    ("Max_Glucose", "max"),
    ("Sample_Count", "count"),
    ("Std_Glucose", "std")
]).round(2)

print("\nAverage Glucose Reading by Technician:")
print("-" * 60)
print(f"{'Technician':<12} {'Avg Glucose':<15} {'Min':<10} {'Max':<10} {'Samples':<10}")
print("-" * 60)
for tech, row in tech_glucose.iterrows():
    print(f"{tech:<12} {row['Average_Glucose']:<15.2f} {row['Min_Glucose']:<10.2f} {row['Max_Glucose']:<10.2f} {int(row['Sample_Count']):<10}")
print("-" * 60)

highest_tech = tech_glucose["Average_Glucose"].idxmax()
highest_avg = tech_glucose["Average_Glucose"].max()

print(f"\nTechnician with HIGHEST Average Glucose: {highest_tech}")
print(f"Average Glucose Reading: {highest_avg:.2f} mg/dL")

print("\n" + "=" * 60)
print("TECHNICIANS RANKED BY AVERAGE GLUCOSE (HIGHEST TO LOWEST)")
print("=" * 60)
sorted_tech = tech_glucose.sort_values("Average_Glucose", ascending=False)
for i, (tech, row) in enumerate(sorted_tech.iterrows(), 1):
    marker = " <-- HIGHEST" if tech == highest_tech else ""
    print(f"  {i}. {tech}: {row['Average_Glucose']:.2f} mg/dL ({int(row['Sample_Count'])} samples){marker}")

print("\n" + "=" * 60)
print(f"DETAILED BREAKDOWN: {highest_tech}")
print("=" * 60)
tech_data = df[df["Technician_ID"] == highest_tech]
print(f"\nSamples processed: {len(tech_data)}")
print(f"Patients: {list(tech_data['Patient_ID'])}")
print(f"Wards served: {list(tech_data['Ward'].unique())}")
print("\nIndividual readings:")
for _, row in tech_data.iterrows():
    status = "HIGH" if row["Glucose_Reading"] > 140 else "Normal"
    print(f"  {row['Patient_ID']}: {row['Glucose_Reading']:.2f} mg/dL [{status}] ({row['Ward']})")
