#Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

def seventeen():
    print("Enter the number:")
    x = input()
    y = int(x)-17
    if y > 17:
        print(y*2)

seventeen()
