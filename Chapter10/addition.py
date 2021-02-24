mainloop = True
while mainloop == True:
    loop = True
    num1 = input("Please enter the first number: ")
    while loop == True:
        try:
            num1 = int(num1)
        except:
            print("The value you entered is not a number.")
            num1 = input("Please enter the first number: ")
        else:
            loop == False
            break

    print()

    loop = True
    num2 = input("Please enter the second number: ")
    while loop == True:
        try:
            num2 = int(num2)
        except:
            print("The value you entered is not a number.")
            num2 = input("Please enter the second number: ")
        else:
            loop == False
            break

    print()
    print(f"{num1} + {num2} = {num1+num2}")
    answer = input("Would you like to go again? [y / n] ")
    if answer == "y" or answer == "Y":
        print()
        print("-------------------------------------------------")
    else:
        mainloop = False
        break
