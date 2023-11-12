play = input("Use calculator? Y/N: ")
if play == 'Y':

    print("")

    def calc():

        oper1 = input("Choose your operation (+, -, *, /): ")
        num1 = int(input("Enter your first number: "))
        num2 = int(input("enter your second number: "))

        if oper1 == '+':
            print(num1 + num2)
        elif oper1 == '-':
            print(num1 - num2)
        elif oper1 == '*':
            print(num1 * num2)
        elif oper1 == '/':
            print(num1 / num2)
        else:
            pass
        
    while play == 'Y':
        
        play_if_not = input("Do you want to play? Y/N: ")
        if play_if_not == 'Y':
            calc()
        else:
            quit()

else:
    quit()
            


