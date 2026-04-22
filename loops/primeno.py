n = int(input("Enter any no "))
for i in range(2,n):
    if(n%i == 0):
        print("not a prime no ")
        break
if((i+1) == n):
    print("no is prime")