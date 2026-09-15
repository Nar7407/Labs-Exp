import numpy as np

np.random.seed(42)

def task1_matrix_operations():
    print("=" * 60)
    print("TASK 1: Matrix Operations Calculator")
    print("=" * 60)

    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=float)

    B = np.array([[9, 8, 7],
                  [6, 5, 4],
                  [3, 2, 1]], dtype=float)

    print("Matrix A:\n", A)
    print("\nMatrix B:\n", B)

    print("\n--- Element-wise Operations ---")
    print("Addition (A + B):\n", A + B)
    print("Subtraction (A - B):\n", A - B)
    print("Element-wise Multiplication (A * B):\n", A * B)

    print("\n--- Matrix Multiplication (Dot Product) ---")
    print("A @ B:\n", A @ B)
    print("np.dot(A, B):\n", np.dot(A, B))

    print("\n--- Transpose & Determinant of A ---")
    print("Transpose of A:\n", A.T)
    print("Determinant of A:", np.linalg.det(A))

    print()

def task2_boolean_masking():
    print("=" * 60)
    print("TASK 2: Boolean Masking and Conditional Replacement")
    print("=" * 60)

    temps = np.random.randint(15, 46, size=30)
    print("Daily Temperatures (30 days):\n", temps)

    extreme_heat_count = np.sum(temps > 40)
    print(f"\nDays with temperature > 40°C (extreme heat): {extreme_heat_count}")

    temps_flagged = np.where(temps < 20, -1, temps)
    print("Temperatures with values < 20°C replaced by -1:\n", temps_flagged)

    mean_temp = np.mean(temps)
    std_temp = np.std(temps)
    lower, upper = mean_temp - std_temp, mean_temp + std_temp
    within_one_std = temps[(temps >= lower) & (temps <= upper)]
    print(f"\nMean: {mean_temp:.2f}, Std: {std_temp:.2f}")
    print(f"Range within 1 std dev: [{lower:.2f}, {upper:.2f}]")
    print("Temperatures within 1 standard deviation of mean:\n", within_one_std)

    print()

def task3_row_col_statistics():
    print("=" * 60)
    print("TASK 3: Row and Column-wise Statistics on 2-D Array")
    print("=" * 60)

    marks = np.random.randint(0, 101, size=(5, 4))
    print("Marks (5 students x 4 subjects):\n", marks)
    print("Subjects: Sub1, Sub2, Sub3, Sub4")
    print("Students: S0, S1, S2, S3, S4")

    print("\n--- Row-wise (per student) ---")
    student_totals = marks.sum(axis=1)
    student_avgs = marks.mean(axis=1)
    for i in range(5):
        print(f"Student S{i}: Total = {student_totals[i]}, Average = {student_avgs[i]:.2f}")

    print("\n--- Column-wise (per subject) ---")
    subject_avgs = marks.mean(axis=0)
    subject_maxs = marks.max(axis=0)
    for j in range(4):
        print(f"Subject Sub{j}: Average = {subject_avgs[j]:.2f}, Highest = {subject_maxs[j]}")

    topper_idx = np.argmax(student_totals)
    print(f"\nTopper: Student S{topper_idx} with total marks = {student_totals[topper_idx]}")

    print()

def case_study_abnormal_glucose():
    print("=" * 60)
    print("AI CASE STUDY: Abnormal-Glucose Detection")
    print("=" * 60)

    patient_ids = np.array(["H101", "H102", "H103", "H104", "H105"])
    glucose = np.array([110.0, 165.0, 185.5, 95.0, 150.0])
    threshold = 140.0

    print("Glucose Reading Array:\n", glucose)

    abnormal_flag = glucose > threshold
    print("\nAbnormal Flags:\n", abnormal_flag)

    abnormal_patients = patient_ids[abnormal_flag]
    abnormal_glucose = glucose[abnormal_flag]

    print("\nAbnormal-Glucose Patients:")
    for pid in abnormal_patients:
        print(pid)

    print("\nGlucose Readings of Abnormal Samples:\n", abnormal_glucose)

    total_abnormal = np.sum(abnormal_flag)
    total_patients = len(glucose)
    abnormal_percentage = (total_abnormal / total_patients) * 100

    print(f"\nTotal Abnormal Samples : {total_abnormal}")
    print(f"Total Patients : {total_patients}")
    print(f"Abnormal Percentage : {abnormal_percentage:.2f} %")

    print("\n--- Additional Tasks ---")

    fasting_status = np.array([True, False, True, True, False])
    print("Fasting Status of Abnormal Patients:", fasting_status[abnormal_flag])

    max_glucose_idx = np.argmax(glucose)
    print(f"\nPatient with Maximum Glucose: {patient_ids[max_glucose_idx]} ({glucose[max_glucose_idx]} mg/dL)")

    avg_glucose = np.mean(glucose)
    print(f"Average Glucose Reading: {avg_glucose:.2f} mg/dL")

    between_140_180 = glucose[(glucose >= 140) & (glucose <= 180)]
    print("Patients with Glucose 140-180 mg/dL:", patient_ids[(glucose >= 140) & (glucose <= 180)])
    print("Their Readings:", between_140_180)

    urgent_flag = glucose > 180
    urgent_patients = patient_ids[urgent_flag]
    urgent_percentage = (np.sum(urgent_flag) / total_patients) * 100
    print(f"\nUrgent Attention (>180): {urgent_patients}")
    print(f"Urgent Percentage: {urgent_percentage:.2f}%")

    random_glucose = np.random.uniform(80, 200, size=10).round(1)
    random_ids = np.array([f"P{i+1:03d}" for i in range(10)])
    random_flag = random_glucose > threshold
    print(f"\nRandom 10 Patients Glucose: {random_glucose}")
    print(f"Random Abnormal: {random_ids[random_flag]}")

    conditions = [
        glucose <= 140,
        (glucose > 140) & (glucose <= 180),
        glucose > 180
    ]
    choices = ["Normal", "Elevated Glucose", "High Glucose - Urgent"]
    classification = np.select(conditions, choices, default="Unknown")
    print("\nClassification:")
    for pid, g, c in zip(patient_ids, glucose, classification):
        print(f"  {pid}: {g} mg/dL -> {c}")

    print()

def additional_task1_identity_matrix():
    print("=" * 60)
    print("Additional Task 1: 4x4 Identity Matrix")
    print("=" * 60)

    I = np.eye(4)
    print("Identity Matrix (4x4):\n", I)

    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]], dtype=float)

    print("\nMatrix A:\n", A)
    print("I @ A:\n", I @ A)
    print("A @ I:\n", A @ I)
    print("Verification (I @ A == A):", np.allclose(I @ A, A))
    print()

def additional_task2_normalize():
    print("=" * 60)
    print("Additional Task 2: Normalize 1-D Array to [0, 1]")
    print("=" * 60)

    arr = np.array([10, 20, 30, 40, 50], dtype=float)
    print("Original Array:", arr)

    arr_min, arr_max = arr.min(), arr.max()
    normalized = (arr - arr_min) / (arr_max - arr_min)
    print("Normalized Array:", normalized)
    print("Min:", normalized.min(), "Max:", normalized.max())
    print()

def additional_task3_primes():
    print("=" * 60)
    print("Additional Task 3: Find Primes in Array")
    print("=" * 60)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    vec_is_prime = np.vectorize(is_prime)

    arr = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19, 23, 25, 29])
    print("Array:", arr)

    prime_mask = vec_is_prime(arr)
    primes = arr[prime_mask]
    print("Prime Numbers:", primes)
    print()

def additional_task4_stacking():
    print("=" * 60)
    print("Additional Task 4: Stack Arrays Vertically & Horizontally")
    print("=" * 60)

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Array a:", a)
    print("Array b:", b)

    vstacked = np.vstack((a, b))
    print("\nVertical Stack (vstack):\n", vstacked)

    hstacked = np.hstack((a, b))
    print("Horizontal Stack (hstack):", hstacked)
    print()

def additional_task5_cumulative():
    print("=" * 60)
    print("Additional Task 5: Cumulative Sum & Product")
    print("=" * 60)

    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Cumulative Sum:", np.cumsum(arr))
    print("Cumulative Product:", np.cumprod(arr))
    print()

def post_lab_answers():
    print("=" * 60)
    print("POST-LAB CONCEPTUAL QUESTIONS - ANSWERS")
    print("=" * 60)

    answers = {
        1: "Key difference: NumPy ndarray is homogeneous (single dtype), fixed-size, supports vectorized ops, and uses contiguous memory. Python list is heterogeneous, dynamic, stores pointers to objects, and requires loops for element-wise operations.",
        2: "Broadcasting allows NumPy to perform arithmetic on arrays of different shapes. Rule: Dimensions are compatible if they are equal or one of them is 1. Comparison starts from trailing dimensions.",
        3: "arr.sum() = scalar sum of all elements. arr.sum(axis=0) = column-wise sums (reduce rows). arr.sum(axis=1) = row-wise sums (reduce columns).",
        4: "Boolean masking creates a boolean array of same shape. NumPy uses this as an index array to select elements where True. Internally, it creates a new array with only the True-positioned elements (fancy indexing).",
        5: "np.dot() / @ = matrix multiplication (linear algebra): (m×n) @ (n×p) → (m×p). * = element-wise (Hadamard) multiplication: same shape required, multiplies corresponding elements."
    }

    for q, a in answers.items():
        print(f"\nQ{q}: {a}")

    print("\n" + "=" * 60)
    print("APPLICATION-BASED QUESTIONS - ANSWERS")
    print("=" * 60)

    app_answers = {
        1: "np.where() is vectorized (C-level), avoids Python loop overhead, is concise, and handles broadcasting automatically. Loops are slower due to interpreter overhead per iteration.",
        2: "axis=0 reduces rows → computes per-column (per-subject) stats. axis=1 reduces columns → computes per-row (per-student) stats. Real-world: axis=0 gives subject averages across students; axis=1 gives student totals across subjects.",
        3: "Vectorized ops run in compiled C/Fortran code, use contiguous memory (cache-friendly), avoid Python interpreter overhead per element, and leverage SIMD instructions. Loops have per-iteration type checks, bounds checks, and object allocations."
    }

    for q, a in app_answers.items():
        print(f"\nQ{q}: {a}")

    print()

def demo_loop_vs_vectorized():
    print("=" * 60)
    print("DEMO: Loop vs Vectorized Performance")
    print("=" * 60)

    import time

    n = 10_000_000
    arr = np.random.rand(n)

    start = time.perf_counter()
    result_vec = arr * 2 + 1
    vec_time = time.perf_counter() - start

    start = time.perf_counter()
    result_loop = [x * 2 + 1 for x in arr]
    loop_time = time.perf_counter() - start

    print(f"Array size: {n:,}")
    print(f"Vectorized time: {vec_time:.4f}s")
    print(f"Python loop time: {loop_time:.4f}s")
    print(f"Speedup: {loop_time/vec_time:.1f}x")
    print()

if __name__ == "__main__":
    task1_matrix_operations()
    task2_boolean_masking()
    task3_row_col_statistics()
    case_study_abnormal_glucose()
    additional_task1_identity_matrix()
    additional_task2_normalize()
    additional_task3_primes()
    additional_task4_stacking()
    additional_task5_cumulative()
    demo_loop_vs_vectorized()
    post_lab_answers()
    print("All tasks completed successfully!")