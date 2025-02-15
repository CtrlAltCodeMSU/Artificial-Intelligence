a = (1,34,564, False , "Ahmad" , "Ali" )
print(a)

no = a.count(1)  #it count the specific elemets 
print(no)


i = a.index(34 )  #it tells the specific element's index
print(i)

T1 = (1,2,3)
T2 = (4,5,6)
concatenated = T1 + T2
print(concatenated)
# (1, 2, 3, 4, 5, 6)

my_t = (1,2,3,4,5,6,7)
repeated = my_t*3
print(repeated)   
#(1, 2, 3, 1, 2, 3, 1, 2, 3)

print(2 in my_t)  #True 2 exist in my_t
print( 10 in my_t)  #False 10 no exist in my_t

print(len(my_t))  #give length of the tuple

print(min(my_t))  #give max value
print(max(my_t))  #give min value

print(my_t[1:4])  #Slicing of tuple

a,b,c,d,e,f,g = my_t
print(a,b,c,d,e,f,g)  #assign values to abcdefg


my_t = (1,2,3,4,5,6,7)
repeated = my_t*3
print(repeated)   

