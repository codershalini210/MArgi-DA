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


# Practice Set 2 – Student Marks
# import pandas as pd

# df = pd.DataFrame({
#     "Class": ["A","A","B","B","A","C","C","B"],
#     "Student": ["Rahul","Neha","Amit","Pooja","Raj","Riya","Karan","Ankit"],
#     "Marks": [78,92,65,88,81,74,69,95]
# })
# Questions
# Find total marks of each class.
# Find average marks of each class.
# Find highest marks in each class.
# Find lowest marks in each class.
# Display all statistics using agg().
# Count students in each class.
# Which class has the highest average marks?
# Which class has the maximum total marks?
# Find the mark difference (highest − lowest) for each class.
# Sort classes according to average marks.