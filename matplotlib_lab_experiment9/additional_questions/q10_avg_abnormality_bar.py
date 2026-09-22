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

abnormality = np.array([
    [20, 35, 45, 60, 30],
    [25, 40, 55, 65, 35],
    [15, 30, 50, 70, 45],
    [30, 45, 60, 75, 40],
])
ward_names = ["Ward A", "Ward B", "Ward C", "Ward D"]

avg_per_ward = abnormality.mean(axis=1)
for name, avg in zip(ward_names, avg_per_ward):
    print(f"{name}: average abnormality index = {avg:.2f}")

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.bar(ward_names, avg_per_ward, color="teal", edgecolor="black",
              alpha=0.85, label="Average AI")
for bar, avg in zip(bars, avg_per_ward):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.6,
            f"{avg:.1f}", ha="center", va="bottom", fontweight="bold")

ax.set_title("Average Glucose-Abnormality Index per Ward", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Ward")
ax.set_ylabel("Average Abnormality Index")
ax.grid(axis="y", alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "q10_avg_abnormality_bar.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q10_avg_abnormality_bar.png")
