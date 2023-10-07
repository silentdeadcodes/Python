# Collections is ordered or unordered group of elements(some data types).
# Two types of collections (List and Tuples)
# List ex. 'x = []'
# List is an ordered collection (oredered is maintained)

x = [4, True, 'hi']

# len() tells us the length of the string

print(len(x))

# Append = adds to the end of the list ex. 'x.append('hello)'

x.append('hello')
print(x)

# Extend = Extend the list

x.extend([4,5,6,7,8,9,0])
print(x)

# Pop = it takes the last value out and print it

print(x.pop())

# You can also pop any value starting from 0 (which is the first one) to how many you have

# If we want to access one value  from the list then,

print(x[0])