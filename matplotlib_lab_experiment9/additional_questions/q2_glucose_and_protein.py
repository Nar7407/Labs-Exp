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

days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])
protein = np.array([12, 18, 25, 32, 40, 45, 38, 28, 20])

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(days, glucose, color="blue", marker="o", linewidth=2,
         label="Glucose (mg/dL)")
ax1.set_xlabel("Monitoring Period (Days)")
ax1.set_ylabel("Glucose Reading (mg/dL)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()
ax2.plot(days, protein, color="purple", marker="s", linestyle="--",
         linewidth=2, label="Protein (mg/dL)")
ax2.set_ylabel("Protein Reading (mg/dL)", color="purple")
ax2.tick_params(axis="y", labelcolor="purple")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

ax1.set_title("Glucose vs Protein Readings Over Monitoring Period",
              fontsize=13, fontweight="bold")
ax1.grid(alpha=0.4)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "q2_glucose_protein.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q2_glucose_protein.png")
