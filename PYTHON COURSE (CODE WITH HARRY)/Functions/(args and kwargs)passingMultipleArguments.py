def add(*args):
  return sum(args)

print(add(1,2,3,4,5))


def greet(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}: {value}")
greet(name="Alice" ,age=25 , location="Pakistan")

# *args: Collects all additional arguments into a tuple.
# **kwargs: Collects all additional keyword arguments into a dictionary.
print("\t\t(Next Greet)")
def greet(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} , {value}")
greet(name="Ahmad" ,age=30 , location="United Kingdom")


def my_function(*args, **kwargs):
    print(args)
    print(kwargs)

my_function(1, 2, 3, name="Alice", age=30)