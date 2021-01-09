# def adstring():
#     print("Please enter a sentence:")
#     n: str = input()
#     if n[0]=='i' or 'I' and n[1]=='s' or 'S':
#         print("Correct")
#     else:
#         print('is'+"\t"+n)
# adstring()


def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))
