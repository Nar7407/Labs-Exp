import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [18, 20, 25, 30, 34, 33, 31, 30, 29, 26, 21, 18]
rainfall = [12, 9, 11, 20, 55, 180, 240, 210, 150, 60, 15, 10]
umbrella_sales = [50, 40, 45, 70, 150, 400, 520, 480, 350, 160, 55, 45]

x = np.arange(len(months))

fig, axes = plt.subplots(3, 1, figsize=(10, 11), sharex=True)
fig.suptitle("City Weather vs Umbrella Sales (Shared X-Axis)", fontsize=15,
             fontweight="bold")

axes[0].plot(x, temperature, color="crimson", marker="o", linewidth=2,
             label="Temperature")
axes[0].set_ylabel("Temperature (\u00b0C)")
axes[0].set_title("Monthly Temperature")
axes[0].grid(alpha=0.3)
axes[0].legend(loc="upper right")

axes[1].bar(x, rainfall, color="steelblue", alpha=0.85, edgecolor="black",
            label="Rainfall")
axes[1].set_ylabel("Rainfall (mm)")
axes[1].set_title("Monthly Rainfall")
axes[1].grid(axis="y", alpha=0.3)
axes[1].legend(loc="upper left")

axes[2].scatter(x, umbrella_sales, color="purple", s=70, marker="^",
                edgecolor="black", label="Umbrella sales")
axes[2].set_ylabel("Umbrellas Sold")
axes[2].set_title("Monthly Umbrella Sales")
axes[2].set_xlabel("Month")
axes[2].grid(alpha=0.3)
axes[2].legend(loc="upper left")

axes[2].set_xticks(x)
axes[2].set_xticklabels(months)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("practice5_shared_x_subplots.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved practice5_shared_x_subplots.png")
