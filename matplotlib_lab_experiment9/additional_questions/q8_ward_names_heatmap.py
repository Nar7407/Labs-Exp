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

fig, ax = plt.subplots(figsize=(9, 6))
heat = ax.imshow(abnormality, cmap="YlOrRd", aspect="auto")
cbar = plt.colorbar(heat, ax=ax)
cbar.set_label("Glucose-Abnormality Index")

ax.set_title("Ward-Wise Glucose Abnormality (Named Wards)", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Ward-Section Column")
ax.set_ylabel("Ward")
ax.set_xticks(range(abnormality.shape[1]))
ax.set_xticklabels([f"Col {c + 1}" for c in range(abnormality.shape[1])])
ax.set_yticks(range(len(ward_names)))
ax.set_yticklabels(ward_names)

for r in range(abnormality.shape[0]):
    for c in range(abnormality.shape[1]):
        value = abnormality[r, c]
        color = "white" if value > abnormality.max() / 1.6 else "black"
        ax.text(c, r, str(value), ha="center", va="center",
                color=color, fontweight="bold")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "q8_ward_names_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q8_ward_names_heatmap.png")
