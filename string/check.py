u = input("Enter you name ")
# print("your name has ",len(u)," alphabates")
vowelcount=0
for c in u :
    if(c in "aeiouAEIOU"):
        vowelcount= vowelcount+1

print(f"total no of vowels in {u} is {vowelcount}")