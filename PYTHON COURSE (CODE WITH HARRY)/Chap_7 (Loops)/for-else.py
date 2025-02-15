# l = [1,7,8]

# for item in l:
#   print(item)
# else:
#   print("done")

# List of numbers
# numbers = [1, 2, 3, 4, 5, 6]

# # Searching for an odd number greater than 5
# for number in numbers:
#     if number % 2 == 0 and number > 5:
#         print(f"Found: {number}")
#         break
# else:
#     print("No odd number greater than 5 found.")


# num = 17
# for i in range(2, num):
#   if num%i==0:
#     print(f"{num} is not a prime number.")
#     break
# else:
#   print(f"{num} is a prime number.")


# grades = {'Alice' : 'A' , 'Bob' : 'B' , 'Charlie' : 'C'}

# for name in grades:
#   if name == 'David':
#     print(f"Found: David has grade {grades[name]}")
#     break;
# else:
#   print("David not found in the dictionary")



# ages = [18, 21 , 30 , 25]
# for age in ages:
#   if age<18:
#     print("Not all members are 18 or older")
#     break
# else:
#   print("All members are 18 or older")


# words = ["apple" , "banana" , "cherry" , "date" , "fig"]
# search_word = input("Enter a word to search: ").lower()

# for word in words:
#   if word == search_word:
#     print(f"{search_word} found in the list!")
#     break
# else:
#   print(f"{search_word} not found in the list.")


# numbers = input("Enter Numbers seperated by spaces: ").split()
# numbers = [int(num) for num in numbers ]
# for number in numbers:
#   if number %2!=0:
#     print(f"{numbers} is not even.")
#     break
# else:
#   print("All numbers are even")


# valid_password = ["password123" , "secure456" , "admin789"]
# for attempt in range(3):
#   user_input = input("Enter your password: ")
#   if user_input in valid_password:
#     print("Access Granted!")
#     break
#   else:
#     print("Invalid Passoword! Please try again")
# else:
#   print("Access denied. too many failed attempts")


# import random
# secret_number = random.randint(1, 10)

# for attempt in range(5):
#   guess = int(input("Guess the Number between 1 and 10: "))
#   if guess == secret_number:
#     print("Congratulations! you guessed the correct Number.")
#     break
#   else:
#     print("Incorrect guess. Try again.")
# else:
#   print(f"Sorry, the correct number was {secret_number}")


# integers = []
# for i in range(5):
#   number = int(input(f"Enter Integer {i+1}: "))
#   if number < 0 or number > 100:
#     print(f"{number} is out of the allowed range (1-100)")
#     break
#   integers.append(number)
# else:
#   print("All numbers are within the allowed range. the list of numbers: " , integers)


# integers = []
# for i in range(5):
#   number = int(input(f"Enter Integer {i+1}: "))
#   if number < 0 or number > 100:
#     print(f"{number} is out of the allowed range (0-100).")
#     break
#   integers.append(number)
# else:
#   print("All numbers are with in the allowed range. The list of numbers: " , integers)


# valid_password = ["password123" , "secure456" , "admin789"]

# for attempt in range(3):
#   user = input("Enter your password: ")
#   if user in valid_password:
#     print("Access Granted!")
#     break
#   else:
#     print("Invalid Password, Try Again.")
# else:
#   print("Access denied, too many failed attempts")

# import random
# secret_number = random.randint(1 , 10)
# for attempt in range (5):
#   guess = int(input("Enter The Number between 1 and 10"))
#   if guess == secret_number:
#     print("Congrats! You guessed correct number")
#     break
#   else:
#     print("Incorrect Guess, Try again")
# else:
#   print(f"The secret Number was {secret_number}")


# user = input("Enter Numbers Seperated by spaces: ").split()

# numberlist = [int(each) for each in user]

# for each in numberlist:
#   if each % 2 != 0:
#     print(f"{each} is not even")
#     break
# else:
#   print("All numbers are even")

# User input for a list of numbers
# user_input = input("Enter numbers separated by spaces: ").split()

# # Converting the input strings to integers
# number_list = [int(each_number) for each_number in user_input]

# # Checking if all numbers are even
# for each_number in number_list:
#     if each_number % 2 != 0:
#         print(f"{each_number} is not even.")
#         break
# else:
#     print("All numbers are even.")


# user = input("Enter a String: ")
# search = input("Enter Character to search for: ")
# for char in user:
#   if char == search:
#     print(f"Cahracter '{search}' found in the string ")
#     break
# else:
#   print(f"Character '{search}' not found in the string")

# user = input ("Enter Numbers seperated by spaces.: ").split()

# number = [int(each) for each in user]

# for each in number:
#   if each <= 0:
#     print(f"{each} is not a +ve Number")
#     break
# else:
#   print("All numbers are +ve.")


# sentence = input("Enter a Sentence: ")

# search = input("Enter a word for search: ")
# word_split = sentence.split()
# for word in word_split:
#   if word == search:
#     print(f"'{search}' is in String.")
#     break
# else:
#     print(f"'{search}' is not in String.")
  
# password = input("Enter a password: ")

# for char in password:
#   if char.isdigit():
#     print("Password contain atleast one digit.")
#     break
# else:
#   print("Password does not contain any digits.")


