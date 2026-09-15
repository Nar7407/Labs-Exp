import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ai_case_study", "patient_tests.csv"))

print("=" * 60)
print("Q4: NUMBER OF PATIENTS PER WARD (using groupby)")
print("=" * 60)

patients_per_ward = df.groupby("Ward").size()
print("\nMethod 1 - groupby('Ward').size():")
print(patients_per_ward)

patients_per_ward_count = df.groupby("Ward")["Patient_ID"].count()
print("\nMethod 2 - groupby('Ward')['Patient_ID'].count():")
print(patients_per_ward_count)

patients_per_ward_vc = df["Ward"].value_counts()
print("\nMethod 3 - value_counts():")
print(patients_per_ward_vc)

patients_summary = df.groupby("Ward").agg(
    Patient_Count=("Patient_ID", "count"),
    Patient_List=("Patient_ID", lambda x: list(x))
)
print("\nMethod 4 - Detailed breakdown:")
print(patients_summary)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"\nTotal Wards: {len(patients_per_ward)}")
print(f"Total Patients: {len(df)}")
print(f"Ward with most patients: {patients_per_ward.idxmax()} ({patients_per_ward.max()} patients)")
print(f"Ward with fewest patients: {patients_per_ward.idxmin()} ({patients_per_ward.min()} patients)")
