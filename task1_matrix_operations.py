import numpy as np

def get_3x3_matrix(name: str) -> np.ndarray:
    print(f"\nEnter 3x3 matrix {name} (row by row, 3 numbers per row):")
    rows = []
    for i in range(3):
        while True:
            try:
                row = list(map(float, input(f"  Row {i + 1}: ").split()))
                if len(row) != 3:
                    print("  Please enter exactly 3 numbers.")
                    continue
                rows.append(row)
                break
            except ValueError:
                print("  Invalid input. Enter numbers separated by spaces.")
    return np.array(rows)

def main():

    A = get_3x3_matrix("A")
    B = get_3x3_matrix("B")

    print("\n" + "=" * 50)
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    addition = A + B
    print("\n--- Matrix Addition (A + B) ---")
    print(addition)

    subtraction = A - B
    print("\n--- Matrix Subtraction (A - B) ---")
    print(subtraction)

    elem_mult = A * B
    print("\n--- Element-wise Multiplication (A * B) ---")
    print(elem_mult)

    dot_mult = A @ B
    print("\n--- Matrix Multiplication (A @ B / np.dot) ---")
    print(dot_mult)

    transpose_A = A.T
    print("\n--- Transpose of A (A^T) ---")
    print(transpose_A)

    det_A = np.linalg.det(A)
    print(f"\n--- Determinant of A: {det_A:.4f} ---")

if __name__ == "__main__":
    main()
