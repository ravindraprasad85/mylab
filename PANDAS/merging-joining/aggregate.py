import pandas as pd
data = {
    "Name": ["Ram", "shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28,35,40,25,43,34,30,23],
    "Salary": [50000, 55000, 65000, 70000, 89000, 40000, 35000, 63000],
    "Performance_Score": [85,80,75,68,90,67,86,94]
}

df = pd.DataFrame(data)
print(df)

average_salary = df["Salary"].mean()
print(average_salary)

min_salary = df["Salary"].min()
print(min_salary)

max_salary = df["Salary"].max()
print(max_salary)