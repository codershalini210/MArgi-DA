age = int(input("Enter age"))
if(age<0 or age>120):
    print("invalid age ")
elif(age>=18):
    print("Eligigble to vote")
else:
    print("Not eligible to vote")