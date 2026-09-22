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
import pandas as pd

DATA_DIR = LAB9_DIR / "datasets"
FLIGHTS_CSV = DATA_DIR / "flights.csv"

flights = pd.read_csv(FLIGHTS_CSV)
print(f"Loaded Flights dataset: {flights.shape[0]} rows")

month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
pivot = flights.pivot(index="month", columns="year", values="passengers")
pivot = pivot.reindex(month_order)
print("\nYear x Month matrix of passengers (first 5 rows):")
print(pivot.iloc[:, :5].head())

X, Y = np.meshgrid(pivot.columns.values, np.arange(len(month_order)))
Z = pivot.values

fig, ax = plt.subplots(figsize=(11, 7))
cf = ax.contourf(X, Y, Z, levels=15, cmap="viridis")
cbar = plt.colorbar(cf, ax=ax)
cbar.set_label("Passengers")

ax.set_title("Seasonal Contour: Airline Passengers by Year and Month (1949-1960)",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Month")
ax.set_yticks(np.arange(len(month_order)))
ax.set_yticklabels(month_order)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "flights_seasonal_contour.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved flights_seasonal_contour.png")

peak_cell = np.unravel_index(np.nanargmax(Z), Z.shape)
print(f"\nPeak traffic: {Z[peak_cell]:.0f} passengers in {month_order[peak_cell[0]]} {pivot.columns[peak_cell[1]]}")
print("Observation: traffic grows year over year and peaks every year in July-August (summer holidays).")
