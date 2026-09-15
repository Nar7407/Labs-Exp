"""Practice Task 6: A 2x2 subplot dashboard for a class of 30 students' marks
across 4 subjects, containing:
  - A bar chart of the class average per subject.
  - A pie chart of the proportion of students scoring Distinction /
    First Class / Pass / Fail (cutoffs defined below).
  - A histogram of the overall marks distribution across all subjects.
  - A violin plot comparing the marks distribution of two subjects.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(7)

subjects = ["Maths", "Physics", "Python", "DBMS"]
# 30 students x 4 subjects of marks between 35 and 98
marks = {
    "Maths": np.random.randint(35, 99, 30),
    "Physics": np.random.randint(35, 99, 30),
    "Python": np.random.randint(35, 99, 30),
    "DBMS": np.random.randint(35, 99, 30),
}

# Grade cutoffs: Distinction >= 75, First Class 60-74, Pass 40-59, Fail < 40
def grade(score):
    if score >= 75:
        return "Distinction"
    if score >= 60:
        return "First Class"
    if score >= 40:
        return "Pass"
    return "Fail"

all_marks = np.concatenate(list(marks.values()))
grades = np.array([grade(s) for s in all_marks])
grade_names = ["Distinction", "First Class", "Pass", "Fail"]
grade_counts = [int((grades == g).sum()) for g in grade_names]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Class of 30 Students - Marks Dashboard (4 Subjects)",
             fontsize=15, fontweight="bold")

# (1) Bar chart: class average per subject
averages = [marks[s].mean() for s in subjects]
bars = axes[0, 0].bar(subjects, averages, color="teal", edgecolor="black",
                      alpha=0.85, label="Class average")
for bar, avg in zip(bars, averages):
    axes[0, 0].text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.5, f"{avg:.1f}",
                    ha="center", fontweight="bold", fontsize=9)
axes[0, 0].set_title("Class Average per Subject")
axes[0, 0].set_xlabel("Subject")
axes[0, 0].set_ylabel("Average Marks")
axes[0, 0].set_ylim(0, 100)
axes[0, 0].grid(axis="y", alpha=0.3)
axes[0, 0].legend()

# (2) Pie chart: grade proportions
axes[0, 1].pie(grade_counts, labels=grade_names, autopct="%1.1f%%",
               startangle=90, colors=["#2e7d32", "#66bb6a", "#ffb74d", "#e57373"],
               wedgeprops={"edgecolor": "black"})
axes[0, 1].set_title("Grade Distribution (all subjects combined)")

# (3) Histogram: overall marks distribution
axes[1, 0].hist(all_marks, bins=10, color="orange", edgecolor="black",
                alpha=0.85, label="All subject marks")
axes[1, 0].axvline(all_marks.mean(), color="red", linestyle="--",
                   label=f"Mean: {all_marks.mean():.1f}")
axes[1, 0].set_title("Overall Marks Distribution")
axes[1, 0].set_xlabel("Marks")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].legend()
axes[1, 0].grid(axis="y", alpha=0.3)

# (4) Violin plot: Maths vs Python marks side by side
vp = axes[1, 1].violinplot([marks["Maths"], marks["Python"]], showmeans=True)
axes[1, 1].set_xticks([1, 2], ["Maths", "Python"])
axes[1, 1].set_title("Marks Distribution: Maths vs Python")
axes[1, 1].set_ylabel("Marks")
axes[1, 1].grid(axis="y", alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("practice6_class_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved practice6_class_dashboard.png")

print("\nGrade counts:", dict(zip(grade_names, grade_counts)))
