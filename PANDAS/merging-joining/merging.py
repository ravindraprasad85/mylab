import pandas as pd
customer = {
    "Name": ["Ramesh", "Suresh", "Shyam", "Ritesh"],
    "ID": [10,20,30,60]
}

sale = {
    "ID": [10,20,40,50],
    "Amount": [2000,3000,4000,5000]
}

df_customer = pd.DataFrame(customer)

df_sale = pd.DataFrame(sale)

print("Inner")
df_merged = pd.merge(df_customer, df_sale, on="ID", how="inner")
print(df_merged)

print("#Outer")
df_merged = pd.merge(df_customer, df_sale, on="ID", how="outer")
print(df_merged)


print("#Right")
df_merged = pd.merge(df_customer, df_sale, on="ID", how="right")
print(df_merged)

print("#Cross")
df_merged = pd.merge(df_customer, df_sale, how="cross")
print(df_merged)