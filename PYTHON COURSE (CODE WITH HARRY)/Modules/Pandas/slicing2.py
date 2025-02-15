import pandas as pd
CSV = pd.read_csv('python.csv')

print(CSV)

print(CSV.loc[:3])

print(CSV.loc[1:3 , ['Name' , 'Age']])

print(CSV[CSV['Name'] == 'Alice'])

# CSV['Age']= 25  # new column
# print(CSV) # display new column
# print(CSV[CSV['Age'] > 30]) # display rows with age > 30

print(CSV[CSV['Age'] > 30][['Name' , 'Age']]) # display rows with age > 30

print(CSV)


print(CSV.loc[:10 , 'Salary':])




