numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
slice1 = numbers[2:6]
print(slice1)
slice2 = numbers[:5]
print(slice2)
slice3 = numbers[5:]
print(slice3)
slice4 = numbers[1:8:2]
print(slice4)

neg1 = numbers[-5:]
print(neg1)

neg2 = numbers[:-1]
print(neg2)

neg3 = numbers[:-1:2]
print(neg3)

reverse = numbers[::-2]
print(reverse)