class person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, value):
    if isinstance(value, str):
      self.__name = value
    else:
      raise ValueError("name must be string")
    
  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self, value):
    if isinstance (value, int) and value>0:
      self.__age = value
    else:
      raise ValueError("Age must be a +ve Integer")

def create_person():
  name = input("Enter the person`s name: ")
  age = int(input("Enter age: "))
  
  person1 = person(name, age)
  
  print(f"Person's Name: {person1.name}")
  print(f"Person's Age: {person1.age}")
  
create_person()