#import pandas as pd
#df  = pd.read_csv("Python\sample_files\sales_data_sample.csv", encoding="latin1")
#print(df.info())


import pandas as pd
df = pd.read_excel(r"Python\sample_files\SampleSuperstore.xlsx")
print(df.info())  #To summarize the dataset, used memory,