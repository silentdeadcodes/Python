age = int(input("What is your age? "))

while age < 0 or age > 100 or age < 10:
    print("Invalid age")
    age = int(input("What is your age? "))

print(f"you are, {age} years old!")

color = input("What is your favourite color?(q to quit) ")

while not color == 'q':
    print(f'your favourite color is {color}.')
    input("What is another one of your favourite color?(q to quit) ")


