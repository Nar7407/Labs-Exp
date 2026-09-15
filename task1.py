import pandas as pd
import numpy as np

# Build a student DataFrame from a dictionary of lists
data = {
" Name ": [" Aditi ", " Rohan ", " Priya ", "Lauki", "Yash","Om","Swarup","Naresh" ] ,
" Branch ": [" CSE ", " ECE ", " MECH ", " CIVIL " , "EEE " , " CSE " , " ECE " , " MECH "] ,
"Age": [20 , 21 , 20 , 22 , 21, 20 , 22 , 21] ,
" CGPA ": [8.8 , 7.6 , 9.2 , 8.5 , 8.9, 7.8 , 8.1 , 9.0]
}
df = pd.DataFrame(data)
print(df)
df= pd.DataFrame(df.describe())  # summary statistics become the new rows

# Add eligibility flag based on CGPA using a vectorised condition
df["Status"]=np.where(df[" CGPA "]>7.5,"Eligible","Not -Eligible")
print(df)