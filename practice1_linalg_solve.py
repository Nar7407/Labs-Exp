import numpy as np
from scipy import linalg

ALPHA = 0.05


def banner(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def main():
    banner("PRACTICE 1 : Linear Algebra with scipy.linalg")

    A = np.array([[3.0, 2.0, -1.0],
                  [2.0, -2.0, 4.0],
                  [-1.0, 0.5, -1.0]])
    b = np.array([8.0, 11.0, -3.0])

    print("System of equations:")
    for row, rhs in zip(A, b):
        print("   " + "  ".join(f"{v:5.1f}" for v in row) + f"  =  {rhs:6.1f}")
    print("\nAs matrix form : A x = b")
    print("A =\n", A)
    print("b =", b)

    print("\n--- Basic quantities ---")
    print("-" * 72)
    d = linalg.det(A)
    print(f"Determinant        : {d:.6f}")
    print(f"Inverse            :\n{np.array2string(linalg.inv(A), precision=6)}")
    cond = linalg.norm(A, 2) * linalg.norm(linalg.inv(A), 2)
    print(f"Condition number   : {cond:.6f}   "
          f"({'well conditioned' if cond < 100 else 'ill conditioned - solution is unreliable'})")
    print(f"Matrix rank        : {np.linalg.matrix_rank(A)} of {A.shape[0]}")

    print("\n--- Solution ---")
    print("-" * 72)
    x = linalg.solve(A, b)
    print(f"linalg.solve(A, b) = {x}")
    print(f"  x1 = {x[0]:.6f},  x2 = {x[1]:.6f},  x3 = {x[2]:.6f}")

    print("\nVerification by substitution A x = b:")
    ok = True
    for i, (row, rhs) in enumerate(zip(A, b), start=1):
        lhs = row @ x
        print(f"  eq{i}: {lhs:12.6f}  vs  b{i} = {rhs:6.1f}   "
              f"residual = {lhs - rhs:+.2e}")
        ok &= np.isclose(lhs, rhs, atol=1e-10)
    print(f"\nResidual vector A x - b = {A @ x - b}")
    print(f"Verification : {'PASSED - the solution satisfies every equation' if ok else 'FAILED'}")

    x_lu = linalg.solve(A, b, assume_a="gen")
    print(f"Cross-check with assume_a='gen' : {x_lu}")
    print(f"Max difference between solvers  : {np.max(np.abs(x - x_lu)):.2e}")

    print("\n--- Other decompositions ---")
    print("-" * 72)
    lu, piv = linalg.lu_factor(A)
    print(f"LU solve (lu_solve on lu_factor) : {linalg.lu_solve((lu, piv), b)}")
    print(f"QR-based least-squares             : {linalg.lstsq(A, b)[0]}")
    u, s, vt = linalg.svd(A)
    print(f"Singular values                   : {s}")
    print(f"  product of singular values = {np.prod(s):.6f} = |det(A)| "
          f"({d:.6f}) - the magnitudes match")
    evals = linalg.eigvals(A)
    print(f"Eigenvalues                       : {evals}")
    print(f"Solution vector norm ||x||        : {linalg.norm(x):.6f}")

    print("\nLesson : det(A) != 0 only tells you a unique solution exists. cond(A) tells you how trustworthy the computed digits are. Use both.")


if __name__ == "__main__":
    main()
