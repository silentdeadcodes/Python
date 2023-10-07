import time

print("--Welcome to Slicing software--")
time.sleep(1)
print("")
print("In a sentence or word there are index's ex. 'slice one' starts from 0 and end 8, also you have to include the spaces as index.")
time.sleep(1.5)
input("--press enter--")
name = input("Enter your word or scentence: ")

first_name = int(input("What index whould you like to start from? "))
second_name = int(input("What index whould you like to end at? "))
step_name = int(input("What index whould you like to step by? "))

funky_name = name[first_name: second_name: step_name]
print(funky_name)



