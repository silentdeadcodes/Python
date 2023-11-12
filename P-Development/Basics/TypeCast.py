# Type cast = convert the data type of a value to another data type

x = 2 #int
y = 2.0 #float
z = "3" #string

# This converted '2.0' float into '2' integer. Notice it is only temporary to this line of code,
print(int(y))

# To make it permanent:
y = int(y)

# And now we can change and it should be something like this:

# y = 2.0
# y = int(y)
#  
# print(y)
#
# Output --> 2

# we can use int, float and str. But str wont make a differance int the output but the computer will
# save it as a string and if the number is a string then that means you can't preform any maths with it.
# So if you do for ex. '2' which is a string and you add 2 it will give an error, and if you multiply
# it by any number for ex. '2'* 5 it will result in 22222, because its not a number and is repeating
# a string not a number.

# By converting the value to string for ex.

x = str(x)

# We can add it into sentences

print(f"x is {x}")

# or we can make the change temporary:

print("X is "+ str(x))

#---------------

print(z)