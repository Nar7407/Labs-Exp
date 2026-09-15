import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

tips = pd.read_csv(URL)
print(f"Loaded Tips dataset: {tips.shape[0]} rows x {tips.shape[1]} columns")
print(tips.head(), "\n")

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Restaurant Tipping Dashboard (Tips Dataset)", fontsize=16, fontweight="bold")

day_order = ["Thur", "Fri", "Sat", "Sun"]
avg_tip_by_day = tips.groupby("day")["tip"].mean().reindex(day_order)

axes[0, 0].bar(avg_tip_by_day.index, avg_tip_by_day.values,
               color="teal", edgecolor="black", alpha=0.85, label="Average tip")
axes[0, 0].set_title("Average Tip Amount by Day")
axes[0, 0].set_xlabel("Day of the Week")
axes[0, 0].set_ylabel("Average Tip ($)")
axes[0, 0].legend()
for i, v in enumerate(avg_tip_by_day.values):
    axes[0, 0].text(i, v + 0.03, f"{v:.2f}", ha="center", va="bottom", fontsize=9)

meal_counts = tips["time"].value_counts()

axes[0, 1].pie(meal_counts.values, labels=meal_counts.index, autopct="%1.1f%%",
               startangle=90, colors=["#ff9999", "#66b3ff"],
               wedgeprops={"edgecolor": "black"})
axes[0, 1].set_title("Proportion of Bills: Lunch vs Dinner")

axes[1, 0].hist(tips["total_bill"], bins=15, color="orange",
                edgecolor="black", alpha=0.85, label="Bills")
axes[1, 0].axvline(tips["total_bill"].mean(), color="red", linestyle="--",
                   label=f"Mean: ${tips['total_bill'].mean():.2f}")
axes[1, 0].set_title("Distribution of Total Bill")
axes[1, 0].set_xlabel("Total Bill ($)")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].legend()

smoker_tips = tips.loc[tips["smoker"] == "Yes", "tip"]
non_smoker_tips = tips.loc[tips["smoker"] == "No", "tip"]

vp = axes[1, 1].violinplot([non_smoker_tips, smoker_tips], showmeans=True)
axes[1, 1].set_xticks([1, 2], ["Non-Smokers", "Smokers"])
axes[1, 1].set_title("Tip Distribution: Smokers vs Non-Smokers")
axes[1, 1].set_ylabel("Tip ($)")
parts_legend = [plt.Line2D([0], [0], color="steelblue", lw=6, alpha=0.6, label="Distribution"),
                plt.Line2D([0], [0], color="blue", marker="o", lw=0, label="Mean")]
axes[1, 1].legend(handles=parts_legend, loc="upper right")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("tips_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved tips_dashboard.png")
