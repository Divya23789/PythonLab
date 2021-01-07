def child():
    age = 'WRONG'
    while age.isdigit() == False:
        age = input(print("Enter the age of child:"))
        if age.isdigit():
           if int(age) < 12:
               print("Child")
           elif int(age) >= 12 and int(age)<=18:
               print("Youngsters")
           elif int(age) > 18 and int(age)>100:
               print("Adult")
           else:
               print("Enter the numbers b/w 1 to 100")
        else:
           print("Not Valid")
    return int(age)
child()
