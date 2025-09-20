import pandas as pd
data = {
    "Name": ["Ram", "shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28,35,40,25,43,34,30,23],
    "Salary": [50000, 55000, 65000, 70000, 89000, 40000, 35000, 63000],
    "Performance_Score": [85,80,75,68,90,67,86,94]
}

df = pd.DataFrame(data)
print(df)

#Adding Column
df["Location"]=["Delhi", "Hyderabad", "Noida", "Lucknow", "Mumbai", "Kanpur", "Dehradun", "khatima"]
print(df)

#Adding with Calculation on existing DataFrame
df["Bonus"] = df["Salary"] * (10/100)
print(df)


#Insert Method adding column
#df.insert(loc, "name_data", some_data)

df.insert(0, "Employee_ID", ["100", "101", "102", "103", "104", "105", "106", "107"])
print(df)