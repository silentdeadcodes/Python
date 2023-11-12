# Tuples = collection which is ordered but unchangable used to together group related data
# Tuples = ()

student = ("Slice",13,'male')

#counts how many name of that student are there
print(student.count('slice'))

#finds the index of the element given in the tuple
print(student.index('male'))

#display all the values within the tuple
for x in student:
    print(x)

#check to see if a certain value exists within the Tuple
if 'Slice' in student:
    print("Slice is here!")

# This is tuples and can't be changes so x.append() wouldn't work neither if you want to remove something from the Tuple.
# Not used too much, Only used for Important things like storing some data that you cant change, so nothing goes wrong.
# Example like storing some user data that you don't want to be changed.
# Mostly not useful don't use use the [], {} its better. ([] = list, or {} = set)

