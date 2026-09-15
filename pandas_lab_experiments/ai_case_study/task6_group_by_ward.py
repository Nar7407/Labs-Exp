import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("=" * 60)
print("GROUPBY WARD - DATA EXPLORATION")
print("=" * 60)

grouped = df.groupby("Ward")

print("\nGroups created:")
for name, group in grouped:
    print(f"\n  {name}: {len(group)} patients")
    print(f"  Patients: {list(group['Patient_ID'])}")

print("\n" + "=" * 60)
print("WARD-WISE SUMMARY")
print("=" * 60)

print("\nNumber of patients per ward:")
print(df.groupby("Ward").size())

print("\nWard-wise patient details:")
for ward, group in grouped:
    print(f"\n{ward}:")
    print(f"  Patient IDs: {list(group['Patient_ID'])}")
    print(f"  Ages: {list(group['Age'])}")
    print(f"  Average Age: {group['Age'].mean():.1f}")
