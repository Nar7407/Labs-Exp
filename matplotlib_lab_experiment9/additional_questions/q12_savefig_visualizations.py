"""Additional Question 12: Save the generated visualizations as image files
using plt.savefig().

Demonstrates saving both a line chart and a heat map at different dpi values,
in both PNG and PDF formats, before showing them.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])
abnormality = np.array([
    [20, 35, 45, 60, 30],
    [25, 40, 55, 65, 35],
    [15, 30, 50, 70, 45],
    [30, 45, 60, 75, 40],
])

# ---------------------- Visualization 1: line chart -> PNG, PDF and SVG -----
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(days, glucose, color="blue", marker="o", linewidth=2,
         label="Glucose Reading")
ax1.axhline(140, color="red", linestyle="--", label="Threshold (140 mg/dL)")
ax1.set_title("Glucose Trend")
ax1.set_xlabel("Monitoring Period (Days)")
ax1.set_ylabel("Glucose Reading (mg/dL)")
ax1.grid(alpha=0.4)
ax1.legend()

plt.savefig("q12_glucose_trend_150dpi.png", dpi=150, bbox_inches="tight")
plt.savefig("q12_glucose_trend.pdf", bbox_inches="tight")   # vector format
plt.savefig("q12_glucose_trend.svg", bbox_inches="tight")   # vector format
plt.close(fig1)
print("Saved q12_glucose_trend_150dpi.png, q12_glucose_trend.pdf, q12_glucose_trend.svg")

# ---------------------- Visualization 2: heat map -> PNG at 300 dpi ---------
fig2, ax2 = plt.subplots(figsize=(9, 6))
heat = ax2.imshow(abnormality, cmap="YlOrRd", aspect="auto")
plt.colorbar(heat, ax=ax2, label="Glucose-Abnormality Index")
ax2.set_title("Ward-Wise Glucose-Abnormality Heat Map")
ax2.set_xlabel("Ward-Section Column")
ax2.set_ylabel("Ward-Section Row")
plt.savefig("q12_heatmap_300dpi.png", dpi=300, bbox_inches="tight")
plt.close(fig2)
print("Saved q12_heatmap_300dpi.png")

print("\nNote: call plt.savefig() BEFORE plt.show(); after show() the figure "
      "is cleared and the saved file would be blank.")
