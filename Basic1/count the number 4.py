#Write a Python program to count the number 4 in a given list.

def num(n):
    count = 0
    for num in n:
        if num == 4:
            count = count+1
    return count
print(num([1,2,3,4,5,4,6,4,8,4]))

