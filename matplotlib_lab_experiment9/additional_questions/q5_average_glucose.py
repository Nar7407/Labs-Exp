"""Additional Question 5: Calculate and display the average glucose reading.

The average is drawn as a horizontal reference line and also printed.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])

avg_glucose = glucose.mean()
print(f"Average glucose reading over the monitoring period: {avg_glucose:.2f} mg/dL")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(days, glucose, color="blue", marker="o", linewidth=2,
        label="Glucose Reading")
ax.axhline(avg_glucose, color="green", linestyle="--", linewidth=1.5,
           label=f"Average: {avg_glucose:.2f} mg/dL")
ax.set_title("Glucose Trend with Average Reading", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Monitoring Period (Days)")
ax.set_ylabel("Glucose Reading (mg/dL)")
ax.grid(alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig("q5_average_glucose.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q5_average_glucose.png")
