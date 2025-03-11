import pandas as pd

data = pd.read_csv('python.csv')
# data.head(5)
# data_columns = data.columns
data_columns = data.shape
print(data_columns)