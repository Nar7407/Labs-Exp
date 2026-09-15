import numpy as np

def task_1_user_input():
    print("=" * 60)
    print("  TASK 1: User-Defined Glucose Readings")
    print("=" * 60)

    n = int(input("Number of Patients: "))
    ids_input = input(f"Enter {n} patient IDs (space-separated): ")
    readings_input = input(f"Enter {n} glucose readings (space-separated): ")

    patient_ids = np.array(ids_input.split())
    glucose = np.array(readings_input.split(), dtype=float)

    threshold = 140
    abnormal_flag = glucose > threshold

    print(f"\nGlucose Array:\n{glucose}")
    print(f"Abnormal Flags:\n{abnormal_flag}")
    print(f"Abnormal Patients: {patient_ids[abnormal_flag]}")
    print(f"Abnormal Readings: {glucose[abnormal_flag]}")

def task_2_fasting_status():
    print("\n" + "=" * 60)
    print("  TASK 2: Fasting Status of Abnormal Patients")
    print("=" * 60)

    glucose = np.array([110.0, 165.0, 185.5, 95.0, 150.0])
    patient_ids = np.array(["H101", "H102", "H103", "H104", "H105"])
    fasting_status = np.array(["Fasting", "Non-Fasting", "Fasting", "Fasting", "Non-Fasting"])

    threshold = 140
    abnormal_flag = glucose > threshold

    abnormal_fasting = fasting_status[abnormal_flag]

    print(f"Fasting Status Array:\n{fasting_status}")
    print(f"\nAbnormal Patients and their Fasting Status:")
    for pid, status in zip(patient_ids[abnormal_flag], abnormal_fasting):
        print(f"  {pid}: {status}")

def task_3_user_threshold():
    print("\n" + "=" * 60)
    print("  TASK 3: User-Defined Threshold")
    print("=" * 60)

    glucose = np.array([110.0, 165.0, 185.5, 95.0, 150.0])
    patient_ids = np.array(["H101", "H102", "H103", "H104", "H105"])

    threshold = float(input("Enter glucose abnormality threshold (mg/dL): "))

    abnormal_flag = glucose > threshold
    num_abnormal = int(np.sum(abnormal_flag))
    pct = (num_abnormal / len(glucose)) * 100

    print(f"\nThreshold: {threshold} mg/dL")
    print(f"Abnormal Flags:\n{abnormal_flag}")
    print(f"Abnormal Patients: {patient_ids[abnormal_flag]}")
    print(f"Abnormal Percentage: {pct:.2f}%")

def task_4_max_and_average():
    print("\n" + "=" * 60)
    print("  TASK 4: Max Glucose & Average")
    print("=" * 60)

    glucose = np.array([110.0, 165.0, 185.5, 95.0, 150.0])
    patient_ids = np.array(["H101", "H102", "H103", "H104", "H105"])

    max_idx = np.argmax(glucose)
    avg = np.mean(glucose)

    print(f"Glucose Array:\n{glucose}")
    print(f"\nPatient with Maximum Glucose: {patient_ids[max_idx]} "
          f"({glucose[max_idx]} mg/dL)")
    print(f"Average Glucose Reading: {avg:.2f} mg/dL")

def task_5_range_and_urgent():
    print("\n" + "=" * 60)
    print("  TASK 5: Range 140–180 & Urgent Attention (>180)")
    print("=" * 60)

    glucose = np.array([110.0, 165.0, 185.5, 95.0, 150.0])
    patient_ids = np.array(["H101", "H102", "H103", "H104", "H105"])

    in_range_flag = (glucose >= 140) & (glucose <= 180)
    print("Patients with glucose 140–180 mg/dL:")
    for pid, g in zip(patient_ids[in_range_flag], glucose[in_range_flag]):
        print(f"  {pid}: {g} mg/dL")

    urgent_flag = glucose > 180
    num_urgent = int(np.sum(urgent_flag))
    urgent_pct = (num_urgent / len(glucose)) * 100

    print("\nPatients requiring URGENT attention (>180 mg/dL):")
    for pid, g in zip(patient_ids[urgent_flag], glucose[urgent_flag]):
        print(f"  {pid}: {g} mg/dL")
    print(f"Urgent Attention Percentage: {urgent_pct:.2f}%")

def task_6_loop_vs_vectorized():
    print("\n" + "=" * 60)
    print("  TASK 6: Loop vs Vectorized Comparison")
    print("=" * 60)

    import time

    N = 1_000_000
    glucose = np.random.uniform(60, 250, size=N)
    threshold = 140.0

    start = time.time()
    loop_result = [g > threshold for g in glucose]
    loop_count = sum(loop_result)
    loop_time = time.time() - start

    start = time.time()
    vec_result = glucose > threshold
    vec_count = int(np.sum(vec_result))
    vec_time = time.time() - start

    print(f"Patients (N): {N}")
    print(f"Threshold: {threshold} mg/dL\n")
    print(f"Python loop — Abnormal: {loop_count}, Time: {loop_time:.4f}s")
    print(f"NumPy vectorized — Abnormal: {vec_count}, Time: {vec_time:.4f}s")
    if vec_time > 0:
        print(f"Speedup: {loop_time / vec_time:.1f}x faster with NumPy")

def task_7_classification():
    print("\n" + "=" * 60)
    print("  TASK 7: Patient Classification")
    print("=" * 60)

    glucose = np.array([110.0, 165.0, 185.5, 95.0, 150.0])
    patient_ids = np.array(["H101", "H102", "H103", "H104", "H105"])

    status = np.where(
        glucose <= 140, "Normal",
        np.where(glucose <= 180, "Elevated Glucose", "High Glucose - Urgent")
    )

    print(f"{'Patient ID':<12s} {'Glucose (mg/dL)':<18s} {'Status'}")
    print("-" * 50)
    for pid, g, s in zip(patient_ids, glucose, status):
        print(f"{pid:<12s} {g:<18.1f} {s}")

if __name__ == "__main__":

    task_2_fasting_status()
    task_4_max_and_average()
    task_5_range_and_urgent()
    task_6_loop_vs_vectorized()
    task_7_classification()
