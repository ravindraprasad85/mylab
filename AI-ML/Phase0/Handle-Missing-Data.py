import pandas as pd
data = {
    'Name': ['Pawan', 'Kapil', 'Lalit', 'Kishan', 'Omprakash'],
    'Age': [25, None, 44, 23, None],
    'Salary': [50000, 60000, 70000, None, None] 
}

df = pd.DataFrame(data)
print("Orogonal Dataframe")
print(df)

###Missing % of Data
print('Missing % of Data')
print(df.isnull().mean() * 100)

### Checking total missing data
print(df.isnull().sum()) #Total missing data

df_drop = df.dropna()
print(df_drop)


### Filling with mean()
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)
