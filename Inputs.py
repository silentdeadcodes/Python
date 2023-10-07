user = input("What is your name? ")
user = user.capitalize().title().strip()

age = int(input("How old are you? "))

height = float(input("How tall are you (cm)? "))

print("")
print("Hello, " + user + " you are "+ str(age) +" years old!")
print("You are "+ str(height) + "cm tall!")

