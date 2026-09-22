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

THRESHOLD = 140
days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])
abnormality = np.array([
    [20, 35, 45, 60, 30],
    [25, 40, 55, 65, 35],
    [15, 30, 50, 70, 45],
    [30, 45, 60, 75, 40],
])

fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))
fig.suptitle("Patient Monitoring Dashboard", fontsize=15, fontweight="bold")

axes[0].plot(days, glucose, color="blue", marker="o", linewidth=2,
             label="Glucose Reading")
axes[0].axhline(THRESHOLD, color="red", linestyle="--",
                label=f"Threshold ({THRESHOLD} mg/dL)")
axes[0].fill_between(days, glucose, THRESHOLD, where=(glucose > THRESHOLD),
                     color="red", alpha=0.25, interpolate=True)
max_idx = np.argmax(glucose)
axes[0].annotate(f"Max: {glucose[max_idx]} mg/dL (Day {days[max_idx]})",
                 xy=(days[max_idx], glucose[max_idx]),
                 xytext=(days[max_idx] - 9, glucose[max_idx] + 6),
                 arrowprops=dict(facecolor="darkgreen", arrowstyle="->"),
                 color="darkgreen", fontweight="bold")
axes[0].set_title("Glucose Trend")
axes[0].set_xlabel("Monitoring Period (Days)")
axes[0].set_ylabel("Glucose Reading (mg/dL)")
axes[0].grid(alpha=0.4)
axes[0].legend(loc="lower right")

heat = axes[1].imshow(abnormality, cmap="YlOrRd", aspect="auto")
cbar = plt.colorbar(heat, ax=axes[1])
cbar.set_label("Glucose-Abnormality Index")
axes[1].set_title("Ward-Wise Abnormality Heat Map")
axes[1].set_xlabel("Ward-Section Column")
axes[1].set_ylabel("Ward-Section Row")
axes[1].set_xticks(range(abnormality.shape[1]))
axes[1].set_yticks(range(abnormality.shape[0]))
for r in range(abnormality.shape[0]):
    for c in range(abnormality.shape[1]):
        value = abnormality[r, c]
        color = "white" if value > abnormality.max() / 1.6 else "black"
        axes[1].text(c, r, str(value), ha="center", va="center",
                     color=color, fontweight="bold")

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig(OUTPUT_DIR / "q11_dashboard_subplot.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q11_dashboard_subplot.png")
