# Lists = used to store multiple items in a single variable
# lists = [x, y, ....]

food = ['pizza', 'burger', 'balkalava', 'cheetos', 'noodles']

#--Useful Tips in Lists--

# 'x.append("something")' will add that certain thing in the list at the end
food.append("Ice cream")

# 'x.remove("something")' will remove a certain thing in the list
food.remove(food[1])

# or a more simpler way
food.remove('pizza')

# 'x.pop()' will remove the last element in the list
food.pop()

# 'x.insert(y, 'something')' will add a element in the position given
food.insert(0, 'pizza')

# 'x.sort()' will put all the elements in alphabetical order
food.sort()

# 'x.clear()' will remove all the elements in the list
food.clear()

#------------------------

# printing a certain item from the list
print(food[0])

# Replacing a certain item in the list
food[1] = 'sausages'

# Now if we try it the list has changed
print(food)

# Printing all the elements in a list (meaning without the brackets and only the values)
for x in food:
    print(x)

# Print all the elements in the list with an index
for x, element in enumerate(food):
    print(x, "-" ,element)




