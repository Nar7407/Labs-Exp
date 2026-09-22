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

fig, ax = plt.subplots(figsize=(10, 6))

normal_days = np.where(glucose <= THRESHOLD, days, np.nan)
abnormal_days = np.where(glucose > THRESHOLD, days, np.nan)
normal_values = np.where(glucose <= THRESHOLD, glucose, np.nan)
abnormal_values = np.where(glucose > THRESHOLD, glucose, np.nan)

ax.plot(normal_days, normal_values, color="green", marker="o",
        linestyle="-", linewidth=2, label=f"Normal (\u2264 {THRESHOLD} mg/dL)")
ax.plot(abnormal_days, abnormal_values, color="red", marker="s",
        linestyle="--", linewidth=2, label=f"Abnormal (> {THRESHOLD} mg/dL)")
ax.axhline(THRESHOLD, color="black", linestyle=":", linewidth=1.5,
           label="Threshold (140 mg/dL)")
ax.fill_between(days, glucose, THRESHOLD, where=(glucose > THRESHOLD),
                color="red", alpha=0.15, interpolate=True)

ax.set_title("Glucose Trend: Normal vs Abnormal Regions", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Monitoring Period (Days)")
ax.set_ylabel("Glucose Reading (mg/dL)")
ax.grid(alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "q3_line_styles.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q3_line_styles.png")
