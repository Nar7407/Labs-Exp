"""Experiment: 3x3 matrix operations using NumPy (add, subtract, multiply,
transpose, determinant)."""

import numpy as np


def get_3x3_matrix(name: str) -> np.ndarray:
    """Prompt the user until a valid 3x3 matrix is entered."""
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
    # Read the two input matrices
    A = get_3x3_matrix("A")
    B = get_3x3_matrix("B")

    print("\n" + "=" * 50)
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

 
    # Element-wise operations
    addition = A + B
    print("\n--- Matrix Addition (A + B) ---")
    print(addition)

    subtraction = A - B
    print("\n--- Matrix Subtraction (A - B) ---")
    print(subtraction)

    
    elem_mult = A * B  # element-wise product, NOT the matrix product
    print("\n--- Element-wise Multiplication (A * B) ---")
    print(elem_mult)

    # True matrix (dot) product
    dot_mult = A @ B  
    print("\n--- Matrix Multiplication (A @ B / np.dot) ---")
    print(dot_mult)

    
    # Transpose and determinant
    transpose_A = A.T
    print("\n--- Transpose of A (A^T) ---")
    print(transpose_A)

    det_A = np.linalg.det(A)
    print(f"\n--- Determinant of A: {det_A:.4f} ---")


if __name__ == "__main__":
    main()
