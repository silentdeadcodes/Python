# if statement = block of code and it will execute only if it's condition is true

# Asking user how old are you and making the question an int as we need age not a string.
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult!")

elif age <= 17:
    print("You are a teenager!")

elif age <= 10:
    print("You are a kid!")
else:
    print("ok..")


