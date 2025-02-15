import pandas as pd

data = { #dictionary
  'A' : [1,2,3,4,5], # row
  'B' : ['a' , 'b' , 'c' , 'd' , 'e'], # row
  'C' : [10,20,30,40,50] #column
}

data = pd.DataFrame(data) #converting dictionary to dataframe
print(data, "\n" ) #dataframe

print(data.loc[:3] , "\n")  #slicing

print(data[['A']] , "\n")  #slicing

print(data.loc[1:3 , ['B','C']] , "\n")   #slicing

print(data[data['A']>2] , "\n") #conditional slicing

data['D'] = data['A'] + data['C']  #add new column
print(data , "\n")

data['E'] = data['A'] * data['C']  #add new column
print(data , "\n")

data.drop('E', axis = 1, inplace = True) #drop column
print(data , "\n")

data.drop('D', axis = 1, inplace = True) #drop column
print(data , "\n")

data.drop([1,3], axis = 0, inplace = True) #drop row
print(data , "\n")

# data.drop([1,3], axis = 0, inplace = True) #drop row
# print(data , "\n")

data.reset_index(inplace = True) #reset index
print(data , "\n")