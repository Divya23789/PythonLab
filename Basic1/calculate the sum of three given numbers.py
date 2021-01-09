# def addition(a,b,c):
#     if a==b==c:
#         d=(a+b+c)*3
#         print("result",d)
#     else:
#         e = a+b+c
#         print("result",e)
# print(addition(3,2,2))

def addition():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    c = int(input("Enter the value of c:"))
    if a == b == c:
        d = (a+b+c)*3
        print("result",d)
    else:
        e = a+b+c
        print("result",e)
addition()

