#Write a Python program to check whether a specified value is contained in a group of values.

print("Enter some numbers")
n = input()
print("Enter a number to check in list")
m = input()
if m in n:
    print("The number is in the list")
else:
    print("The number is not in the list")

# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#     return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))
