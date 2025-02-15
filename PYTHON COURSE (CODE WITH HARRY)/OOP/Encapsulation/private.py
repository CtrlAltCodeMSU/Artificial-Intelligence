class car:
  def __init__(self, make, model):
    self.make = make
    self.__engine_number = "ABC123"  #private attribute
  def car_info(self):
    return f"{self.make}, Engine: {self.__engine_number}"

car1 = car("BMW", "X5")
print(car1.make)
# print(car1.__engine_number) #this will raise private attribute error