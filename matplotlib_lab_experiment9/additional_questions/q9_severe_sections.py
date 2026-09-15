"""Additional Question 9: Identify and display all ward sections with
abnormality index AI >= 70 (severely abnormal sections).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

abnormality = np.array([
    [20, 35, 45, 60, 30],
    [25, 40, 55, 65, 35],
    [15, 30, 50, 70, 45],
    [30, 45, 60, 75, 40],
])

SEVERE_LIMIT = 70

# ------------------------------------------------------------ console report
print("=" * 55)
print("SEVERELY ABNORMAL WARD SECTIONS (AI >= 70)")
print("=" * 55)
count = 0
for r in range(abnormality.shape[0]):
    for c in range(abnormality.shape[1]):
        if abnormality[r, c] >= SEVERE_LIMIT:
            count += 1
            print(f"Section: Row {r + 1}, Column {c + 1} | "
                  f"AI = {abnormality[r, c]} | Severe Abnormality")
if count == 0:
    print("No severely abnormal sections found.")
print("=" * 55)

# ------------------------------------------------- heat map with highlights
fig, ax = plt.subplots(figsize=(9, 6))
heat = ax.imshow(abnormality, cmap="YlOrRd", aspect="auto")
plt.colorbar(heat, ax=ax, label="Glucose-Abnormality Index")
ax.set_title("Severely Abnormal Sections Highlighted (AI \u2265 70)",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Ward-Section Column")
ax.set_ylabel("Ward-Section Row")
ax.set_xticks(range(abnormality.shape[1]))
ax.set_yticks(range(abnormality.shape[0]))

for r in range(abnormality.shape[0]):
    for c in range(abnormality.shape[1]):
        value = abnormality[r, c]
        if value >= SEVERE_LIMIT:
            ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1,
                                       fill=False, edgecolor="blue",
                                       linewidth=3))
        text_color = "white" if value > abnormality.max() / 1.6 else "black"
        ax.text(c, r, str(value), ha="center", va="center",
                color=text_color, fontweight="bold")

plt.tight_layout()
plt.savefig("q9_severe_sections.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved q9_severe_sections.png")
