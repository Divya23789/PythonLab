import string
def user_choice():
    choice: str = 'WRONG'
    acceptable_range = list(string.ascii_lowercase)
    while choice.isalpha() == True:
        choice = input("Enter a letter between a to z:")
        if choice in acceptable_range:
            print("True")
        elif choice.isdigit() == True:
            print("Not in range")
        else:
            print("Sorry it is not accepted")
    return choice
user_choice()
