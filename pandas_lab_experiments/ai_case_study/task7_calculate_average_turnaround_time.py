import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

print("=" * 60)
print("AVERAGE TURNAROUND TIME BY WARD")
print("=" * 60)

avg_turnaround = df.groupby("Ward")["Turnaround_Time"].mean()

print("\nAverage Turnaround Time by Ward:")
print("-" * 45)
print(f"{'Ward':<15} {'Avg Turnaround (minutes)':<25}")
print("-" * 45)
for ward, avg_time in avg_turnaround.items():
    print(f"{ward:<15} {avg_time:>22.2f}")
print("-" * 45)

print("\nDetailed breakdown by ward:")
for ward in df["Ward"].unique():
    ward_data = df[df["Ward"] == ward]
    total_time = ward_data["Turnaround_Time"].sum()
    num_samples = len(ward_data)
    avg_time = total_time / num_samples
    print(f"\n{ward}:")
    print(f"  Total Turnaround Time: {total_time} minutes")
    print(f"  Number of Samples: {num_samples}")
    print(f"  Average Turnaround Time: {avg_time:.2f} minutes")
    print(f"  Individual times: {list(ward_data['Turnaround_Time'])}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Ward with FASTEST average turnaround: {avg_turnaround.idxmin()} ({avg_turnaround.min():.2f} minutes)")
print(f"Ward with SLOWEST average turnaround: {avg_turnaround.idxmax()} ({avg_turnaround.max():.2f} minutes)")
