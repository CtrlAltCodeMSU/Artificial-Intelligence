class dog:
  def sound(self):
    return "bark"
class cat:
  def sound(self):
    return "Meow"
  
def animal_sound(animal):
  print(animal.sound())
    
D1 = dog()
C1 = cat()

animal_sound(D1)
animal_sound(C1)