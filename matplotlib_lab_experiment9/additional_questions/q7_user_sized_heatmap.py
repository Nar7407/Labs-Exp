import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def read_dimensions():
    try:
        rows = int(input("Enter number of ward rows: "))
        cols = int(input("Enter number of ward columns: "))
        if rows <= 0 or cols <= 0:
            raise ValueError
        return rows, cols
    except (EOFError, ValueError):
        print("No valid input - using default 4 rows x 5 columns.")
        return 4, 5

def plot_heatmap(abnormality):
    rows, cols = abnormality.shape
    fig, ax = plt.subplots(figsize=(9, 6))
    heat = ax.imshow(abnormality, cmap="YlOrRd", aspect="auto")
    plt.colorbar(heat, ax=ax, label="Glucose-Abnormality Index")
    ax.set_title(f"Ward Heat Map ({rows} Rows x {cols} Columns)", fontsize=13,
                 fontweight="bold")
    ax.set_xlabel("Ward-Section Column")
    ax.set_ylabel("Ward-Section Row")
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    for r in range(rows):
        for c in range(cols):
            value = abnormality[r, c]
            color = "white" if value > abnormality.max() / 1.6 else "black"
            ax.text(c, r, str(value), ha="center", va="center",
                    color=color, fontweight="bold")
    plt.tight_layout()
    plt.savefig("q7_user_heatmap.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Saved q7_user_heatmap.png")

if __name__ == "__main__":
    n_rows, n_cols = read_dimensions()
    np.random.seed(42)
    data = np.random.randint(10, 90, size=(n_rows, n_cols))
    print(f"\nGenerated random abnormality matrix of size {n_rows}x{n_cols}:")
    print(data)
    plot_heatmap(data)
