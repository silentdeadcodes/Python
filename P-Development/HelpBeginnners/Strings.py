name2 = 'Slice'

#print methods

#1
print('hello')

# with variables

#1
print("Hello,", name2)

#2

print(f"Hello, {name2}")

# "x = 'example'.upper()" or "print(x.upper())" The upper make the whole the uppercase
# "x = 'ExAmPle'.capitalize() makes the sentencing or the word correct."
# The end='' refers to that the sentence has ended and you can add another one after it.

bye = 'Bye'.upper()
print(bye, end='|')
print('end')

Sentence_One = 'HeLlO WoRlD'.capitalize()
print(Sentence_One)

#or

Sentence_Two = 'HeLlO HuMaNs'
print(Sentence_Two.capitalize())

# Count how many strings there are

print(Sentence_Two.count('L'))

# This counts how many Capital "L" there are as I put a Capital "L" in the count and if I do this:

print(Sentence_Two.count('l'))

# This command counts how many lowercase "l" there are!

# and if we do this it will count all the l's in the sentence:

print(Sentence_Two.lower().count('l'))

# This command will repeat the amount of times the string is commanded to ex.:

a = 'Cool'
b = 5

print(a * b)

# We can also add strings:

c = 'Best'
d = 'kid'

print(c + d)

# strip() removes extra space

name = '  Slice  '
name = name.strip()

print(name)

