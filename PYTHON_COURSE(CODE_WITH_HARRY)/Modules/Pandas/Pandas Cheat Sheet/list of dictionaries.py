import pandas as pd

data = [{'Name' : 'John' , 'Age' : 25  , 'City' : 'New York'} , {'Name' : 'Jane' , 'Age' : 30 , 'City' : 'London'} , {'Name' : 'Joe' , 'Age' : 35 , 'City' : 'Paris', }]

df = pd.DataFrame(data)

print(df)