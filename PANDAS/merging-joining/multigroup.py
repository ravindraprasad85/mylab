import pandas as pd
data = {
    "Name": ["Ram", "shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [25,34,40,25,40,34,30,25],
    "Salary": [50000, 55000, 65000, 70000, 89000, 40000, 35000, 63000],
    "Performance_Score": [85,80,75,68,90,67,86,94]
}

df = pd.DataFrame(data)
#print(df)

grouped =df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)