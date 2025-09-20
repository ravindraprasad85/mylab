import pandas as pd
data = {
    "Name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28,None,40,25,43,34,30,23],
    "Salary": [50000, None, 65000, 70000, 89000, 40000, 35000, 63000],
    "Performance_Score": [85,None,75,68,90,67,86,94]
}

df = pd.DataFrame(data)

#Checking data is missing or not
print(df.isnull())   