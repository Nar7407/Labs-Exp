import os
import pandas as pd

def main():
    print("=" * 80)
    print("PATIENT TEST-RESULT ANALYSIS USING PANDAS")
    print("=" * 80)

    df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))
    print("\n[STEP 2] Loaded patient_tests.csv into DataFrame")

    print("\n" + "-" * 80)
    print("[STEP 3] DATASET STRUCTURE AND SUMMARY")
    print("-" * 80)
    print(f"\nDataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"\nColumn Names: {list(df.columns)}")
    print(f"\nData Types:\n{df.dtypes.to_string()}")
    print(f"\nStatistical Summary:\n{df.describe().to_string()}")

    print("\n" + "-" * 80)
    print("[STEP 4] MISSING VALUES ANALYSIS")
    print("-" * 80)
    missing_counts = df.isnull().sum()
    missing_pct = (missing_counts / len(df)) * 100

    missing_df = pd.DataFrame({
        "Column": missing_counts.index,
        "Missing_Count": missing_counts.values,
        "Missing_Percentage": missing_pct.values
    })
    print(f"\n{missing_df.to_string(index=False)}")
    print(f"\nTotal missing values: {missing_counts.sum()}")

    print("\n" + "-" * 80)
    print("[STEP 5] HANDLING MISSING GLUCOSE VALUES")
    print("-" * 80)
    glucose_mean = df["Glucose_Reading"].mean()
    print(f"\nMean glucose reading (from available data): {glucose_mean:.2f} mg/dL")
    df["Glucose_Reading"] = df["Glucose_Reading"].fillna(glucose_mean)
    print(f"Missing glucose values after imputation: {df['Glucose_Reading'].isnull().sum()}")

    print("\n" + "-" * 80)
    print("[STEP 6] PATIENTS WITH GLUCOSE > 140 mg/dL")
    print("-" * 80)
    high_glucose = df[df["Glucose_Reading"] > 140]
    print(f"\nNumber of patients with glucose > 140 mg/dL: {len(high_glucose)}")
    print(f"\n{high_glucose[['Patient_ID', 'Age', 'Ward', 'Glucose_Reading', 'Sample_Type']].to_string(index=False)}")

    print("\n" + "-" * 80)
    print("[STEP 7] GROUPING DATA BY WARD")
    print("-" * 80)
    wards = df.groupby("Ward")
    for ward_name, ward_df in wards:
        print(f"\n{ward_name}: {len(ward_df)} patients - {list(ward_df['Patient_ID'])}")

    print("\n" + "-" * 80)
    print("[STEP 8] AVERAGE TURNAROUND TIME BY WARD")
    print("-" * 80)
    avg_turnaround = df.groupby("Ward")["Turnaround_Time"].mean().round(2)
    turnaround_df = pd.DataFrame({
        "Ward": avg_turnaround.index,
        "Average_Turnaround_Time": avg_turnaround.values
    })
    print(f"\n{turnaround_df.to_string(index=False)}")

    print("\n" + "-" * 80)
    print("[STEP 9] WARD-WISE GLUCOSE STATISTICS")
    print("-" * 80)
    glucose_stats = df.groupby("Ward")["Glucose_Reading"].agg(["mean", "min", "max", "count"]).round(2)
    glucose_stats.columns = ["Avg_Glucose", "Min_Glucose", "Max_Glucose", "Patient_Count"]
    print(f"\n{glucose_stats.to_string()}")

    print("\n" + "-" * 80)
    print("[STEP 10] WARD WITH HIGHEST AVERAGE TURNAROUND TIME")
    print("-" * 80)
    max_turnaround_ward = avg_turnaround.idxmax()
    max_turnaround_time = avg_turnaround.max()
    print(f"\nWard Requiring Maximum Average Turnaround: {max_turnaround_ward}")
    print(f"Average Turnaround Time: {max_turnaround_time:.2f} minutes")

    print("\n" + "=" * 80)
    print("[STEP 11] FINAL ANALYSIS SUMMARY")
    print("=" * 80)

    final_summary = pd.DataFrame({
        "Ward": avg_turnaround.index,
        "Patient_Count": df.groupby("Ward").size().values,
        "Avg_Glucose_mg_dL": df.groupby("Ward")["Glucose_Reading"].mean().round(2).values,
        "Min_Glucose_mg_dL": df.groupby("Ward")["Glucose_Reading"].min().values,
        "Max_Glucose_mg_dL": df.groupby("Ward")["Glucose_Reading"].max().values,
        "Avg_Turnaround_min": avg_turnaround.values,
        "High_Glucose_Patients": df[df["Glucose_Reading"] > 140].groupby("Ward").size().reindex(avg_turnaround.index, fill_value=0).values
    })

    print(f"\n{'=' * 80}")
    print("COMPREHENSIVE WARD-WISE ANALYSIS")
    print(f"{'=' * 80}")
    print(f"\n{final_summary.to_string(index=False)}")

    print(f"\n{'=' * 80}")
    print("KEY FINDINGS")
    print(f"{'=' * 80}")

    highest_glucose_ward = final_summary.loc[final_summary["Avg_Glucose_mg_dL"].idxmax()]
    print(f"\n1. Highest Average Glucose Reading:")
    print(f"   Ward: {highest_glucose_ward['Ward']}")
    print(f"   Average: {highest_glucose_ward['Avg_Glucose_mg_dL']:.2f} mg/dL")

    print(f"\n2. Highest Average Turnaround Time:")
    print(f"   Ward: {max_turnaround_ward}")
    print(f"   Time: {max_turnaround_time:.2f} minutes")

    print(f"\n3. Total Patients Analyzed: {len(df)}")
    print(f"   Patients with High Glucose (>140): {len(high_glucose)}")

    print(f"\n4. Wards Requiring Close Clinical Monitoring:")
    flagged = final_summary[(final_summary["Avg_Glucose_mg_dL"] > 140) & (final_summary["Avg_Turnaround_min"] > 50)]
    if len(flagged) > 0:
        for _, row in flagged.iterrows():
            print(f"   - {row['Ward']}: Glucose={row['Avg_Glucose_mg_dL']} mg/dL, Turnaround={row['Avg_Turnaround_min']:.2f} min")
    else:
        print("   No wards meet both criteria for flagging.")

    print(f"\n{'=' * 80}")
    print("ANALYSIS COMPLETE")
    print(f"{'=' * 80}")

if __name__ == "__main__":
    main()
