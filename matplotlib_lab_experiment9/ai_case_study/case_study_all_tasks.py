import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])
THRESHOLD = 140

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(days, glucose, color="blue", marker="o", linestyle="-",
         linewidth=2, label="Glucose Reading")

ax1.axhline(THRESHOLD, color="red", linestyle="--", linewidth=1.5,
            label=f"Abnormality Threshold ({THRESHOLD} mg/dL)")
ax1.fill_between(days, glucose, THRESHOLD, where=(glucose > THRESHOLD),
                 color="red", alpha=0.25, interpolate=True,
                 label="Abnormal-glucose period (> 140 mg/dL)")

max_idx = np.argmax(glucose)
max_value = glucose[max_idx]
max_day = days[max_idx]
ax1.annotate(f"Max: {max_value} mg/dL\n(Day {max_day})",
             xy=(max_day, max_value), xytext=(max_day + 2, max_value + 12),
             arrowprops=dict(facecolor="darkgreen", arrowstyle="->"),
             fontsize=10, fontweight="bold", color="darkgreen")

ax1.set_title("Patient Glucose Trend Across Monitoring Period", fontsize=13,
              fontweight="bold")
ax1.set_xlabel("Monitoring Period (Days)")
ax1.set_ylabel("Glucose Reading (mg/dL)")
ax1.grid(alpha=0.4)
ax1.legend(loc="lower right")

plt.tight_layout()
plt.savefig("glucose_trend.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved glucose_trend.png")
print(f"Maximum glucose reading : {max_value} mg/dL")
print(f"Day of maximum reading  : Day {max_day}")

abnormality = np.array([
    [20, 35, 45, 60, 30],
    [25, 40, 55, 65, 35],
    [15, 30, 50, 70, 45],
    [30, 45, 60, 75, 40],
])

fig2, ax2 = plt.subplots(figsize=(9, 6))
heat = ax2.imshow(abnormality, cmap="YlOrRd", aspect="auto")
cbar = plt.colorbar(heat, ax=ax2)
cbar.set_label("Glucose-Abnormality Index")

ax2.set_title("Ward-Wise Glucose-Abnormality Heat Map", fontsize=13,
              fontweight="bold")
ax2.set_xlabel("Ward-Section Column")
ax2.set_ylabel("Ward-Section Row")
ax2.set_xticks(np.arange(abnormality.shape[1]))
ax2.set_yticks(np.arange(abnormality.shape[0]))
ax2.set_xticklabels([f"Col {c + 1}" for c in range(abnormality.shape[1])])
ax2.set_yticklabels([f"Row {r + 1}" for r in range(abnormality.shape[0])])

for r in range(abnormality.shape[0]):
    for c in range(abnormality.shape[1]):
        value = abnormality[r, c]
        text_color = "white" if value > abnormality.max() / 1.6 else "black"
        ax2.text(c, r, str(value), ha="center", va="center",
                 color=text_color, fontweight="bold")

def classify(ai):
    if ai < 30:
        return "Low Abnormality"
    if ai < 50:
        return "Moderate Abnormality"
    if ai < 70:
        return "High Abnormality"
    return "Severe Abnormality"

max_pos = np.unravel_index(np.argmax(abnormality), abnormality.shape)
max_abnormality = abnormality[max_pos]

print("\n" + "=" * 50)
print("MOST ABNORMAL WARD SECTION")
print("=" * 50)
print(f"Maximum Abnormality : {max_abnormality}")
print(f"Ward Section        : Row {max_pos[0] + 1}, Column {max_pos[1] + 1}")
print(f"Status              : {classify(max_abnormality)}")
print("=" * 50)

plt.tight_layout()
plt.savefig("ward_abnormality_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved ward_abnormality_heatmap.png")
