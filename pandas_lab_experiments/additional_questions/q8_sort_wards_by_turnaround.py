"""Additional Question 8: Sort wards by average turnaround descending"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 70)
print("Q8: WARDS SORTED BY AVERAGE TURNAROUND TIME (DESCENDING)")
print("=" * 70)

avg_turnaround = df.groupby("Ward")["Turnaround_Time"].agg([
    ("Average_Turnaround", "mean"),
    ("Total_Turnaround", "sum"),
    ("Min_Turnaround", "min"),
    ("Max_Turnaround", "max"),
    ("Sample_Count", "count")
]).round(2)

sorted_wards = avg_turnaround.sort_values("Average_Turnaround", ascending=False)

print("\nWards Sorted by Average Turnaround Time (Descending):")
print("-" * 80)
print(f"{'Rank':<6} {'Ward':<12} {'Avg Time':<12} {'Total':<10} {'Min':<8} {'Max':<8} {'Count':<8}")
print("-" * 80)

for rank, (ward, row) in enumerate(sorted_wards.iterrows(), 1):
    print(f"{rank:<6} {ward:<12} {row['Average_Turnaround']:<12.2f} {row['Total_Turnaround']:<10.2f} {row['Min_Turnaround']:<8.2f} {row['Max_Turnaround']:<8.2f} {int(row['Sample_Count']):<8}")

print("-" * 80)

print("\n" + "=" * 60)
print("ALTERNATIVE METHODS")
print("=" * 60)

turnaround_series = df.groupby("Ward")["Turnaround_Time"].mean().sort_values(ascending=False)
print("\nMethod 1 - Series.sort_values(ascending=False):")
print(turnaround_series)

turnaround_series2 = df.groupby("Ward")["Turnaround_Time"].mean()
print("\nMethod 2 - Using nlargest(3):")
print(turnaround_series2.nlargest(3))

print("\n" + "=" * 60)
print("INTERPRETATION")
print("=" * 60)
fastest = sorted_wards.index[-1]
slowest = sorted_wards.index[0]
print(f"\nFASTEST Ward (lowest avg time): {fastest} ({sorted_wards.loc[fastest, 'Average_Turnaround']:.2f} min)")
print(f"SLOWEST Ward (highest avg time): {slowest} ({sorted_wards.loc[slowest, 'Average_Turnaround']:.2f} min)")
print(f"\nDifference: {sorted_wards.loc[slowest, 'Average_Turnaround'] - sorted_wards.loc[fastest, 'Average_Turnaround']:.2f} minutes")
