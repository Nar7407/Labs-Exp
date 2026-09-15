"""Practice Task 1: Plot two line series - two students' marks across 5 tests
- on the same chart with different colours, markers and a legend.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

tests = np.arange(1, 6)  # Test 1..5
alice_marks = [78, 82, 91, 85, 88]
bob_marks = [70, 75, 68, 80, 92]

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(tests, alice_marks, color="blue", marker="o", linestyle="-",
        linewidth=2, label="Alice")
ax.plot(tests, bob_marks, color="darkorange", marker="s", linestyle="--",
        linewidth=2, label="Bob")

for x, y in zip(tests, alice_marks):
    ax.annotate(str(y), (x, y), textcoords="offset points", xytext=(0, 8),
                ha="center", fontsize=9, color="blue")
for x, y in zip(tests, bob_marks):
    ax.annotate(str(y), (x, y), textcoords="offset points", xytext=(0, -14),
                ha="center", fontsize=9, color="darkorange")

ax.set_title("Marks of Two Students Across Five Tests", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Test Number")
ax.set_ylabel("Marks")
ax.set_xticks(tests)
ax.set_ylim(60, 100)
ax.grid(alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig("practice1_two_students_marks.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved practice1_two_students_marks.png")
