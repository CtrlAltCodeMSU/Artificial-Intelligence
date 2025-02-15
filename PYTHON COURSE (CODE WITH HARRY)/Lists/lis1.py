list = [i*i for i in range(5)]
print(list)
list = [i for i in range(10) if i%2==0]
print(list)

list.append(10)
print(list)
list.sort()
list.reverse()
list.index()
m = list.copy()
m[0] = [0]
list.insert(1,899)
list.extend(m)