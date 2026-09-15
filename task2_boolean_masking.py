"""Experiment: boolean masking on a month of random daily temperatures."""

import numpy as np


def main():
    np.random.seed(42)  # reproducible data

    # 30 days of random temperatures between 15 and 45 C
    temperatures = np.random.randint(15, 46, size=30)

    print("Daily Temperatures (°C):")
    print(temperatures)
    print()

    # Boolean mask: count days above 40 C
    extreme_heat_mask = temperatures > 40
    extreme_heat_count = extreme_heat_mask.sum()
    print(f"Extreme heat days (> 40°C): {extreme_heat_count}")

    # Replace cold days (< 20 C) with -1 using np.where
    modified = np.where(temperatures < 20, -1, temperatures)
    print(f"\nAfter replacing values < 20°C with -1:")
    print(modified)

    # Select the days within one standard deviation of the mean
    mean = temperatures.mean()
    std = temperatures.std()
    lower = mean - std
    upper = mean + std
    within_1std = temperatures[(temperatures >= lower) & (temperatures <= upper)]

    print(f"\nMean: {mean:.2f}°C, Std Dev: {std:.2f}°C")
    print(f"Range within 1 std dev: [{lower:.2f}, {upper:.2f}]")
    print(f"Temperatures within 1 std dev of mean ({len(within_1std)} days):")
    print(within_1std)


if __name__ == "__main__":
    main()
