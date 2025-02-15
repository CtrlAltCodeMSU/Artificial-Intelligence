print("\t\tOld method")
letter = "Hey my name is {1} and i am from {0}"  
letter1 = "Hey my name is {0} and i am from {1}"  
country = "Pakistan"
name = "Ahmad"

print(letter.format(name , country))
print(letter1.format(name , country))
print("\t\tNew method")

print(f"Hey my name is {name} and i am from {country}")


txt = "for only {price: .2f} dollars!" #it will format the price to 2 decimal places
print(txt.format(price = 49.894951269988))
print(type(f"{2*30}")) #same as print(2*30) but its is a string