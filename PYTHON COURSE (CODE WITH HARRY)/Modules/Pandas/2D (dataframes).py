import pandas as pd
data = pd.DataFrame({
  'Name' : ['Alice' , 'Bob' , 'Charlie'],
  'Age' : [25 , 30 , 35],
  'City' : ['New York' , 'London' , 'Paris']
})
data.to_csv('dummy_data.csv', index = False)
data_loaded = pd.read_csv('dummy_data.csv')
print(data_loaded , "\n")

# data.head(3)
print(data.head(3))
print("\n")
print(data.tail(2))
print("\n")
print(data.describe() , "\n")
print(data.info())

print(data[['Name' , 'Age']])

print(data['Age'] > 30)

