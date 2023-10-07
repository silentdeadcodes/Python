
def deposit():
    while True:
        Amount = input("Enter deposit amount: $")
        if Amount.isdigit():
            Amount = int(Amount)
            if Amount > 0:
                break
            else:
                print("Please enter a valid amount!")
        else:
            ("Invalid!")

    return Amount


