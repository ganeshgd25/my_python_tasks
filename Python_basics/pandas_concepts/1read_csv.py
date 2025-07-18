
import pandas as pd 

# load the csv file
df = pd.read_csv('C:\\Users\\HP\\Desktop\\ganesh.csv')

print(df.to_string())

# Display first 5 rows
print(df.head())

# Display last 5 rows
print(df.tail())

# shape of data rows and columns
print("shape: ", df.shape)

# columns names
print("columns" , df.columns)

# Data type of each columns
print("Data Types: ", df.dtypes)

# summary info
print(df.info())