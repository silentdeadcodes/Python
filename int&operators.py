# '+' = add, '-' = subtarct, '*' = multiply, '/' = divide, '%' = Take remainder after dividing

# reason for int, because if there is no int it will think that it is a string

# if the user puts in a float it will convert it to an int, because the whole line of code is being
# converted to int.

# Calaculator

x = int(input("What is x? "))
y = int(input("What is y? "))

# The reason I said 'z = x + y' is, because I want to store the answer.
z = x + y

print(z)
