# Dictionary = A changeable, unordered collection of uniques key: value pairs fast because they use
# hashing, allows us to access a value quickly

# Dictionary-->  x = ("something":"something")

# Captial is the dictionary and it has keys with some unique value pairs
capitals = {"USA":"Washington DC", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow"}

# Not the safest method to get the key and if the key is wrong it will come with an error
print(capitals["China"])

# More safer option if that key doesn't exist it will say 'none':
print(capitals.get('Germany'))

#---Dictionary tips---

# Only print the key, but not the value
print(capitals.keys())

# Only print the value, but not the key
print(capitals.values())

# Get both the keys and the values
print(capitals.items())

# We can also add another value insite the dictionary
capitals.update({"Germany":"Berlin"})

# we can also use update to update the key value pair
capitals.update({"USA":"Las Vegas"})

# 'x.pop({"something":"something"})' to remove a key value pair
capitals.pop("USA")

# 'x.clear()' remove everything in the dictionary
capitals.clear()

#---------------------

# iterate once for each key value pair in my dictionary (printing only all the keys and value)

for key,value in capitals.items():
    print(key, "-", value)



