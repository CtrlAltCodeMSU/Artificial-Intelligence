# numbers = input("Enter Number: ").split()
# doubled = list(map(lambda x: x*2 , numbers))
# print(doubled)

numbers= input("Enter Number: ").split()
double = []

for num in numbers:
  try:
    double.append(int(num)*2)
  except ValueError:
    print(f"Invalid input: '{num}' is not a number")
print(double)