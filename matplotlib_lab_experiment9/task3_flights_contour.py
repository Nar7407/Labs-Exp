"""Experiment 9 - Task 3: Contour Visualization of Real Seasonal Data.

Pivots the Flights dataset into a Year x Month matrix of passenger counts and
plots it as a filled contour plot with a colorbar, showing the seasonal peak
months and year-over-year growth in real historical data (1949-1960).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"

flights = pd.read_csv(URL)
print(f"Loaded Flights dataset: {flights.shape[0]} rows")

# Pivot: rows = month (calendar order), columns = year, values = passengers
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
plt.savefig("flights_seasonal_contour.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved flights_seasonal_contour.png")

# Quick interpretation helpers
peak_cell = np.unravel_index(np.nanargmax(Z), Z.shape)
print(f"\nPeak traffic: {Z[peak_cell]:.0f} passengers in {month_order[peak_cell[0]]} {pivot.columns[peak_cell[1]]}")
print("Observation: traffic grows year over year and peaks every year in July-August (summer holidays).")
