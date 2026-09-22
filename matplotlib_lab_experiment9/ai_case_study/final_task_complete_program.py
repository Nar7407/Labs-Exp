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

def classify(ai):
    if ai < 30:
        return "Low Abnormality"
    if ai < 50:
        return "Moderate Abnormality"
    if ai < 70:
        return "High Abnormality"
    return "Severe Abnormality"

def plot_glucose_trend(days, glucose):
    max_idx = np.argmax(glucose)
    max_value, max_day = glucose[max_idx], days[max_idx]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(days, glucose, color="blue", marker="o", linewidth=2,
            linestyle="-", label="Glucose Reading")
    ax.axhline(THRESHOLD, color="red", linestyle="--", linewidth=1.5,
               label=f"Abnormality Threshold ({THRESHOLD} mg/dL)")
    ax.fill_between(days, glucose, THRESHOLD, where=(glucose > THRESHOLD),
                    color="red", alpha=0.25, interpolate=True,
                    label="Abnormal-glucose period")
    ax.annotate(f"Max: {max_value} mg/dL (Day {max_day})",
                xy=(max_day, max_value), xytext=(max_day - 8, max_value + 8),
                arrowprops=dict(facecolor="darkgreen", arrowstyle="->"),
                fontsize=10, fontweight="bold", color="darkgreen")

    ax.set_title("Glucose Trend Graph of Sample Patient", fontsize=13,
                 fontweight="bold")
    ax.set_xlabel("Monitoring Period (Days)")
    ax.set_ylabel("Glucose Reading (mg/dL)")
    ax.grid(alpha=0.4)
    ax.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "glucose_trend.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close(fig)
    print("Saved glucose_trend.png")

    print(f"\nMaximum glucose reading : {max_value} mg/dL")
    print(f"Day of maximum reading  : Day {max_day}")
    abnormal_days = days[glucose > THRESHOLD]
    print(f"Abnormal days (> {THRESHOLD} mg/dL): {list(abnormal_days)}")

def plot_ward_heatmap(abnormality):
    rows, cols = abnormality.shape

    fig, ax = plt.subplots(figsize=(9, 6))
    heat = ax.imshow(abnormality, cmap="YlOrRd", aspect="auto")
    cbar = plt.colorbar(heat, ax=ax)
    cbar.set_label("Glucose-Abnormality Index")

    ax.set_title("Ward-Wise Glucose-Abnormality Heat Map", fontsize=13,
                 fontweight="bold")
    ax.set_xlabel("Ward-Section Column")
    ax.set_ylabel("Ward-Section Row")
    ax.set_xticks(range(cols))
    ax.set_xticklabels([f"Col {c + 1}" for c in range(cols)])
    ax.set_yticks(range(rows))
    ax.set_yticklabels([f"Row {r + 1}" for r in range(rows)])

    for r in range(rows):
        for c in range(cols):
            value = abnormality[r, c]
            color = "white" if value > abnormality.max() / 1.6 else "black"
            ax.text(c, r, str(value), ha="center", va="center",
                    color=color, fontweight="bold")

    max_pos = np.unravel_index(np.argmax(abnormality), abnormality.shape)
    max_val = abnormality[max_pos]

    print("\n" + "=" * 50)
    print("MOST ABNORMAL WARD SECTION")
    print("=" * 50)
    print(f"Maximum Abnormality : {max_val}")
    print(f"Ward Section        : Row {max_pos[0] + 1}, Column {max_pos[1] + 1}")
    print(f"Status              : {classify(max_val)}")
    print("=" * 50)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "ward_abnormality_heatmap.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close(fig)
    print("Saved ward_abnormality_heatmap.png")

def main():

    days = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24])
    glucose = np.array([110, 125, 138, 152, 168, 180, 160, 145, 130])
    plot_glucose_trend(days, glucose)

    abnormality = np.array([
        [20, 35, 45, 60, 30],
        [25, 40, 55, 65, 35],
        [15, 30, 50, 70, 45],
        [30, 45, 60, 75, 40],
    ])
    plot_ward_heatmap(abnormality)

if __name__ == "__main__":
    main()
