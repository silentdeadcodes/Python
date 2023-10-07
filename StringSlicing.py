# slicing = create a sub string by extracting other strings.
# To slice a string we can use:

# Indexing[] = set of square brackets (index operator)
# Slice() = to create a slice object

# Three optional arguments with slicing:
# [start:stop:step]

name = 'Slice One'

# Creating a sub string
# start with index 0 according to computer, so in our case index 0 would be 's'
# in 'Slice One' the index is 0-8
# when you would wanna print out 'Slice ' then you don't write [0:4] as it will print out 'slic', 
# because whenever you slice it excludes the the index you put in the stop

first_name = name[0:5]
# or
# first_name = name[:5]
# This will indicate slice out everything from, index 0 or start to the index 5

last_name = name[6:9]
# or
# last_name = name[6:]
# This will indicate slice out everything from, index 6 to the last one

# We can also step:

# This will print out the whole name as it is only stepping by 1 and printing all the letters
random_name = name[0:9:1]

# or

# This will print out some letter of the name as it is skipping by 2 and not including some letters
random_name1 = name[0:9:2]


print(first_name)
print(last_name)
print(random_name)
print(random_name1)