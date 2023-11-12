# set = collection which is uordered and unindexed, doesn't allow any duplicate values.
# set = {}
# If we add the same thing more than once than it will only print it once ex.

"""
utensils = {"fork", "spoon", "knife", "knife", "knife"}

---Output---
spoon
knife
fork

"""

#----Useful tips for sets----

food = {"pizza", "burger", "noodles"}
drinks = {"tea", "soda", "water"}

# We can add elements in the list
food.add("cake")

# We can also remove stuff
food.remove("burger")

# We can also clear everything in the set
food.clear()

# We can use 'x.update(y)' to add the other set values into another set
food.update(drinks)

# We can also make a new set featuring all the values from x and y. 'z = x.union(y)'
menu = drinks.union(food)

# 'print(x.differance(y))' This will print what x has that y doesn't

utensilsX = {"Fork", "Spoon", "Knife", "Plate"}
dishesX = {"Bowl", "Plate", "Cup", "Knife", "Fork"}

# This will print what utensil has that dishes don't
print("Utensils have this but dishes dont." , utensilsX.difference(dishesX))

# This will tprint what dishes has that utnsils don't
print("Dishes have this but utensils dont." , dishesX.difference(utensilsX))

# 'print(x.intersection(y))' This will print what x and y have in common.
print(utensilsX.intersection(dishesX))

#----------------------------

utensils = {"Fork", "Spoon", "Knife"}
dishes = {"Bowl", "Plate", "Cup"}

# We can use 'x.update(y)' to add the other set values into another set
utensils.update(dishes)

# We can also make a new set featuring all the values from x and y. 'z = x.union(y)'
dinner_table = dishes.union(utensils)

for x in dinner_table:
    print(x)







