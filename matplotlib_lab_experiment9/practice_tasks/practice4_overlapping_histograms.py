"""Practice Task 4: Histogram with two overlapping datasets using transparency
(alpha) to compare their distributions visually.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
class_a = np.random.normal(65, 8, 200)   # Section A marks
class_b = np.random.normal(72, 12, 200)  # Section B marks

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(class_a, bins=15, color="steelblue", alpha=0.6, edgecolor="black",
        label=f"Section A (mean {class_a.mean():.1f})")
ax.hist(class_b, bins=15, color="crimson", alpha=0.6, edgecolor="black",
        label=f"Section B (mean {class_b.mean():.1f})")

ax.axvline(class_a.mean(), color="steelblue", linestyle="--", linewidth=1.5)
ax.axvline(class_b.mean(), color="crimson", linestyle="--", linewidth=1.5)

ax.set_title("Overlapping Histograms: Marks of Two Sections", fontsize=13,
             fontweight="bold")
ax.set_xlabel("Marks")
ax.set_ylabel("Frequency")
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("practice4_overlapping_histograms.png", dpi=150,
            bbox_inches="tight")
plt.show()
print("Saved practice4_overlapping_histograms.png")
