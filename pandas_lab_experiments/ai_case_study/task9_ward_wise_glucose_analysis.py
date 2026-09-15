import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))

glucose_avg = df["Glucose_Reading"].mean()
df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_avg)

print("=" * 70)
print("WARD-WISE GLUCOSE ANALYSIS")
print("=" * 70)

ward_glucose_stats = df.groupby("Ward")["Glucose_Reading"].agg([
    ("Average", "mean"),
    ("Minimum", "min"),
    ("Maximum", "max"),
    ("Count", "count")
]).round(2)

print("\nGlucose Reading Statistics by Ward:")
print("-" * 65)
print(f"{'Ward':<12} {'Count':<8} {'Average':<10} {'Minimum':<10} {'Maximum':<10}")
print("-" * 65)

for ward, row in ward_glucose_stats.iterrows():
    print(f"{ward:<12} {int(row['Count']):<8} {row['Average']:<10.2f} {row['Minimum']:<10.2f} {row['Maximum']:<10.2f}")

print("-" * 65)

highest_avg_ward = ward_glucose_stats["Average"].idxmax()
highest_avg_value = ward_glucose_stats["Average"].max()

lowest_avg_ward = ward_glucose_stats["Average"].idxmin()
lowest_avg_value = ward_glucose_stats["Average"].min()

print(f"\nWARD WITH HIGHEST AVERAGE GLUCOSE READING:")
print(f"  {highest_avg_ward}: {highest_avg_value:.2f} mg/dL")

print(f"\nWARD WITH LOWEST AVERAGE GLUCOSE READING:")
print(f"  {lowest_avg_ward}: {lowest_avg_value:.2f} mg/dL")

print("\n" + "=" * 60)
print("ADDITIONAL INSIGHTS")
print("=" * 60)

sorted_wards = ward_glucose_stats.sort_values("Average", ascending=False)
print("\nWards ranked by average glucose (highest to lowest):")
for i, (ward, row) in enumerate(sorted_wards.iterrows(), 1):
    print(f"  {i}. {ward}: {row['Average']:.2f} mg/dL")

print("\nWards with average glucose > 140 mg/dL (potential concern):")
high_glucose_wards = ward_glucose_stats[ward_glucose_stats["Average"] > 140]
if len(high_glucose_wards) > 0:
    for ward, row in high_glucose_wards.iterrows():
        print(f"  - {ward}: {row['Average']:.2f} mg/dL")
else:
    print("  No wards have average glucose above 140 mg/dL")

print(f"\nDetailed breakdown for {highest_avg_ward}:")
high_ward_data = df[df["Ward"] == highest_avg_ward]
for _, row in high_ward_data.iterrows():
    status = "HIGH" if row["Glucose_Reading"] > 140 else "Normal"
    print(f"  {row['Patient_ID']}: {row['Glucose_Reading']:.2f} mg/dL [{status}]")
