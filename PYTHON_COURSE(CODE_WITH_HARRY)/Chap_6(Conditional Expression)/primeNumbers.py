for n in range(2, 20):
  for x in range(2 , n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x , end=", ")
      break
  else:
    print(n, 'is a prime number' , end=", ")
      

for num in range(2, 10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("Found an odd number", num)