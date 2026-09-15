import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q11: FLAGGING WARDS FOR CLINICAL MONITORING")
print("=" * 70)

print("\nCriteria for flagging:")
print("  1. Average Glucose Reading > 140 mg/dL")
print("  2. Average Turnaround Time > 50 minutes")
print("  Both conditions must be met to flag a ward.")

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

ward_stats = df.groupby("Ward").agg({
    "Glucose_Reading": ["mean", "min", "max", "count"],
    "Turnaround_Time": ["mean", "min", "max", "count"],
    "Patient_ID": "count"
}).round(2)

ward_stats.columns = [
    "Avg_Glucose", "Min_Glucose", "Max_Glucose", "Glucose_Count",
    "Avg_Turnaround", "Min_Turnaround", "Max_Turnaround", "Turnaround_Count",
    "Patient_Count"
]

ward_stats["Flagged_for_Monitoring"] = (
    (ward_stats["Avg_Glucose"] > 140) & 
    (ward_stats["Avg_Turnaround"] > 50)
)

print("\n" + "=" * 70)
print("WARD-WISE ANALYSIS WITH MONITORING FLAGS")
print("=" * 70)

print("\n" + "-" * 95)
print(f"{'Ward':<10} {'Patients':<10} {'Avg Glucose':<14} {'Avg Time':<12} {'Flagged':<10}")
print("-" * 95)

for ward, row in ward_stats.iterrows():
    flagged = "YES" if row["Flagged_for_Monitoring"] else "No"
    print(f"{ward:<10} {int(row['Patient_Count']):<10} {row['Avg_Glucose']:<14.2f} {row['Avg_Turnaround']:<12.2f} {flagged:<10}")

print("-" * 95)

flagged_wards = ward_stats[ward_stats["Flagged_for_Monitoring"]]

print("\n" + "=" * 70)
print("WARRANTS REQUIRING CLOSER CLINICAL MONITORING")
print("=" * 70)

if len(flagged_wards) > 0:
    print(f"\n{len(flagged_wards)} ward(s) flagged:\n")
    for ward, row in flagged_wards.iterrows():
        print(f"  {ward}")
        print(f"      - Average Glucose: {row['Avg_Glucose']:.2f} mg/dL (>140 threshold)")
        print(f"      - Average Turnaround: {row['Avg_Turnaround']:.2f} min (>50 threshold)")
        print(f"      - Patients: {int(row['Patient_Count'])}")
        print()
else:
    print("\nNo wards meet both criteria for flagging.")
    print("\nNote: Some wards may meet individual criteria:")

    high_glucose_wards = ward_stats[ward_stats["Avg_Glucose"] > 140]
    if len(high_glucose_wards) > 0:
        print(f"\n  Wards with high glucose (>140 mg/dL): {list(high_glucose_wards.index)}")

    high_turnaround_wards = ward_stats[ward_stats["Avg_Turnaround"] > 50]
    if len(high_turnaround_wards) > 0:
        print(f"  Wards with long turnaround (>50 min): {list(high_turnaround_wards.index)}")

print("\n" + "=" * 70)
print("DETAILED BREAKDOWN FOR FLAGGED WARDS")
print("=" * 70)

for ward in flagged_wards.index:
    ward_data = df[df["Ward"] == ward]
    print(f"\n{ward} - All Patient Records:")
    print("-" * 70)
    print(f"{'Patient_ID':<12} {'Age':<6} {'Glucose':<12} {'Protein':<10} {'Turnaround':<12} {'Status':<10}")
    print("-" * 70)
    for _, row in ward_data.iterrows():
        glucose_status = "HIGH" if row["Glucose_Reading"] > 140 else "Normal"
        turnaround_status = "LONG" if row["Turnaround_Time"] > 50 else "Normal"
        print(f"{row['Patient_ID']:<12} {row['Age']:<6} {row['Glucose_Reading']:<12.2f} {row['Protein_Reading']:<10.1f} {row['Turnaround_Time']:<12} {glucose_status}/{turnaround_status}")
    print("-" * 70)

print("\n" + "=" * 70)
print("RECOMMENDATIONS")
print("=" * 70)

if len(flagged_wards) > 0:
    print("""
Based on the analysis, the following actions are recommended for flagged wards:

1. INVESTIGATE CAUSES: Review why glucose readings are elevated and why
   turnaround times are extended in these wards.

2. RESOURCE ALLOCATION: Consider assigning additional staff or equipment
   to reduce turnaround times.

3. PATIENT MANAGEMENT: Implement tighter glucose monitoring protocols
   for patients in flagged wards.

4. PROCESS IMPROVEMENT: Identify bottlenecks in the testing workflow
   and address them systematically.
""")
else:
    print("""
All wards are currently within acceptable ranges for both metrics.
Continue routine monitoring and periodic analysis.
""")
