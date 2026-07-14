import pandas as pd 
# students = pd.Series(["Aman","RAman","John"])
# # print(students)
# # print(students[2])
# ---------------------
# students = pd.Series(["Aman","RAman","John"],index=["a","b","c"])
# print(students)
# print(students["b"])
# print(students.index)
# students.index=[101,102,103]
# print(students)
# for i in students.index:
#     print(f"id = {i} name ={students[i]}")
# ---------------------------
# emps = pd.Series([pd.Series(["emp1",25000]),pd.Series(["emp2",25000]),pd.Series(["emp3",25000])])
# print(emps[0])
emps = pd.DataFrame({"emp1":[25000,32000,45200],
                     "emp2":[65222,52000,56000],
                     "emp3":[23652,40000,32000]})
print(emps)
print(emps.columns)
# print(emps["emp1"])
print(emps.index)
emps.index=["jan","Feb","March"]
print(emps)
print(emps.head(1))
print(emps.tail(1))
# 10 min break 
# print(emps.head())
# for e in emps:
#     print(emps[e])