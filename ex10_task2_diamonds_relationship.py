import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DIAMONDS_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"


def load_diamonds():
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diamonds.csv")
    if os.path.exists(local_path):
        return pd.read_csv(local_path)
    return pd.read_csv(DIAMONDS_URL)


def main():
    df = load_diamonds()
    print(f"Loaded Diamonds dataset: {df.shape[0]} rows x {df.shape[1]} columns")

    sample_df = df.sample(500, random_state=1)

    plt.figure(figsize=(8, 6))
    sns.regplot(x="carat", y="price", data=sample_df,
                scatter_kws={"alpha": 0.5, "s": 25, "color": "steelblue"},
                line_kws={"color": "red"})
    plt.title("Diamonds: Carat vs Price with Regression Line (Sample of 500)")
    plt.xlabel("Carat (weight of diamond)")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_task2_carat_vs_price_regplot.png"), dpi=150, bbox_inches="tight")
    plt.show()

    g = sns.jointplot(x="carat", y="price", data=df, kind="hex",
                      height=8, color="teal", joint_kws={"gridsize": 40})
    g.fig.suptitle("Diamonds: Carat vs Price Hexbin Joint Plot (Full Dataset)",
                   y=1.02, fontsize=13, fontweight="bold")
    g.set_axis_labels("Carat", "Price (USD)")
    g.savefig(os.path.join(SCRIPT_DIR, "ex10_task2_carat_vs_price_hexbin.png"), dpi=150, bbox_inches="tight")
    plt.show()

    print("\nRelationship analysis (carat vs price):")
    print("- The relationship appears CURVED, not linear.")
    print("- Price rises slowly for small carats and accelerates steeply as")
    print("  carat increases, so the straight regression line under-predicts")
    print("  prices at both the low and high carat ends.")
    print("- The hexbin joint plot on the full dataset confirms this: the")
    print("  densest hexagons bend upward, showing price grows faster than")
    print("  carat. A quadratic or log(price) model would fit better.")


if __name__ == "__main__":
    main()
