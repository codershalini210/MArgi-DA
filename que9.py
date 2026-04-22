# 9. Take a number and check if it is 
# between 10 and 100 using nested if (no logical operators).
a  = int(input("Enter any no"))
if(a>10):
    if(a<100):
        print("no is between 10-100")
    else:
        print("no is not between 10-100")
else:
    print("no is not between 10 and 100")