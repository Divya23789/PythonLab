def user_choice():
    choice = '11'
    acceptable_value = range(0, 10)
    while choice.isdigit() == False or int(choice) > 10:
        choice = input("Input enter a number(0-10):")
        if choice.isdigit():
          if int(choice) in acceptable_value:
            print("True")
          else:
            print("Sorry not in range")
        else:
            print("Sorry that is not a digit")
    return int(choice)
user_choice()
