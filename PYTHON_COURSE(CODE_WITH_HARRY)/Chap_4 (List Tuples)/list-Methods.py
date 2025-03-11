# friends = ["Apple" , "Banana" , "Orange" , False , 5.254 , 10 ]  #lists
# print(friends)

# friends.append("Grapes")

# print(friends)

# l1 = [1,8,7,2,21,15]
# print(l1)  
# l1.sort()         #sorting of lists
# print(l1)    
# l1.reverse()      #reversing of lists
# print(l1)
# l1.insert(3,9)    #inser 9 at index 3
# print(l1)

# l1.pop(3)         #it will remove element at index 3
# print(l1) 
# print(l1.pop(3))  # it will print only specific index value

# (l1.remove(21))  #it will remove the specific mentioned  value from the list 
# print(l1)

# L2 = [2,4,67,9,1]

# L2.index(2)
# print(L2)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# transposed = []
# for i in range(4):
#   transposed.append([row[i] for row in matrix])

# print(transposed)

transposed = []
for i in range(4):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  transposed.append(transposed_row)

print(transposed)


squares = []
for x in range(10):
  squares.append(x**2)
print(squares)


square = list(map(lambda x : x**2 , range(10)))
print(square)

sq = [x**2 for x in range(10)]
print(sq)


vec = [-4, -2, 0, 2, 4]
doubled = [x*2 for x in vec]
print(doubled)


from math import pi
pi = [str(round(pi, i)) for i in range(1, 6)]
print(pi)


matrix = [
  [10, 11, 12, 13],
  [20, 21, 22, 23],
  [30, 31, 32, 33],
  [40, 41, 42, 43]
]

transposed = []
for i in range(4):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  transposed.append(transposed_row)
print(transposed)
