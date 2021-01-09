# Write a Python program to concatenate all elements in a list into a string and return it.
def conc(list):
    x = ''
    for i in list:
        x += str(i)
    return x
# print(conc([1,3,5,7]))
