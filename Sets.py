# 's.add(x)' adds and number and 's.remove(x)' removes any number from a set.
# 'print(x in s)' the y(number) in s asks python if that number 'x' is in the set
# Using set '{}' is more beneficial when dealing with big numbers.
# can use Union, Difference, Intersection if there are more than one sets ex. 'print(s.union(x)'

# s = set() is a set

s3 = set()

# s = {} is actually a dictionary
s = {64,32,64,16,8,4,2,8}
s2 = {64,18,32,16,8,4,2,8}

print(s.intersection(s2))
