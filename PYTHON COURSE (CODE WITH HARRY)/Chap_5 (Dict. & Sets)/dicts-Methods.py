# a = {
#       "key" : "value" ,
#       "harry" : "code" ,
#       "marks" : "100" ,
#       "list" : [1,2,9]
# }

# print(a.items())  #it will give all items in the dict print both keys and value using proper formatting

# print(a.keys())  #it will print keys only
# print(a.values()) #it will print values only

# a.update({"harry" : "Coding", "Ahmad" : 100})  # it can also add and update
# print(a)

# print(a.get("harry"))    #it will give key
# print(a["harry"])        #it will give key

# #difference is when the specific key
# #doesnt exist in the key print(a.get("harry1")) 
# # it will print none , 
# # but this will throw error 
# # print(a["harry1"]) as harry onr
# #  doesnt exist in the dict


# print(a.popitem())

student = {
  "name": "Ahmad",
  "age": 22,
  "major": "Software Engineering",
  "GPA": 3.8 ,
  "Courses": ["AI" , "Python" , "C++"]
}

# student.clear() #will delete all items in the dict
# print(student)

# student_copy = student.copy()
# print(student_copy)

# items = student.items()
# print(items)

# for keys, values in student.items():
#   print(f"{keys} , {values}  : " , end="")

# ep1 = {122: 45 , 123:89 , 567:69 , 670:69}
# ep2 = {222: 67 , 566: 90}
# ep1.update(ep2)
# print(ep1)

# ep1.popitem()  #it will remove last item
# del ep1[122]   #it will remove specific item
# print(ep1)
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
# tel['jack']

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i , fruits in enumerate(basket): # enumerate will give the indexes of 
  print(i , fruits)