# if statement = block of code and it will execute only if it's condition is true

# Asking user how old are you and making the question an int as we need age not a string.
# Order matter(if, elif, else)
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult!")
elif age == 100:
    print("Well done on reaching a very big milestone!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You are a child!")


