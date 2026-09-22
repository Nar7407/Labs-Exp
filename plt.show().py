import os
import matplotlib.pyplot as plt
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load dataset (local CSV first, URL fallback)
tips_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tips.csv')
if os.path.exists(tips_path):
    tips = pd.read_csv(tips_path)
else:
    tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Create 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Multi-Panel Restaurant Tipping Dashboard', fontsize=16)

# 1. Bar Chart: Average tip by day
avg_tip = tips.groupby('day')['tip'].mean()
axes[0, 0].bar(avg_tip.index, avg_tip.values, color='teal')
axes[0, 0].set_title('Average Tip Amount by Day')
axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Average Tip ($)')

# 2. Pie Chart: Bills served at Lunch vs. Dinner
time_counts = tips['time'].value_counts()
axes[0, 1].pie(time_counts.values, labels=time_counts.index, autopct='%1.1f%%', startangle=90, colors=['coral', 'skyblue'])
axes[0, 1].set_title('Proportion of Bills: Lunch vs. Dinner')

# 3. Histogram: Total bill distribution
axes[1, 0].hist(tips['total_bill'], bins=12, color='orange', edgecolor='black')
axes[1, 0].set_title('Total Bill Distribution')
axes[1, 0].set_xlabel('Total Bill ($)')
axes[1, 0].set_ylabel('Frequency')

# 4. Violin Plot: Tip distribution between smokers and non-smokers
smokers = tips[tips['smoker'] == 'Yes']['tip']
non_smokers = tips[tips['smoker'] == 'No']['tip']
axes[1, 1].violinplot([smokers, non_smokers], showmeans=True)
axes[1, 1].set_xticks([1, 2])
axes[1, 1].set_xticklabels(['Smoker', 'Non-Smoker'])
axes[1, 1].set_title('Tip Distribution: Smokers vs Non-Smokers')
axes[1, 1].set_ylabel('Tip Amount ($)')

plt.tight_layout()
    plt.savefig("plt_show_tips_dashboard.png", dpi=150, bbox_inches="tight")
    plt.show()