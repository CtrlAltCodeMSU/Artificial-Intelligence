numbers= [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x%2==0 , numbers))
print(even)

is_even = lambda x: x%2==0
user = input("Enter Numbers seperated by space: ")
numbers = list(map(int , user.split()))
even = list(filter(is_even , numbers))
print("Even Numbers:" , even)