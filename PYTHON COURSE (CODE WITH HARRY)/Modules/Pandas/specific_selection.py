import pandas as pd

data = pd.read_csv('python.csv')

print(data.loc[[10,12,13,15],['Name', 'Age']])

print(data[data['Age']>30])

print(data)

