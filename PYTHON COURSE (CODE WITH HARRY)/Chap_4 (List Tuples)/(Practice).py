fruits = ["apple" , "banana" , "Cherry"]
index = fruits.index("apple")
print(index)


li = fruits.append("mango")
print(fruits)

insert = fruits.insert(1 , "Dates")
print(fruits)

# fruits.remove("banana")
# print(fruits)


# fruits.pop(1)
# print(fruits)

# fruits.clear()
# print(fruits)


fruit = fruits.copy()
print(fruit)

more_fruits = ["strwaerry" , "SugarCane"]
fruits.extend(more_fruits)
print(fruits)