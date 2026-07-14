import pandas as pd 
# data = [12,23,43,54]
# s = pd.Series(data)
# print(s)

# student = {"name":["Aman","Ron"],
#            "age":[25,28]}
# st = pd.DataFrame(student)
# # print(st)
# print(st["name"])
# ----------------------------
data = {
    "Student": ["Amit", "Neha", "Raj", "Sara"],
    "Marks": [85, 92, 78, 88]
}
studentFrame = pd.DataFrame(data)
print(studentFrame["Marks"])
print(studentFrame["Marks"] >80)
print(studentFrame[studentFrame["Marks"] >80])
print(studentFrame["Marks"].max())
print(studentFrame[studentFrame["Marks"] == studentFrame["Marks"].max()])

