import scipy.ndimage as ndi
from scipy import datasets
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np

df_bill = pd.read_csv("total_bill.csv")

print(df_bill.head())

t_stat, p = stats.ttest_1samp(df_bill["total_bill"], 20)
print("One-sample t-test p-value:", p)
print("The mean total bill differs significantly from $20.")

grouped = df_bill["tip"].groupby(df_bill["smoker"])

tip_non_smokers = grouped.get_group("No")
tip_smokers = grouped.get_group("Yes")


stat1, p1 = stats.levene(tip_smokers, tip_non_smokers)
print("p-value:", p1)
print("there is high corrolation")

t_stat2, p2 = stats.ttest_ind(tip_smokers,tip_non_smokers)
print("Independent t-test p-value:", p2)


grouped2 = df_bill["total_bill"].groupby(df_bill["day"])

sun = grouped2.get_group("Sun")
sat = grouped2.get_group("Sat")
thur = grouped2.get_group("Thur")
fri = grouped2.get_group("Fri")

f_stat, p3 = stats.f_oneway(sun,sat,thur,fri)
print("ANOVA p-value:", p3)

if p3 < 0.05:
    print("At least one day's mean total bill differs significantly from the others.")
else:
    print("No significant differences across days.")

bp_before = [142, 138, 150, 135, 145, 155, 130, 148, 140, 146]
bp_after  = [135, 132, 148, 130, 140, 150, 128, 142, 136, 141]

t_stat4, p4 = stats.ttest_rel(bp_before, bp_after)
print(f"p value:- {p4}")

if p4 < 0.05:
    print("Significant difference found in the bloop pressure report before and after.")
else:
    print("NO significant difference found in the blood pressure report")