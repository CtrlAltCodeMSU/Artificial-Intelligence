# def factorila(n):
#   if n==0:
#     return 1
#   else:
#     return n * factorila(n-1)
# n = int(input("Enter Number: "))
# for i in range(n , 0 , -1):
#   print(f"{i} X " , end="")
# print("\n")
# print(factorila(n))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter Number: "))
for i in range(n, 0, -1):
    print(f"{i} X ", end="")
print("1")  
print(f"Factorial of {n} is: {factorial(n)}")

