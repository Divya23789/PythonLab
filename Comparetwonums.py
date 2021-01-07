def add():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    if a % 2 == 0 and b % 2 == 0:
        print("The min value is:", min(a, b))
        #return min(a, b)
    else:
        print("The max value is:", max(a, b))
        #return max(a, b)
add()
