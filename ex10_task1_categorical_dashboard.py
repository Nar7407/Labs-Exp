import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PENGUINS_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"


def load_penguins():
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "penguins.csv")
    if os.path.exists(local_path):
        return pd.read_csv(local_path)
    return pd.read_csv(PENGUINS_URL)


def main():
    df = load_penguins()
    print(f"Loaded Penguins dataset: {df.shape[0]} rows x {df.shape[1]} columns")
    df = df.dropna(subset=["species", "body_mass_g", "flipper_length_mm", "island"])

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Task 1: Categorical Comparison Dashboard - Penguins Dataset",
                 fontsize=15, fontweight="bold")

    sns.boxplot(x="species", y="body_mass_g", data=df, ax=axes[0, 0],
                hue="species", palette="pastel")
    axes[0, 0].set_title("Boxplot: Body Mass (g) by Species")
    axes[0, 0].set_xlabel("Species")
    axes[0, 0].set_ylabel("Body Mass (g)")

    sns.violinplot(x="species", y="body_mass_g", data=df, ax=axes[0, 1],
                   hue="species", palette="muted")
    axes[0, 1].set_title("Violinplot: Body Mass (g) by Species")
    axes[0, 1].set_xlabel("Species")
    axes[0, 1].set_ylabel("Body Mass (g)")

    sns.boxplot(x="species", y="flipper_length_mm", data=df, ax=axes[1, 0],
                hue="species", palette="Set2", showfliers=False)
    sns.swarmplot(x="species", y="flipper_length_mm", data=df, ax=axes[1, 0],
                  color="black", size=4, alpha=0.8)
    axes[1, 0].set_title("Swarmplot over Boxplot: Flipper Length (mm) by Species")
    axes[1, 0].set_xlabel("Species")
    axes[1, 0].set_ylabel("Flipper Length (mm)")

    sns.countplot(x="species", hue="island", data=df, ax=axes[1, 1],
                  palette="Set1")
    axes[1, 1].set_title("Countplot: Penguin Species Count per Island")
    axes[1, 1].set_xlabel("Species")
    axes[1, 1].set_ylabel("Number of Penguins")
    axes[1, 1].legend(title="Island")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(SCRIPT_DIR, "ex10_task1_categorical_dashboard.png"), dpi=150, bbox_inches="tight")
    plt.show()

    print("\nInterpretation:")
    print("- Gentoo penguins have the highest median body mass; Adelie the lowest.")
    print("- The box + swarm overlay shows every individual penguin's flipper")
    print("  length along with the median/quartile summary statistics.")
    print("- Adelie penguins live on all three islands, whereas Chinstrap are")
    print("  found only on Dream and Gentoo only on Biscoe.")


if __name__ == "__main__":
    main()
