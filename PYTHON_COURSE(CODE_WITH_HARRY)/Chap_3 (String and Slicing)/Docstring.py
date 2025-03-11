# DocString are used to describe the purpose of the program 
# def square(n):
#   """This function returns the square of the number"""
#   print( n**2)
# square(5)
# print(square.__doc__)
# """
# This module provides utility functions for basic arithmetic operations.

# Functions:
# - add_numbers(a, b): Returns the sum of two numbers.
# - subtract_numbers(a, b): Returns the difference between two numbers.
# """

# def add_numbers(a, b):
#     return a + b

# def subtract_numbers(a, b):
#     return a - b


# def add_numbers(a, b):
#     """
#     This function takes two numbers and returns their sum.

#     Parameters:
#     a (int or float): The first number.
#     b (int or float): The second number.

#     Returns:
#     int or float: The sum of the two numbers.
#     """
#     return a + b

# # Accessing the docstring
# print(add_numbers.__doc__)
def square(n):
  print(n)  #doc string only work after defination, here it wont work as it is after print statement in defined function
  """This function returns the square of the number"""
  print( n**2)  

square(5)
print(square.__doc__)
def square(n):
   #here it will work here as it is after the function
  """This function returns the square of the number"""
  print( n**2)  

square(5)
print(square.__doc__)

