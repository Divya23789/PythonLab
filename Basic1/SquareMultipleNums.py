my_list = [1, 2, 3, 4, 5]
def square(num):
    return num**2
#Naming Convention and Best Practise
updated_list = list(map(square, my_list))
print(updated_list)
