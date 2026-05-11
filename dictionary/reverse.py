# l = {'a':'1','b':2,'c':3}
# rl={}
# for k,v in l.items():
#     rl[v]=k
# print("original list ",l)
# print("Reversed list ",rl)
# Check if a particular student exists in the dictionary.

students = {"Ram":65,"Raman":25,"Sam":26,"john":65,"Maria":18}
# student = input("Enter student name ")
# if( student in students):
#     print(student," is present in list")
# else:
#     print(student," Not present in list")


# plist={}
# flist={}
# for k,v in students.items():
#     if(v>=35):
#         plist[k]=v
#     else:
#         flist[k]=v
# print("full list ",students)
# print("pass list ", plist)
# print("fail list ",flist)

nlist =[]
mlist=[]
for k,v in students.items():
    nlist.append(k)
    mlist.append(v)
print("names ", nlist,"  marks: ",mlist)
# print("total student: average marks:  highest : name marks, lowest : name marks",no of pass ,
#  no of fail)