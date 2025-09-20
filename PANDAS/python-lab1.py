import numpy as np
import pandas as pd

data = {
    "name" : ["ram", "ramesh", "ravi", "shohan", "sandeep"],
    "Age" : [30, 32, 31, 29, 33],
    "Salary" : [20000, 30000, 40000, 45000, 25000]
}

df = pd.DataFrame(data)
print(df)