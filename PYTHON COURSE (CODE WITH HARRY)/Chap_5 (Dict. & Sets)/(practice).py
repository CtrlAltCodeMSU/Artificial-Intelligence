student = {
  "name": "Ahmad",
  "age": 22,
  "major": "Software Engineering"
}

print(student["name"])
print(student)

student["GPA"] = 3.8
print(student)

keys = student.keys()
print(keys)
values = student.values()
print(values)
items = student.items()
print(items)

print(student.get("age"))

#-----------Sets-------------#

fruits = {"apple" , "banana" , "cherry"}
fruits.add("orange")   #for add single element at once
fruits.update(["mango","grapes"])  #for add multiple elements at once
print(fruits)

#fruits.remove("kela") # Using remove() to remove an element (raises KeyError if the element doesn't exist)

fruits.discard("kela")  # Using discard() to remove an element (does nothing if the element doesn't exist)
print(fruits)


