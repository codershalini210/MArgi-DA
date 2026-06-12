import numpy as np
sales = np.array([3000,7000,5000,9000,20000,5200,6500,78000])
print(sales[sales>5000])
# print(sales>5000)
print(sales[(sales>5000)  & (sales <15000)])
print(sales[(sales<5000)  | (sales >15000)])

arr = np.array([10,20,30,40,50,60])
print(arr[0],arr[2],arr[3])
print(arr[[0,2,4]])


employees = np.array([
    [101,50000],
    [102,60000],
    [103,70000],
    [104,80000]
])
print(employees[[1,2]])

data = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(data[[2,2,1],[0,2,2]])