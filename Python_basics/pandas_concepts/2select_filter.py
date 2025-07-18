
import pandas as pd 

df = pd.read_csv('C:\\Users\\HP\\Desktop\\ganesh.csv')

print(df) 

# column selection
print("Single column (name) :")
print(df['name'])

# print multiple columns
print("multiple columns (id and role) : ")
print(df[['id' , 'role']])

# Row selection
print("print first row using iloc ")
print(df.iloc[0])

# Row selection using loc 
print("print row using loc assuming index is 0 :")
print(df.loc[0])

# condtional filtering

print("roles where is developer ")
print(df[df['role']=='Developer'])

# rows where is id is >3
print("Rows where id is >3")
print(df[df['id'] >3])