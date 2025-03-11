marks = {
  "Harry"  : 100 ,
  "Ahmad"  : 65 ,
  "Ali"    : 25
}

print(marks, type(marks))  #dictionary type

# print(marks[0]) #throw error dictionaries are unindexed
print(marks["Harry"]) #it is valid it will give corresponding value of the mentioned key


a = {
      "key" : "value" ,
      "harry" : "code" ,
      "marks" : "100" ,
      "list" : [1,2,9]
}

print(a["key"]) #its valid
print(a["list"]) #its valid
# -----properties of dictionary----
#its unordered
#its mutable
# its indexed
# cannot contain dublicate keys

# info = {
#   "name" : "Ahmad" ,
#   "age"  : 22 ,
#   "city" : "Karachi"
#   }

# # print(info["name1"]) #key error
# print(info.get("name2")) #get wil not throw error it just say None
# print(info.items())
# for key, value in info.items():
#   print(info[key])
#   print(f"The value corresponds to the key , {key} is  {value}")


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
tel['jack']
print(tel)

x ={x: x**2 for x in (2, 4, 6)}

print(x)

for i in reversed(range(1, 11 , 2)):
  print(i)
  
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana' , 'apple', 'apple','orange', 'banana' ]

print(basket)
print("\n")
for i in sorted(basket):
  print(i , end=" ")

print("\n")

for i in sorted(set(basket)):
  print(i , end=" ")
print("cherry")

if (1 , 2 ) < (1, 2 , -1):
  print("yes")
else:
  print("no")
if (1, 2, 3) == (1.0, 2.0, 3.0):
  print("yes")
else:
  print("no")
if (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4):
  print("yes")
else:
  print("no")
if 'ABC' < 'C' < 'Pascal' < 'Python':
  print("yes")
else:
  print("no")
  
Questions = ['name' , 'quest' , 'favorite color']
Answers = ['lancelot' , 'the holy grail' , 'blue']

for q , a in zip(Questions, Answers):
  print('What is your {0}?  it is {1}.' .format(q, a))
