import pandas as pd
region1 = {
    "CustomerID": [10,20,30,],
    "Name": ["Ramesh", "Ganesh", "Shyam"]
}
df_region1 = pd.DataFrame(region1)

region2 = {
    "Amount": [1000, 2000, 3000],
    "CustomerID": [40,50,60]
}


df_region2 = pd.DataFrame(region2)

#concatenate rows 
df_concat = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print(df_concat)


#concatenate columns 
df_concat = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_concat)