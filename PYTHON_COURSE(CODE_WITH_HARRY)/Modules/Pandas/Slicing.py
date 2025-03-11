import pandas as pd

# Create a DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e'],
    'C': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
print(df,"\n")

# Slicing rows using .loc
print("Rows 1 to 3:")
print(df.loc[1:3])

# Slicing columns
print("\nColumn A:")
print(df[['A']])

# Slicing both rows and columns
print("\nRows 1 to 3 and Column A:")
print(df.loc[1:3, ['A']])

# Conditional slicing
print("\nRows where column A is greater than 2:")
print(df[df['A'] > 2])
