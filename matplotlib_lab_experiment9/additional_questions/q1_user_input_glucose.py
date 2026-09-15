"""Additional Question 1: Line graph accepting glucose readings from the user.

Prompts the user for the number of readings and the day + glucose value of
each, then plots the glucose trend. Falls back to the default sample data
when run non-interactively (e.g. piped input / no console).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def read_data():
    """Read monitoring days and glucose readings from the user."""
    try:
        n = int(input("Enter the number of glucose readings: "))
        days, glucose = [], []
        for i in range(n):
            day = float(input(f"  Reading {i + 1} - day: "))
            value = float(input(f"  Reading {i + 1} - glucose (mg/dL): "))
            days.append(day)
            glucose.append(value)
        return np.array(days), np.array(glucose)
    except (EOFError, ValueError):
        print("No valid input provided - using default sample data.")
        return (np.array([0, 3, 6, 9, 12, 15, 18, 21, 24]),
                np.array([110, 125, 138, 152, 168, 180, 160, 145, 130]))


def plot_glucose(days, glucose):
    """Plot the user-supplied glucose trend."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(days, glucose, color="blue", marker="o", linestyle="-",
            linewidth=2, label="Glucose Reading")
    ax.set_title("Glucose Trend (User-Entered Readings)", fontsize=13,
                 fontweight="bold")
    ax.set_xlabel("Monitoring Period (Days)")
    ax.set_ylabel("Glucose Reading (mg/dL)")
    ax.grid(alpha=0.4)
    ax.legend()
    plt.tight_layout()
    plt.savefig("q1_user_glucose_trend.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Saved q1_user_glucose_trend.png")


if __name__ == "__main__":
    d, g = read_data()
    plot_glucose(d, g)
