import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("=" * 70)
print("TECHNICIAN-WISE ANALYSIS")
print("=" * 70)

tech_grouped = df.groupby("Technician_ID")

tech_analysis = df.groupby("Technician_ID").agg({
    "Turnaround_Time": ["count", "mean", "min", "max", "sum"],
    "Patient_ID": "count",
    "Glucose_Reading": "mean"
}).round(2)

tech_analysis.columns = ["Samples_Processed", "Avg_Turnaround", "Min_Turnaround",
                         "Max_Turnaround", "Total_Turnaround", "Patient_Count", "Avg_Glucose"]

print("\nTechnician Performance Summary:")
print("-" * 70)
print(f"{'Technician':<12} {'Samples':<10} {'Avg Time':<12} {'Min Time':<10} {'Max Time':<10}")
print("-" * 70)

for tech_id in sorted(df["Technician_ID"].unique()):
    tech_data = df[df["Technician_ID"] == tech_id]
    samples = len(tech_data)
    avg_time = tech_data["Turnaround_Time"].mean()
    min_time = tech_data["Turnaround_Time"].min()
    max_time = tech_data["Turnaround_Time"].max()

    print(f"{tech_id:<12} {samples:<10} {avg_time:<12.2f} {min_time:<10.2f} {max_time:<10.2f}")

print("-" * 70)

print("\n" + "=" * 60)
print("PERFORMANCE INSIGHTS")
print("=" * 60)

fastest_tech = df.groupby("Technician_ID")["Turnaround_Time"].mean().idxmin()
fastest_time = df.groupby("Technician_ID")["Turnaround_Time"].mean().min()

slowest_tech = df.groupby("Technician_ID")["Turnaround_Time"].mean().idxmax()
slowest_time = df.groupby("Technician_ID")["Turnaround_Time"].mean().max()

print(f"\nFASTEST Technician (lowest avg turnaround):")
print(f"  {fastest_tech}: {fastest_time:.2f} minutes average")

print(f"\nSLOWEST Technician (highest avg turnaround):")
print(f"  {slowest_tech}: {slowest_time:.2f} minutes average")

print("\nDetailed breakdown per technician:")
for tech_id in sorted(df["Technician_ID"].unique()):
    tech_data = df[df["Technician_ID"] == tech_id]
    print(f"\n{tech_id}:")
    print(f"  Patients: {list(tech_data['Patient_ID'])}")
    print(f"  Wards served: {list(tech_data['Ward'].unique())}")
    print(f"  Turnaround times: {list(tech_data['Turnaround_Time'])}")
