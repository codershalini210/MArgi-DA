import numpy as np 
# ---------------
# ary = np.full(5,100)
# ary = np.full((5,3),100)
#  this will create a 2d aryy of 5R and 3C
# print(ary)
# ---------------
# aryrange = np.arange(5)
# print(aryrange)
# aryrange =np.arange(12,18)
# print(aryrange)
# aryrange =np.arange(1,10,3)
# print(aryrange)
# ---------------
# arylin = np.linspace(0,10,5)
# print(arylin)

# arylin = np.linspace(10,20,3)
# print(arylin)

# arylin= np.linspace(20,5,3)
# print(arylin)
# ---------------------
# aryi = np.eye(4)
# print(aryi)
# aryi = np.eye(4,3)
# print(aryi)
# ----------------------
# aryrandom = np.random.randint(25,50,10)
# print(aryrandom)
# arr = np.random.rand(15)

# print(arr)

# ary = np.array([500])
# print(ary)

# ary = np.linspace(0,50,20)
# print(ary)

# Generate 20 random sales values between 1000 and 10000.
# ary = np.random.randint(1000,10000,20)
# print(ary)
# print("shape", ary.shape)
# print("size", ary.size)
# print("dime", ary.ndim)
# Create a customer age dataset using NumPy arrays.
# aryage = np.array([32,43,54,23,54,12,53])
# for i  in aryage:
#     print(i )

ary3 = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [ [33,44,55],
     [22,33,44]]
])
print(ary3)
print("dim  ",ary3.ndim)
print("size ",ary3.size)
print("shape ", ary3.shape)