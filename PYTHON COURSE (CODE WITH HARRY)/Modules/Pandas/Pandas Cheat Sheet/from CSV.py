import pandas as pd
data = pd.read_csv('python.csv')
# print(data.head())   # First 5 rows
# print(data.tail())   # Last 5 rows
# print(data.sample(5)) # Random 5 rows
# print(data.describe()) # Summary statistics
# print(data.shape) # Number of rows and columns
# print(data.info()) # Information about the dataset

# print(data.columns) # Names of the columns

# print(data.dtypes) # Data types of the columns
# print(data.isnull().sum()) # Number of missing values in each column

# print(data.nunique()) # Number of unique values in each column

# print(data['Name'].unique()) # Unique values in the "Name" column

# print(data['Name'].nunique()) # Number of unique values in the "Name" column

# print(data.index) # Index of the rows

# print(data.sort_values('Name')) # Sort the data by the "Name" column

# print(data.sort_values('Age'))
# print(data.sort_values('Salary'))
# print(data)
# 
# print(data.copy()) # Create a copy of the dataframe

# new_data = data.copy() # Create a copy of the dataframe

# # new_data['Age'] = 25
# print(new_data)

# print(data.memory_usage()) # Memory usage of the dataframe
# print(data.memory_usage().sum()) # Total memory usage of the dataframe

# print(data[['Salary']])
# print(data.sort_values('Salary' , ascending = False)) # Sort the data by the "Salary" column in descending order

# print(data.iloc[2:10]) # 2-9 rows using iloc
# print(data.loc[2:10])  # 2-10 rows using loc

# print(data.iloc[1:3])  # 1-2 rows using iloc

# print(data.iloc[0: 4 , 0:4 ]) # 0-3 rows, 0-3 columns using iloc

# print(data.iloc[: , 0:4 ]) # All rows, 0-3 columns using iloc , and this cannot be used with loc as it does not include the last row
#with loc we use names of the columns and in iloc we use numbers or integers starting from 0 .


print(data.iloc[-3:]) # Last 3 rows using iloc

print(data.iloc[:-3]) # All rows except the last 3 using iloc

print(data.iloc[1:-3]) # All rows except the first and last 3 using iloc

# print(data.iloc[-2:-4]) # Last 2 rows using iloc

# print(data.iloc[[4,7,6],[0,3,5]]) # 4th, 7th, 6th row, 0th, 3rd, 5th column using iloc
print(data.iloc[11:15, 0:3]) # 11th, 12th, 13th, 14th, 15th row, 0th, 1st, 2nd column using iloc

print(data.describe()) # Summary statistics

print(data.describe(include = 'all')) # Summary statistics including missing values
