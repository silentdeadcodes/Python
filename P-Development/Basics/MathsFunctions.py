# Don't forget to import math
import math

pi = 3.14

# 'round()' will round the number
print(round(pi))

# 'math.ceil()' will round the number up to the nearest integer
print(math.ceil(pi))

# 'math.floor()' will round the number down to the nearest integer
print(math.floor(pi))

# 'abs()' will give you the absolut value of a number. Removes the nagative sign of the number. ex.
# -1 = 1, -2 = 2, -2.2 = 2.2, -x(holding a value) = x, etc.
print(abs(-pi))

# 'pow()' will rais the base number to a certain amount of power in the input ex.
print(pow(pi, 2))

# 'math.sqrt()' gives the spuare root of a number ex. 4 = 2, 16 = 4, etc. Note: You can find the
# square root of a negative number as it doesn't follow Maths giving an error as a result.
print(math.sqrt(pi))

# 'max()' will find the largest value 
# This will result in 3 as 'z = 3'.

x = 1
y = 2
z = 3

print(max(x, y, z))

# 'max()' will find the lowest value 
# This will result in 1 as 'x = 1'.

x = 1
y = 2
z = 3

print(min(x, y, z))
