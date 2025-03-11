import pandas as pd
data=pd.read_csv('python.csv')

print(data.value_counts())

data_column = data[['Age']]
# print(data_column.value_counts())
print(data_column)
