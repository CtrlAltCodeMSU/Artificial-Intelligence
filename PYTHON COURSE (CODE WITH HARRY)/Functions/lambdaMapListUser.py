multiply_list = lambda x: x*2

user = input("Enter numbers seperated by spaces: ")

numbers = list(map(int, user.split()))

multiple = list(map(multiply_list, numbers))

print("Square: " , multiple)