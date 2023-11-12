# CONDITION is python is something that evaluates or compares other variables or data types and and
# it returns to us something that is either True or False based on the comparison. ex:
# is x = y, is x < y, is x > y, those are comparison and the answer to them is either True or false.

# Bool (Boolean) = True or False

# == is the left hand side equal to the right hand side
# != not equal which checks for unequality is left hand side not equal to the right hand side
# <= less than or equal to
# >= greater than or equal to
# < less than
# > Greater than

# Examples:

print(7.5 != 8)

x = 'hello'
y = 'hello'

print(x == y)

# this proves x does equal to y

print(x != y)

# this statement is false as x does equal to y

# We can also compare letters, example:

print('a' > 'z')

# lowercase a is not greater than lower case z and we can check the ordinal (according to ASCII code):

print(ord('z'))
print(ord('a'))

# The ordinal number represents to us that lowercase z has more value than lowercase a.
# We're only comparing the ORDINAL value not the value of a variable.

#----------------

# Chained conditions

a = 10
b = 11
c = 0

Result1 = a == b
Result2 = b > a
Result3 = c - 2 > b + 4

# to chain conditionals together use in order of operations (not, and, or)

Result4 = Result1 or Result2
print(Result4)

print(not (False and True))
print(not (False or True))

# - how to add the glowing effect
# - how to make it flow out




