countries = ("India", "Pakistan", "Nepal", "Bhutan", "China")

temp = list(countries)
temp.append("USA")
temp.pop(3)
temp[2] = "finland"
countries = tuple(temp)
print(countries)


tuple = (1,2,3,2,2,2,34,5,6)
res = tuple.count(2)
print(res)