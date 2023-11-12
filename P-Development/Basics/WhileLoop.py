# While loop = A statement that will execute it's block of code as long as the condition remains true

# To create a infinite loop:

#while 1 == 1:
#   print("I'm stuck in a loop")

# To ask the user their name and if they don't answer then it will keep asking them

print("Username min, be 8 characters long. max, 16 characters long")
user = input("What is your name? ")

while len(user) < 8 or len(user) > 16:
    print("Enter valid a name!")
    user = input("What is your name? ")

print(user)



