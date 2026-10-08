import pandas as pd
import seaborn as sns
from scipy import stats
import pandas as pd

df = sns.load_dataset("penguins").dropna()

print("\n1. Shapiro-Wilk Normality Test")
for species in df["species"].unique():
    flipper = df[df["species"] == species]["flipper_length_mm"]
    stat, p = stats.shapiro(flipper)
    print(f"p-value = {p}")
    if p < 0.05:
        print("flipper length is not normally distributed.")
    else:
        print("flipper length is normally distributed.")




print("\n2. Mann-Whitney U Test")
species_list = df["species"].unique()
g1 = df[df["species"] == species_list[0]]["flipper_length_mm"]
g2 = df[df["species"] == species_list[1]]["flipper_length_mm"]
mwu_stat, mwu_p = stats.mannwhitneyu(g1, g2)
print(f"p-value = {mwu_p}")
if mwu_p < 0.05:
    print("Flipper lengths are significantly different between Adelie and Chinstrap.")
else:
    print("There is no significant difference in flipper lengths between Adelie and Chinstrap.")


print("\n3. Kruskal-Wallis Test")
species_groups = [df[df["species"] == s]["bill_length_mm"] for s in species_list]
kw_stat, kw_p = stats.kruskal(*species_groups)
print(f"p-value = {kw_p}")
if kw_p < 0.05:
    print("At least one species has a significantly different bill length.")
else:
    print("There is no significant difference in bill length among the three species.")


print("\n4. Two-Sample Kolmogorov-Smirnov Test")
islands = df["island"].unique()
i1 = df[df["island"] == islands[0]]["body_mass_g"]
i2 = df[df["island"] == islands[1]]["body_mass_g"]
ks_stat, ks_p = stats.ks_2samp(i1, i2)
print(f"p-value(Distribution across body mass) = {ks_p}")

