import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
electronics = [120, 135, 150, 160, 175, 190]
clothing = [90, 85, 100, 110, 105, 120]
groceries = [200, 210, 195, 220, 230, 240]

fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(months, electronics, clothing, groceries,
             labels=["Electronics", "Clothing", "Groceries"],
             colors=["#66b3ff", "#ff9999", "#99ff99"], alpha=0.85,
             edgecolor="black", linewidth=0.5)

totals = np.array(electronics) + np.array(clothing) + np.array(groceries)
for i, total in enumerate(totals):
    ax.text(i, total + 8, str(total), ha="center", fontweight="bold",
            fontsize=9)

ax.set_title("Monthly Sales by Product Category (Stacked Area)", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (units)")
ax.legend(loc="upper left")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("practice3_stacked_area_sales.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved practice3_stacked_area_sales.png")
