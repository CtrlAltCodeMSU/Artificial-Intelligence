# tuples are immutable while list are mutable

# my_list = [1, 2, 3]
# my_list[0] = 4  # my_list is now [4, 2, 3]

# my_tuple = (1, 2, 3)
# # my_tuple[0] = 4  # This will raise a TypeError



# a = (1,2,34,5)  #(type) class tuple
# a = (1) #<class 'int'>
 #its not tuple , its int type for making tuple for single element we will use (1,) comma after element


# a = (1,) #<class 'tuple'>
# print(type(a))

a = (1,34,564, False , "Ahmad" , "Ali" )
print(a)

no = a.count(1)  #it count the specific elemets 
print(no)


i = a.index(34 )  #it tells the specific element index
print(i)
