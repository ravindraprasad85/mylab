import numpy as np
import pandas as pd

df = pd.read_json("Python\sample_files\sample_Data.json")
#print(df)

print(df.shape)
#print(df.size)
print(df.info())
#print(df.describe)
#print(df.head(6))
print(df[["category", "price"]])