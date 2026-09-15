import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("=" * 60)
print("PATIENT RECORDS WITH GLUCOSE READING > 140 mg/dL")
print("=" * 60)

high_glucose_patients = df[df["Glucose_Reading"] > 140]

print(f"\nTotal patients with glucose > 140 mg/dL: {len(high_glucose_patients)}")
print(f"Out of total {len(df)} patients")

print("\nDetailed records:")
print(high_glucose_patients[["Patient_ID", "Age", "Ward", "Glucose_Reading", "Sample_Type"]].to_string(index=False))

print("\n" + "=" * 60)
print("ADDITIONAL INSIGHTS")
print("=" * 60)

print("\nPatients with high glucose by ward:")
ward_counts = high_glucose_patients.groupby("Ward").size()
for ward, count in ward_counts.items():
    print(f"  {ward}: {count} patients")

print("\nPatients with high glucose by sample type:")
sample_counts = high_glucose_patients.groupby("Sample_Type").size()
for sample_type, count in sample_counts.items():
    print(f"  {sample_type}: {count} patients")
