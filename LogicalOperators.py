# logical operators(and, or, not) = used to check if two or more conditional statements is true.

temp = int(input("What is the temprature outside? "))

# not = flips the false and true ex. this stament is true adding not to it woul make it false
# Checking if both of them are true.
if not(temp >= 0 and temp <= 30):
    print("The temprature is bad today!")
    print("Stay inside!")
    
# Checking if one the staments is true.
elif not(temp < 0 or temp > 30):
    print("The temprature is good today!")
    print("go outside!")






