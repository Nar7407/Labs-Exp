"""AI Case Study: Patient Test-Result Analysis using Pandas DataFrame - Task 10"""

import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

print("=" * 60)
print("IDENTIFYING WARD WITH HIGHEST AVERAGE TURNAROUND TIME")
print("=" * 60)

avg_turnaround = df.groupby("Ward")["Turnaround_Time"].mean()

print("\nAverage Turnaround Time by Ward:")
print("-" * 45)
for ward, avg_time in avg_turnaround.items():
    print(f"  {ward}: {avg_time:.2f} minutes")
print("-" * 45)

max_ward = avg_turnaround.idxmax()
max_time = avg_turnaround.max()

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)
print(f"Ward Requiring Maximum Average Turnaround:")
print(f"{max_ward}")
print(f"Average Turnaround Time:")
print(f"{max_time:.2f} minutes")

print("\n" + "=" * 60)
print("DETAILED BREAKDOWN FOR HIGHEST TURNAROUND WARD")
print("=" * 60)
max_ward_data = df[df["Ward"] == max_ward]
print(f"\n{max_ward} - All Records:")
for _, row in max_ward_data.iterrows():
    print(f"  Patient {row['Patient_ID']}: {row['Turnaround_Time']} minutes")

print(f"\nTotal samples from {max_ward}: {len(max_ward_data)}")
print(f"Total turnaround time: {max_ward_data['Turnaround_Time'].sum()} minutes")
print(f"Average turnaround time: {max_ward_data['Turnaround_Time'].mean():.2f} minutes")

print("\n" + "=" * 60)
print("COMPARISON WITH OTHER WARDS")
print("=" * 60)
for ward in avg_turnaround.index:
    if ward != max_ward:
        diff = max_time - avg_turnaround[ward]
        print(f"  {ward}: {diff:.2f} minutes faster than {max_ward}")
