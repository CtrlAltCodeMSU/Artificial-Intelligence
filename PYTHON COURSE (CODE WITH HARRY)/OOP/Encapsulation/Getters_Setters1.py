class car:
  def __init__(self, make, model):
    self.__make = make
    self.__model = model
  @property
  def make(self):
    return self.__make
  @make.setter
  def make(self, value):
    if isinstance(value, str):
      self.__make = value
    else:
      raise ValueError("model Name must be string")
  @property
  def model(self):
      return self.__model
  @model.setter
  def model(self, value):
    if isinstance(value, str):
      self.__model = value
    else:
      raise ValueError ("Name Must be String or int")
      
car1 = car("Honda" , 2023)
print(car1.make)
print(car1.model)