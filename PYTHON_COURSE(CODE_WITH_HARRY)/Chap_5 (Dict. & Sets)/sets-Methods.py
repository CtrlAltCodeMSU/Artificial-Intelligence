# s = {1,5,32,54,5,5,5,"Ahmad"} #its valid

# print(s , type(s))

# s.add(5456)
# print(s)

# # remove
# # len
# # pop
# # union
# # intersectin

# #properties
# # Sets are unordered
# # sets are unindexed cannot acces
# # there is no way to change items in sets
# # sets cannot contain/print duplicate values

# s1 = {1 , 45 , 2 , 8 ,6 , 78}
# s2 = {7, 8 , 1 , 78 }

# print(s1.union(s2))       #it will union
# print(s1.intersection(s2))  #it will intersect
# s1.update(s2)
# print(s1, s2)
# print(s1.intersection(s2))  #it will intersect


cities = {"Islamabad" , "Lahore" , "Karachi" , "Delhi"}
cities2 = {"Mumbai" , "Delhi" , "Karachi" , "Lahore" , "Goa" , "Faislabad"}

cities3 = cities.intersection(cities2)
print(cities3)
cities.update(cities2)
print(cities)


s = {1,2,3,4,5,6,7,8,9}
s.add(4)
print(s) # Output: {1, 2, 3, 4}

s.remove(2)  #keyerror , beacuse 5 is not in set, so it will throw error when we will use discard it will not throw error
print(s) # Output: {1, 3, 4}

s.discard(5) #it will not throw error
print(s)

pop = s.pop()
print(pop)

# s.clear() # it will clear the set
print(s) # Output: set()

s1 = {10,11,12,13,14,15}
s2 = s1.union(s)
print(s2)

s1 = {1,2,3}
s2 = {3,4,5}
s1.update(s2)
print(s1)

s3 = s1.intersection(s2)
print(s3)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.intersection_update(set2)
print(set1)

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print("Division successful:", result)
# finally:
#     print("This block always executes.")

# divide = 10 / 0  #it wil tghrow error ,but by using exception it wont throw error as we use try and except
# print(divide)



