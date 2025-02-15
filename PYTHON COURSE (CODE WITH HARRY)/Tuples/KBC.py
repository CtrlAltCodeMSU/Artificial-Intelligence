# questions = [
#   ["Which language was used to create to create python?", "Python" , "French" , "JavaScript" , "php" , "None" , 4 ],
  
#   ["Which of the following is not a looping statement?", "for" , "while" , "do while" , "for each" , "None" , 2 ],
  
#   ["Which of the following is not a keyword in python?", "if" , "else" , "elif" , "for" , "None" , 3 ],
  
#   ["Which of the following is not an operator in python?", "+" , "-" , "*" , "/" , "None" , 1 ],
  
#   ["Which of the following is not a data type in python?", "int" , "float" , "string" , "boolean" , "None" , 4 ],
  
#   ["Which of the following is not a variable in python?", "a" , "b" , "c" , "d" , "None" , 3 ],
  
#   ["Which of the following is not a method in python?", "len()" , "sum()" , "max()" , "min()" , "None" , 2 ],
  
#   ["Which of the following is not a class in python?", "int" , "float" , "string" , "boolean" , "None" , 4 ],
  
#   ["Which of the following is not a function in python?", "len()" , "sum()" , "max()" , "min()" , "None" , 2 ],
  
#   ["Which of the following is not a module in python?", "len()" , "sum()" , "max()" , "min()" , "None" , 2 ],

#   ["Which of the following is not a package in python?", "len()" , "sum()" , "max()" , "min()" , "None" , 2 ],

#   ["Which of the following is not a framework in python?", "len()" , "sum()" , "max()" , "min()" , "None" , 2 ],

#   ["Which of the following is not a library in python?", "len()" , "sum()" , "max()" , "min()" , "None" , 2 ],

#   ["Which of the following is not a keyword in python?", "if" , "else" , "elif" , "for" , "None" , 3 ],

#   ["Which of the following is not a method in python?", "+" , "-" , "*" , "/" , "None" , 1 ],

#   ["Which of the following is not a data type in python?", "int" , "float" , "string" , "boolean" , "None" , 4 ],

#   ["Which of the following is not a variable in python?", "a" , "b" , "c" , "d" , "None" , 3 ],
# ]

# levels = [1000, 2000 , 3000 ,  5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000]
# money = 0
# i = 0
# for i in range(0 , len(questions)):
#   question = questions[i]
#   print(f"Questions for Rs. {levels[i]}")
#   print(f"a. {question[1]}\nb. {question[2]}\nc. {question[3]}\nd. {question[4]}")
#   reply = int(input("Enter your answer: "))
#   if(reply==question[-1]):
#     print(f"correct Answer, you have won Rs. {levels[i]}")
#     if(i== 4):
#       money = 10000 
#   elif(i==9):
#       money = 320000 
#   elif(i==14):
#       money = 10000000 
#   else:
#     print("Wrong Answer")
#     break

# questions = [
#     ["Which language was used to create python?", "Python", "French", "JavaScript", "php", "None", 4],
#     ["Which of the following is not a looping statement?", "for", "while", "do while", "for each", "None", 2],
#     ["Which of the following is not a keyword in python?", "if", "else", "elif", "for", "None", 3],
#     ["Which of the following is not an operator in python?", "+", "-", "*", "/", "None", 1],
#     ["Which of the following is not a data type in python?", "int", "float", "string", "boolean", "None", 4],
#     ["Which of the following is not a variable in python?", "a", "b", "c", "d", "None", 3],
#     ["Which of the following is not a method in python?", "len()", "sum()", "max()", "min()", "None", 2],
#     ["Which of the following is not a class in python?", "int", "float", "string", "boolean", "None", 4],
#     ["Which of the following is not a function in python?", "len()", "sum()", "max()", "min()", "None", 2],
#     ["Which of the following is not a module in python?", "len()", "sum()", "max()", "min()", "None", 2]
# ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0

# for i in range(len(questions)):
#     question = questions[i]
#     print(f"Questions for Rs. {levels[i]}")
#     print(f"a. {question[1]}\nb. {question[2]}\nc. {question[3]}\nd. {question[4]}")
#     reply = int(input("Enter your answer: "))
    
#     if reply == question[-1]:
#         money = levels[i]
#         print(f"Correct Answer, you have won Rs. {money}")
#     else:
#         print("Wrong Answer")
#         break

# print(f"You have won a total of Rs. {money}")


questions = [
    ["Which language was used to create python?", "Python", "French", "JavaScript", "php", "None", 4],
    ["Which of the following is not a looping statement?", "for", "while", "do while", "for each", "None", 2],
    ["Which of the following is not a keyword in python?", "if", "else", "elif", "for", "None", 3],
    ["Which of the following is not an operator in python?", "+", "-", "*", "/", "None", 1],
    ["Which of the following is not a data type in python?", "int", "float", "string", "boolean", "None", 4],
    ["Which of the following is not a variable in python?", "a", "b", "c", "d", "None", 3],
    ["Which of the following is not a method in python?", "len()", "sum()", "max()", "min()", "None", 2],
    ["Which of the following is not a class in python?", "int", "float", "string", "boolean", "None", 4],
    ["Which of the following is not a function in python?", "len()", "sum()", "max()", "min()", "None", 2],
    ["Which of the following is not a module in python?", "len()", "sum()", "max()", "min()", "None", 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}: {question[0]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    reply = input("Enter your answer (a, b, c, d): ").lower()
    
    # Map the input to corresponding option index (1, 2, 3, 4)
    answer_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
    if answer_map.get(reply, 0) == question[-1]:
        money = levels[i]
        print(f"Correct Answer, you have won Rs. {money}")
    else:
        print("Wrong Answer")
        break

print(f"\nYou have won a total of Rs. {money}")