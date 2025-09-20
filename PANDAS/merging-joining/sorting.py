import pandas as pd
data = {
    "Name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28,None,40,25,43,34,30,23],
    "Salary": [50000, None, 65000, 70000, 89000, 40000, 35000, 63000],
    "Performance_Score": [85,None,75,68,90,67,86,94]
}

df = pd.DataFrame(data)


#Sorting Data by Name
df.sort_values(by="Name", ascending=False, inplace=True)
print(df)

print("#Multi Sort")
#Multi Sorting data by Name and Age
df.sort_values(by=["Name", "Age"], ascending=True, inplace=True)
print(df)

print("#Multi Sort with multi ascending")
#Multi Sorting data by Name and Age with separet ascending
df.sort_values(by=["Name", "Age"], ascending=[True, False], inplace=True)
print(df)