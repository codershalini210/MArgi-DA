# Create a new column Grade using:
# A : Average ≥ 90
# B : Average ≥ 75
# C : Average ≥ 60
# # D : Otherwise
import pandas as pd
df = pd.DataFrame({
    "Name":["Amit","Neha","Raj","Pooja","Rohan","Anjali"],
    "Math":[78,92,65,88,55,81],
    "Science":[82,89,70,91,60,85]
})
df["total"] = df["Math"]+df["Science"]

df["avg"] = df["total"].apply(lambda x: x/2)
df["result"] =df["avg"].apply(lambda x: "Ist" if x>=90 else "2nd" if x>=75 else "3rd" if x>=60 else "D")
print(df)