import matplotlib

from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
LAB9_DIR = next(parent for parent in [SCRIPT_PATH.parent, *SCRIPT_PATH.parents]
                if parent.name == "matplotlib_lab_experiment9")
OUTPUT_DIR = LAB9_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = LAB9_DIR / "datasets"
CSV_PATH = DATA_DIR / "glucose_readings.csv"

df = pd.read_csv(CSV_PATH)
print("Loaded glucose_readings.csv:")
print(df.to_string(index=False), "\n")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["day"], df["glucose"], color="blue", marker="o", linewidth=2,
        label="Glucose Reading")
ax.axhline(140, color="red", linestyle="--", label="Threshold (140 mg/dL)")
ax.set_title("Glucose Trend from CSV Data", fontsize=13, fontweight="bold")
ax.set_xlabel("Monitoring Period (Days)")
ax.set_ylabel("Glucose Reading (mg/dL)")
ax.grid(alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "q6_csv_glucose_trend.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q6_csv_glucose_trend.png")
