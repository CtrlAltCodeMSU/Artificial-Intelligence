try:
  num = int("abc") # This will raise a ValueError because "abc" cannot be converted to an integer
except ValueError as e: 
  print(e)  # e will hold the specific error message
  
  