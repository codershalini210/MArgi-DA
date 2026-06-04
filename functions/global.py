# # x = 10   this is global
# def hello():
#     x=10  #here x is local , we can't access it outside of fun
#     print("here x is inside hello function ",x)
# hello()
# # print("here x is outside of function ",x) this will give error in case of local 
# ----------------------------
a= 10
print("a is ",a)
def changea():
    global a 
    a=20
    print("a is ",a)
changea()
print("a is ",a )