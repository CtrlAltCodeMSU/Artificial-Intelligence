def greet(name , message):
  print(f"Hello, {name}! {message}")
  
greet("Alice" , "welcome to python progrmming")
greet(name="Alice" , message="welcome to python progrmming") 
#both are valid
# When calling a function, you can pass arguments using the parameter names. This is useful for readability and when dealing with functions that have many parameters.