name = 'slice'

# Finds the legth of the string 
print(len(name))

# Finds a certain letter or number in the string according to index, from 0 to how much
# letter or number there are
print(name.find("e"))

# Fixes the sentence and capitalizes the first letter
print(name.capitalize())

# Makes the whole string Upper case, not including numbers or special characters
print(name.upper())

# Makes the whole string Lower case, not including numbers or special characters
print(name.lower())

# Checks if the string is a number
print(name.isdigit())

# Checks if the string is alphabetical characters, will say true if there is no space and false if
# there is space
print(name.isalpha())

# How many of the certain letter or number is in the string
print(name.count("i"))

# Replaces a certain letter with another letter
print(name.replace("i","o"))

# Multiply the string 'x' number of times
print(name*3)

# strip() removes extra space
print(name.strip())

# title() it corrects names
print(name.title())