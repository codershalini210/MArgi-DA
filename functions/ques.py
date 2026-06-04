# Write a function that accepts any
#  number of names and prints them in uppercase.
# def showname(*names):
#     for name in names:
#         print(name.upper())
# showname("Raman","Aman","Neeta")



# def sumofsquares(*numbers):
#     sum = 0
#     for n in numbers:
#         sum= sum+ (n*n)
#     print(sum)
# sumofsquares(2,3,4)
# sumofsquares(10,2)


# def sumofoddno(*nos):
#     sum = 0
#     for i in nos:
#         if(i%2==1):
#             sum = sum+i
#     return sum
# print(sumofoddno(12,3,5,23,7,14))

# Write a function that returns whether a number is even or odd.
def check(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"
print("5 is ", check(5))
print("8 is ", check(8))