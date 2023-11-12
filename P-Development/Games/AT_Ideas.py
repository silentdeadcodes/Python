import time

def deposit():
    while True:
        Amount = input("Deposit an amount: $")
        if Amount.isdigit:
            Amount = int(Amount)
            if Amount > 0:
                break
            else:
                print("The amount must be valid!")
        else:
            print("Please enter a number!")
    
    return Amount

deposit = Amount()