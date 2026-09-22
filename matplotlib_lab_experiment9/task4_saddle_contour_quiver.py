import matplotlib

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
LAB9_DIR = next(parent for parent in [SCRIPT_PATH.parent, *SCRIPT_PATH.parents]
                if parent.name == "matplotlib_lab_experiment9")
OUTPUT_DIR = LAB9_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

Z = X**2 - Y**2

fig1, ax1 = plt.subplots(figsize=(8, 6.5))
cf = ax1.contourf(X, Y, Z, levels=25, cmap="coolwarm")
cbar = plt.colorbar(cf, ax=ax1)
cbar.set_label("Z = X\u00b2 - Y\u00b2")
ax1.contour(X, Y, Z, levels=10, colors="black", linewidths=0.4)
ax1.set_title("Filled Contour of Saddle Function Z = X\u00b2 - Y\u00b2",
              fontsize=13, fontweight="bold")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "saddle_contour.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved saddle_contour.png")

U = 2 * X
V = -2 * Y

fig2, ax2 = plt.subplots(figsize=(8, 6.5))
ax2.quiver(X, Y, U, V, np.hypot(U, V), cmap="plasma")
cbar2 = plt.colorbar(ax2.collections[0], ax=ax2)
cbar2.set_label("Gradient Magnitude |(2X, -2Y)|")
ax2.set_title("Quiver Plot: Gradient (Steepest Ascent) of Z = X\u00b2 - Y\u00b2",
              fontsize=13, fontweight="bold")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_aspect("equal")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "saddle_gradient_quiver.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved saddle_gradient_quiver.png")

print("\nInterpretation:")
print("- Along X the gradient points outward (Z rises as |X| grows).")
print("- Along Y the gradient points inward toward y=0 (Z falls as |Y| grows).")
print("- The origin is the saddle point: arrows diverge in X but converge in Y.")
