# student = {"Raman":45,"Aman":42,"Mohit":56,"Sania":74}

# for k in student:
#     print("marks of ", k ," are ",student[k])

# for k,v in student.items():
#     print("marks of ", k ," are " , v)

# for v in student.values():
#     print(v)

# sum of n values / n
student = {"Raman":45,"Aman":42,"Mohit":56,"Sania":74,"Tanisha":87}
n =len(student) 
sum = 0

for v in student.values():
    sum = sum+v
avg = sum/n
print("average marks= ",avg)