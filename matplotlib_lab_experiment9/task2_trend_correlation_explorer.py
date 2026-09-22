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
FLIGHTS_CSV = DATA_DIR / "flights.csv"
MPG_CSV = DATA_DIR / "mpg.csv"

flights = pd.read_csv(FLIGHTS_CSV)
print(f"Loaded Flights dataset: {flights.shape[0]} rows")
passengers_per_year = flights.groupby("year")["passengers"].sum()
years = passengers_per_year.index
totals = passengers_per_year.values
overall_avg = totals.mean()
deviation = totals - overall_avg

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Airline Passengers Trend (Flights Dataset, 1949-1960)",
             fontsize=15, fontweight="bold")

axes[0].plot(years, totals, color="steelblue", marker="o", linestyle="-",
             linewidth=2, label="Total passengers per year")
axes[0].axhline(overall_avg, color="red", linestyle="--",
                label=f"Overall average: {overall_avg:.0f}")
axes[0].set_title("Yearly Total Passengers")
axes[0].set_ylabel("Passengers")
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].fill_between(years, deviation, 0,
                     where=(deviation >= 0), color="seagreen", alpha=0.6,
                     interpolate=True, label="Above average")
axes[1].fill_between(years, deviation, 0,
                     where=(deviation < 0), color="indianred", alpha=0.6,
                     interpolate=True, label="Below average")
axes[1].axhline(0, color="black", linewidth=0.8)
axes[1].set_title("Deviation from Overall Average")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Deviation (passengers)")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(OUTPUT_DIR / "flights_trend_area.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved flights_trend_area.png")

mpg = pd.read_csv(MPG_CSV)
mpg = mpg.dropna(subset=["horsepower"])
print(f"\nLoaded Auto MPG dataset: {mpg.shape[0]} rows (after dropping missing horsepower)")

fig, ax = plt.subplots(figsize=(10, 6))
sc = ax.scatter(mpg["horsepower"], mpg["mpg"], c=mpg["model_year"],
                cmap="viridis", alpha=0.85, edgecolors="black", linewidth=0.4)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label("Model Year")
ax.set_title("Horsepower vs MPG (Colour = Model Year)")
ax.set_xlabel("Horsepower")
ax.set_ylabel("Miles Per Gallon (MPG)")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "mpg_horsepower_scatter.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved mpg_horsepower_scatter.png")
