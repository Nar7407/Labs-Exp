import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("=" * 70)
print("Q5: PATIENTS WITH GLUCOSE > 180 mg/dL AND TURNAROUND > 50 min")
print("=" * 70)

high_risk_patients = df[(df["Glucose_Reading"] > 180) & (df["Turnaround_Time"] > 50)]

print(f"\nNumber of patients meeting both criteria: {len(high_risk_patients)}")

if len(high_risk_patients) > 0:
    print("\nHigh-risk patients (high glucose + long turnaround):")
    print("-" * 80)
    print(f"{'Patient_ID':<12} {'Age':<6} {'Ward':<10} {'Glucose':<12} {'Turnaround':<12} {'Tech':<10}")
    print("-" * 80)
    for _, row in high_risk_patients.iterrows():
        print(f"{row['Patient_ID']:<12} {row['Age']:<6} {row['Ward']:<10} {row['Glucose_Reading']:<12.2f} {row['Turnaround_Time']:<12} {row['Technician_ID']:<10}")
    print("-" * 80)

    print("\n" + "=" * 60)
    print("INSIGHTS")
    print("=" * 60)
    print(f"\nWards represented: {list(high_risk_patients['Ward'].unique())}")
    print(f"Technicians involved: {list(high_risk_patients['Technician_ID'].unique())}")
    print(f"\nThese patients require immediate attention due to:")
    print("  1. Elevated glucose levels (>180 mg/dL = hyperglycemia)")
    print("  2. Extended turnaround time (>50 minutes = delayed results)")
else:
    print("\nNo patients meet both criteria simultaneously.")

print("\n" + "=" * 70)
print("ALTERNATIVE: Patients meeting EITHER condition (OR)")
print("=" * 70)
either_condition = df[(df["Glucose_Reading"] > 180) | (df["Turnaround_Time"] > 50)]
print(f"\nPatients with Glucose > 180 OR Turnaround > 50: {len(either_condition)}")
for _, row in either_condition.iterrows():
    reasons = []
    if row["Glucose_Reading"] > 180:
        reasons.append("High Glucose")
    if row["Turnaround_Time"] > 50:
        reasons.append("Long Turnaround")
    print(f"  {row['Patient_ID']}: {', '.join(reasons)}")
