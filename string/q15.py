# no = "9098789098"
# endno =no[6:10]
# n = "XXXXXX"+endno
# print(n)
# #  XXXXXX9098

# email = "abc@gmail.com"
# if( "@" in email and "." in email):
#     print("valid email")
# else:
#     print("not a valid email")
# filelist = ["abc.txt","xy.slsc","demo.py","hello.doc"]
# extlist=[]
# for  f in filelist:
#     l = f.split(".")
#     ext =l[1]
#     extlist.append(ext)
#     # extlist.append((f.split("."))[1])    
# print(extlist)

# s = " hello world     how    are   you              kh"
# while("  " in s):
#     s = s.replace("  "," ")
# print(s)

# Write a program to reverse a number using a while loop.

# no =1586
# s=0
# while(no>0):
#     m = no%10
#     no =int(no/10)
#     s=s*10 +m
# print(s)
# Write a program to count digits in a number.
# no =456182364
# n= no
# d=1
# while(no>9):
#     d=d+1
#     no = no/10
# print(f"no of digits in {n} is {d}")
# Print the sum of digits of a number.
# no = 1234
# sum = 0 
# while(no>0):
#     r = no%10
#     sum = sum+ r
#     no = int(no/10)
# print("sum of digits is ",sum)
# Write a program to check if a number is palindrome.


no =12215
sno = no 
s=0
while(no>0):
    m = no%10
    no =int(no/10)
    s=s*10 +m
if(s==sno):
    print(f"{sno} is palindrome")
else:
    print(f"{sno} is not  palindrome")