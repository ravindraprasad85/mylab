import numpy as np
import pandas as pd

df = pd.read_csv("Python\sample_files\sales_data_sample.csv", encoding="latin1")
#print(df)

print(df.shape)
#print(df.size)
#print(df.info)
#print(df.describe)
print(df.tail(10))