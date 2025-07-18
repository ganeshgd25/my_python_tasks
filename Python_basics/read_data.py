
import pandas as pd


data = {
    'id' : [1,2,3],
    'name' : ['ganesh','ash','shanky'],
    'role' : [ 'Developer','Tester','Hr']
}

df = pd.DataFrame(data)
print(df)

# fetching csv file from location
df = pd.read_csv('C:\\Users\\HP\\Desktop\\ganesh.csv')

print(df.to_string())

print("...........................")
# first 5 elements then use head()
print(df.head())


print("...........................")
# last 5 elements then use tail()
print(df.tail())

# shape (Rows and colums)
print("shape: ",df.shape)

# columes name
print("colums:", df.columns)

# datatype of each column
print(df.dtypes)

# summary info (non-null count and datatypes)
print(df.info())

# summary statistics for numerical columns
print(df.describe())

    
# Accessing the data  in single column

print(df['name'])

# Accessing data in multiple columns
print(df[['name' , 'role']])


# Aceesing rows using index
print(df.iloc[0])    # first row

# first row same here index start from 0
print(df.loc[5])

# filter rows
print(df[df['role'] == 'Developer'])