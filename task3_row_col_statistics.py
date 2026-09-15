import numpy as np

def main():
    np.random.seed(42)

    marks = np.random.randint(0, 101, size=(5, 4))

    subjects = ["Math", "Science", "English", "History"]
    students = [f"Student {i + 1}" for i in range(5)]

    print("Marks Matrix (5 students × 4 subjects):")
    header = f"{'':>12s}" + "".join(f"{s:>10s}" for s in subjects)
    print(header)
    for i, name in enumerate(students):
        print(f"{name:>12s}" + "".join(f"{v:>10d}" for v in marks[i]))
    print()

    totals = marks.sum(axis=1)
    averages = marks.mean(axis=1)

    print("--- Row-wise Statistics (per student) ---")
    for i, name in enumerate(students):
        print(f"  {name}: Total = {totals[i]}, Average = {averages[i]:.1f}")
    print()

    col_averages = marks.mean(axis=0)
    col_maxes = marks.max(axis=0)

    print("--- Column-wise Statistics (per subject) ---")
    for j, subj in enumerate(subjects):
        print(f"  {subj}: Average = {col_averages[j]:.1f}, Highest = {col_maxes[j]}")
    print()

    topper_index = np.argmax(totals)
    print(f"--- Topper ---")
    print(f"  {students[topper_index]} with total {totals[topper_index]} "
          f"(index {topper_index})")

if __name__ == "__main__":
    main()
