class employee:
  def __init__(self, name, salary):
    self.__name = name
    self.__salary = salary
 
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self , value):
    if isinstance(value, str):
      self.__name = value
    else:
      raise ValueError("Name must be a String")
    
  @property
  def salary(self):
    return self.__salary
  
  @salary.setter
  def salary(self, value):
    if isinstance(value, (int, float)) and value > self.__salary:
      self.__salary = value
    else:
      raise ValueError("New Salary must be higher than the current salary")
    
  def display(self):
    print(f"Employee Name: {self.name}, Salary: {self.salary}")
    
emp1 = employee("Ahmad" , 50000)
emp1.display()

emp1.salary = 55000
emp1.display()


try:
  employee.salary = 45000
except ValueError as e:
  print(e)
    