age = int(input("Enter Your Age: "))
print("You are " + str(age)+ " Years Old.") #its also valid
print("You are " , age ," Years Old.")  #its also valid


x ,y = input("Enter two Numbers seperated by space: ").split()
print("you entered: " + str(x) + " and " + str(y) ) #its also valid
print("you entered: " , x ," and " , y) #its also valid


x ,y = map(int,input("Enter two Numbers: ").split())
print("Sum: ", x + y) #this method is used to take multiple inputs at once

x = int(input("Enter Number: "))
y = int(input("Enter Number: "))
print("Sum is: " ,x + y)    #this is the way for taking individualy


x, y , z = map(int, input("Enter Three Numbers Seperated by Space: ").split())
print("Sum of three Numbers is: ", x + y + z)  #taking three inputs from user 


numbers = list(map(int, input("Enter Multiple numbers seperated by space: ").split()))
print("You Entered: " , numbers) #it will generate list of numbers



name = "Sana Ullah"
age = 22 
print(f"My name is {name} and i am {age} years old") #f string method


try:
    num = int(input("Enter an Integer: "))
    print("You Entered: " ,num)
except ValueError:
    print("Thats not an Integer!")


sentence = input("Enter a Sentence: ")
countWords = len(sentence.split())
print(f"Your Sentence has {countWords} words. ")#it will count words in the sentence


import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area of the circle with radius {radius} is {area: .2f}")     #.2f is used for set decimal points


num = list(map(int , input("Enter numbers: ").split()))
maxnumber = max(num)
num.sort()
print(f"the sorted list is {num}")
print(f"the maximum number is: {maxnumber}")


keys = input("Enter keys separated by commas: ").split(',')
values = input("Enter values separated by commas: ").split(',')
my_dict = dict(zip(keys, values))
print(f"Created dictionary: {my_dict}")


keys = input("Enter Keys seperated by commas: ").split(',')
values = input("Enter Values seperated by commas: ").split(',')
my_dic = dict(zip(keys , values))
print(f"Created dictionary: {my_dic}")   #zip is used for combine keys and values of dict


list1 = [1 , 2 , 3]
list2 = ['a' , 'b' , 'c']
zipped = zip(list1 , list2 )
print(list(zipped))


keys = ['name' , 'age' , 'city']
values = ['Alice' , 30 , 'New York']
my_dict = dict(zip(keys , values))
print(my_dict)


numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']
zipped = zip(numbers, letters, symbols)
print(list(zipped))


zipped = [(1 ,'a'),(2 ,'b'),(3 , 'c')]
numbers ,letters = zip(*zipped)
print(numbers)
print(letters)
