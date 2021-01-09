# def ad(n):
#     c = n+(n*n)+(n*n*n)
#     print("The Value of n is:",c)
# print(ad(2))

# def ad():
#     n = int(input("Enter the value of n:"))
#     c = n+(n*n)+(n*n*n)
#     print("The result of n is:", c)
# ad()

n = int(input("Input an integer:"))
n1 = int("%s" %n)
n2 = int("%s%s"%(n,n))
n3 = int("%s%s%s"% (n, n, n))
print(n1+n2+n3)
