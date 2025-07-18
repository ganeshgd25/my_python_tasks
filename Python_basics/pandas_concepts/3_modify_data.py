
import pandas as pd 
#import random
df = pd.read_csv('C:\\Users\\HP\\Desktop\\ganesh.csv')

print(df) 

# Add column salary

df['salary'] = [
    60000, 50000 , 40000 , 75000 , 35000 ,
    29000 , 25000 , 19000, 20000 , 45000
]

print(df)

# 2nd option

# df['salary'] = [random.randint(40000,90000) for  _ in range(len(df))]
# print(df)

# update value 
df.loc[0,'name'] = 'ganesh D.'
df.loc[df['role'] == 'Tester','role'] = 'Quality Analyst'
print("After update values") 
print(df)

# Delete column 
# axis = 0 delete rows amd axis=1 delete columns
# inplace=true chnages in existing df not created new

df.drop('salary',axis=1 , inplace=True)
print("after Deleting salary column : ")
print(df)


# delete row (by index)
df.drop(1,axis=0 , inplace=True)
print("after deleting roe with index 1")
print(df)