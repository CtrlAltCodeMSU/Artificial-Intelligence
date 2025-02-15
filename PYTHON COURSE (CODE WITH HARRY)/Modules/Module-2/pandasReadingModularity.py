import pandas as pd

data = pd.read_csv('D:\Python Data\PYTHON COURSE (CODE WITH HARRY)\Modules\Altair\Python.csv' , usecols=['Name','Age'] )
# usecols use for selecting specific columns
# nrows use for selecting number of rows
# nclos use for selecting number of columns
# index_col use for selecting index column
# skiprows use for skipping rows
# skipfooter use for skipping footer rows
# header use for selecting header
# names use for selecting column names
# dtype use for selecting data type
# na_values use for selecting missing values
# rename use for renaming columns by using dictionary for example rename = {'old name' : 'new Name'}
# drop use for dropping columns by using list for example drop = ['Name' , 'Age']
# like data = data.drop(columns = ['Name' , 'Age'])
# for drop we use data = data.drop(coumns = ['Name' , 'Age'])
# for rename we use data = data.rename(columns = {'old name' : 'new Name'})
print(data)