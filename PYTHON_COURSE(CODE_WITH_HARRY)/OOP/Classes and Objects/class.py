# class person:   # Defining a class 'Person'
#   person1 = person()  # Creating an object from the class
#   print(type(person1))  

# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
    
# person1 = person("John" , 25)
# print(person1.name)
# print(person1.age)

# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def say_hello(self):
#     print(f"Hello, my name is {self.name} and i am {self.age} years old")
# person1 = person("Sana Ullah" , 22)
# person1.say_hello()

class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def say_hello(self):
    print(f"Hello, my name is {self.name} and i am {self.age} years old")

person1 = person("Sana Ullah" , 22)
person1.say_hello()
