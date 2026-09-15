import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

cities = ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mumbai", "Cairo"]
population_millions = [37.4, 32.9, 29.2, 22.6, 21.3, 21.8]

order = np.argsort(population_millions)
cities_sorted = [cities[i] for i in order]
pop_sorted = [population_millions[i] for i in order]

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.barh(cities_sorted, pop_sorted, color="mediumseagreen",
               edgecolor="black", alpha=0.85, label="Population (millions)")
for bar, pop in zip(bars, pop_sorted):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
            f"{pop:.1f}M", va="center", fontweight="bold", fontsize=9)

ax.set_title("Population Comparison of Six Major Cities", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Population (Millions)")
ax.set_ylabel("City")
ax.set_xlim(0, max(pop_sorted) + 4)
ax.grid(axis="x", alpha=0.4)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig("practice2_city_population_barh.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved practice2_city_population_barh.png")
