"""Additional Question 13: Generate the visualization for multiple patients
and compare their glucose trends in a single figure.

Each patient's trend is plotted with its own colour/marker; per-patient
summary statistics (average, max, days above threshold) are printed and the
averages are compared in a companion bar chart.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

THRESHOLD = 140
days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])

patients = {
    "Patient 1": [110, 125, 138, 152, 168, 180, 160, 145, 130],
    "Patient 2": [105, 118, 132, 141, 150, 158, 149, 138, 125],
    "Patient 3": [115, 130, 150, 165, 185, 190, 172, 158, 140],
}

styles = [
    {"color": "blue", "marker": "o"},
    {"color": "green", "marker": "s"},
    {"color": "purple", "marker": "^"},
]

# ------------------------------------------------ comparison line chart -----
fig1, ax1 = plt.subplots(figsize=(10, 6))
for (name, readings), style in zip(patients.items(), styles):
    values = np.array(readings)
    ax1.plot(days, values, linewidth=2, label=name, **style)
    print(f"{name}: average = {values.mean():.2f} mg/dL, "
          f"max = {values.max()} mg/dL (Day {days[np.argmax(values)]}), "
          f"days above {THRESHOLD} = {int((values > THRESHOLD).sum())}")

ax1.axhline(THRESHOLD, color="red", linestyle="--",
            label=f"Threshold ({THRESHOLD} mg/dL)")
ax1.set_title("Glucose Trend Comparison Across Patients", fontsize=13,
              fontweight="bold")
ax1.set_xlabel("Monitoring Period (Days)")
ax1.set_ylabel("Glucose Reading (mg/dL)")
ax1.grid(alpha=0.4)
ax1.legend()

plt.tight_layout()
plt.savefig("q13_multi_patient_comparison.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q13_multi_patient_comparison.png")

# --------------------------------------------- average-glucose bar chart ----
names = list(patients.keys())
averages = [np.array(v).mean() for v in patients.values()]

fig2, ax2 = plt.subplots(figsize=(8, 5))
bars = ax2.bar(names, averages, color=[s["color"] for s in styles],
               edgecolor="black", alpha=0.8, label="Average glucose")
for bar, avg in zip(bars, averages):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
             f"{avg:.1f}", ha="center", va="bottom", fontweight="bold")
ax2.axhline(THRESHOLD, color="red", linestyle="--",
            label=f"Threshold ({THRESHOLD} mg/dL)")
ax2.set_title("Average Glucose per Patient", fontsize=13, fontweight="bold")
ax2.set_ylabel("Average Glucose (mg/dL)")
ax2.legend()

plt.tight_layout()
plt.savefig("q13_avg_glucose_per_patient.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q13_avg_glucose_per_patient.png")
