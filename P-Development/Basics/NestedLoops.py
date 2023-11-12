# Nested Loops = The "inner loop" will finish all of its iterations before finishing one iteration
# of the "outer loop". (Having one loop inside another loop doesn't matter what type of loop it is)

# Iteration for i in range loops is 'j'

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("What symbol do you want to use? ")

for i in range(rows):
    for j in range(columns):
        # end="" will prevent it moving to the next line
        print(symbol, end="")
    # print new line when we exit the inner for loop
    # This is the outer loop
    print()

num1 = int(input("Enter first number: "))
multiply = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(num1):
    for j in range(multiply):
        print(num1 * multiply, end="")
    print()











