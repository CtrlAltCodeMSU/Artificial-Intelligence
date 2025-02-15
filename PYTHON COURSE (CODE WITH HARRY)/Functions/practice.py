is_even = lambda x: x%2==0 
user = input("Enter Numbers seperated by spaces: ")
numbers = list(map(int , user.split()))
even = list(filter(is_even , numbers))

print("EvenNumbers: " , even)