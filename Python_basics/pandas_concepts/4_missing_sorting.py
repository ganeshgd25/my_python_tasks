
import pandas as pd
import numpy as np

# sample dataframe with missing values 

data = {
    'id' : [1,2,3,4,5],
    'name' : ['ganesh' , 'anjali ' , 'rahul' , None ,'Ash' ],
    'role' : ['Developer','Tester' , None , 'Designer', 'HR'],
    'salary' : [60000 , 50000, None , 55000, 49000]
}

df = pd.DataFrame(data)
print(f"Original Data \n: {df}")

# Detect missing data 
print ( "\n missing values (True if missing):")
print(df.isnull())

# count Total missing values per column
print ("\n missing count per column :")
print(df.isnull().sum())

# Drop rows if any missing values 
df_dropana = df.dropna()
print("\n After dropping rows with missing values :")
print(df_dropana)

# fill missing values 
df_fillna= df.fillna(
    {
     'name' : 'unknown',
     'role' : 'Not Assigned',
     'salary' : df['salary'].mean() # fill with avg salary

    })
print("\n After filling missing values :")
print(df_fillna)


# sorting the data 

print("\n sorted by salary (ascending)")
print(df_fillna.sort_values(by ='salary'))

# sorting with decending

print("/n sorted by name (decending) ")
print(df_fillna.sort_values(by='name', ascending=False))

