age = int(input("enter age "))
if(age>=60):
    if(age>120):
        print("Invalid age")
    else:
        print("you are senior citizen")
else:
    if(age>0):
        print("you are not a senior citizen")
    else:
        print("Invalid age")