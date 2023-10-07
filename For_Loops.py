# allows us to iterate(repeat) a set number of times


# 'i' is for some variable its going to do something
# creats a collection of numbers based on the input that we give it
# one number = Stop argument
# start, stop, step ex. 'for i in range(10, -1 ,-1)', so we start at 10 stop at -1 and step by -1

#simple example for 'for loop'

for i in range(10):
    print(i)

# ex. Start at 10, Stop at -1, Step by -1 

for i in range(10, -1, -1):
    print(i)

# We can also make a list and make it write the numbers

for i in [2,4,8,16,32,64,128]:
    print(i)

# We can also store the value in some variable someplace else.

x = [2,4,8,16,32,64,128]

for i in range(len(x)):
    print(x[i])

# Enumerate creates an index for the values in the list

for i, element in enumerate(x):
    print(i, element)


