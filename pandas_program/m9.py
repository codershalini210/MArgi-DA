import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 40000, 60000, 70000, 45000]
})

grouped = df.groupby("Department")["Salary"].sum()
print(grouped)
grouped = df.groupby("Department")["Salary"].mean()
print(grouped)
data = df.groupby("Department")["Salary"].agg(["sum","mean","max","min"])
print(data)