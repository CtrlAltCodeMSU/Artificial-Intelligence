class car:
  def __init__(self, make):
    self.__make = make
  @property
  def make(self):
    return self.__make
  @make.setter
  def make(self, value):
    if isinstance(value, str):
      self.__make = value
    else:
      raise ValueError("Value must be string")
car1 = car("Toyota")
car1.make = "Honda"
print(car1.make)