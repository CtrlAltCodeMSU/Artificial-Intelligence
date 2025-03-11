class person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  @property     #getter for name:
  def name(self):
    return self.__name

  @name.setter  #setters for name
  def name(self, value):
    if isinstance(value, str):
      self.__name = value
    else:
      raise ValueError("Name must be a string")
    
  @property
  def age(self):  #getter for age
    return self.__age
  @age.setter
  def age(self, value):   #setters for name
    if isinstance(value, int) and value>0:
      self.__age = value
    else: 
      raise ValueError("Age must be a +ve Integer")

person1 = person("Ahmad" , 30)

print(person1.name)
print(person1.age)
      
  