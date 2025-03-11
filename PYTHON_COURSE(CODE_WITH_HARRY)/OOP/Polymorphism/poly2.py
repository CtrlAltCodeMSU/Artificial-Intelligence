class Animal:
  def sound(self):
    return "Some sound"
  
class Dog(Animal):
  def sound(self):
    return "Bark"
  
class Cat(Animal):
  def sound(self):
    return "meow"
  
animal = Animal()
dog = Dog()
cat = Cat()

# Call the sound method
print(animal.sound())  # Output: Some sound
print(dog.sound())     # Output: Bark
print(cat.sound())   