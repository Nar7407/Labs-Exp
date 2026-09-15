import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "glucose_readings.csv")

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
plt.savefig("q6_csv_glucose_trend.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q6_csv_glucose_trend.png")
