while True:
  add = lambda x,y:x+y
  n,m = map(int,input("Enter Two Numbers: ").split())
  print(add(n,m))
  
square = lambda z: z**2
n = int(input("Enter Number: "))
print(square(n))