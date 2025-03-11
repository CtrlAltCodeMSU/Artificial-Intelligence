class car:
  def __init__(self, make, model):
    self.make = make    #public attributes
    self.model = model  #public attributes
  def car_info(Self): # Public method
    return f"{Self.make} {Self.model}"

car1 = car("BMW", "X5")
print(car1.car_info())  # Calling public method , they can be access any where