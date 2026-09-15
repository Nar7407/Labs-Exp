"""Additional Question 4: Annotate all glucose readings above 140 mg/dL.

Every abnormal point (glucose > 140 mg/dL) is marked and annotated with its
day and exact value on the trend graph.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

THRESHOLD = 140
days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(days, glucose, color="blue", marker="o", linewidth=2,
        label="Glucose Reading")
ax.axhline(THRESHOLD, color="red", linestyle="--",
           label=f"Threshold ({THRESHOLD} mg/dL)")

# Annotate every reading above the threshold
for day, value in zip(days, glucose):
    if value > THRESHOLD:
        ax.annotate(f"{value} mg/dL (Day {day})",
                    xy=(day, value),
                    xytext=(day - 1, value + 10),
                    arrowprops=dict(facecolor="red", arrowstyle="->"),
                    fontsize=9, color="red", fontweight="bold")

ax.set_title("Glucose Readings Above 140 mg/dL (Annotated)", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Monitoring Period (Days)")
ax.set_ylabel("Glucose Reading (mg/dL)")
ax.set_ylim(min(glucose) - 20, max(glucose) + 35)  # room for annotations
ax.grid(alpha=0.4)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig("q4_abnormal_annotations.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q4_abnormal_annotations.png")
