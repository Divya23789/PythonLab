#Write a Python program to print out a set containing all the colors from color_list_1
# which are not present in color_list_2.
print("Enter first list colours:")
color_list_1 = set(input())
#b = set(n)
print("Enter second list of colours")
color_list_2 = set(input())
print(color_list_1.difference(color_list_2))
#c = set(m)
#print(b.difference(c))

#x = set(n)- set(m)
#print(x)


# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(color_list_1.difference(color_list_2))
