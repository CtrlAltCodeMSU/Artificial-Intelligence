# greeting = "hello" + ',' + "World"
# print(greeting)

# name = 'Sana Ullah'
# welcome = f'Hello, {name}!'
# print(welcome)

# words = ['python' , 'is' ,'fun']
# sentence = ' '.join(words)   #it will join words without commas
# print(sentence)


# text = "Hello, World!"
# print(len(text))
# print(text[-1])

#slicing
# name = "Government-University"
# print(len(name))
# # print(name[0:5])

# print(name[1:15:3])

# text = "pyTHOn proGraMMing"
# print(text.upper())
# print(text.title())
# print(text.title())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# print(text.swapcase())

# text1 = "Python is love"
# print(text1.find('is'))

# print(text1.count('o'))

# replace = text1.replace('love','Awesome')
# print(replace)

# text = ['Python', 'is', 'fun']
# new = " ".join(text)
# print(new)

#opposite of above
# text = "python is fun"
# word = text.split()
# print(word)

# text = "    Hello, World!     "
# print(text)
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

#formatting String
name = "Sana Ullah"
age = 21
greeting = f"My name is {name} and i am {age} years old"

print(greeting)

greeting = "My name is {} and i am {} years old.(Using format function)".format(name,age)
print(greeting)

greeting = "My name is %s and i am %d years old."% (name,age)
print(greeting)


text = "hello"
print(text.center(10))


test = "Python is fun"
print("Python" in test)
print("Java" not in test)



