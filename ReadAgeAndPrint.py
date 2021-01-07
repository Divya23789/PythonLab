def child():
    age = 'WRONG'
    while age.isdigit() == False:
        print("Enter the age of child:")
        age = input()
        if age.isdigit():
           if int(age) < 12:
               print("Child")
           elif int(age) >= 12 and int(age)<=18:
               print("Youngsters")
           elif int(age) > 18 and int(age)<110:
               print("Adult")
           else:
               print("Enter the numbers between 1 to 100")
        else:
           print("Not valid input, please enter again: ")
    return int(age)
child()
