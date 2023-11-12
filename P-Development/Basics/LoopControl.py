# Loop Control = Change a loops execution from its normal sequence

# Break = used to terminate the loop entirely
# continue =  skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# Break ex.

while True:
    name = input("Enter your name: ")
    if name != '':
        break

# continue ex. (continue skipping)

phone_number = '123-456-7890'

for i in phone_number:
    if i == '-':
        continue
    print(i, end="")

# pass ex.

# acting as place holder when nothing is there (if you don't wanna execute a certain thing)
for i in range(0,21):

    if i == 12:
        pass
    else:
        print(i)



