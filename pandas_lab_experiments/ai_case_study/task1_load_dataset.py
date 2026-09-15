import os
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_tests.csv"))
print("First 5 records of the patient tests dataset:")
print(df.head())
