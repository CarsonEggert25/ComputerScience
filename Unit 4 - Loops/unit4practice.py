# python has 4 types of collections
# Tuple
# Set
# List
# Dictionary

#Today, were going to focus on lists
# A list is a way to store more than one value in a single varible
# those values in the list are called ITEMS
# Items can be accessed by their index (position on the list)
# INDEX                      0                   1           2                 3            4
best_elden_ring_weapons = ["Blasphemous blade", "moonveil", "river of blood", "Iron Ball", "bloodhounds fist"]

#INDEX       0      1     1     3  
best_years = [1776, 1985, 1993, 1957]

#print the index of the value in the List
print(best_years.index(1985))

#Print the best elden ring weapon
print(best_elden_ring_weapons[0])

#Print the worst of the nest elden ring weapons
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

#List items can be changed!
best_elden_ring_weapons[3] = "spiked fist"
print(best_elden_ring_weapons)

#Remove the last item in the list by its position in the list
#The .pop() function removes an item by its position in the list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)

#remove an item by its value
best_elden_ring_weapons.remove("moonveil")
print(best_elden_ring_weapons)

#Add a new item to the end of a list
best_elden_ring_weapons.append("Mohgwyn's sacred spear")
print(best_elden_ring_weapons)

import random 
numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
#Strings are lists
# Strings are just a list of characters 
word = "potato"
print(word[0])


              
