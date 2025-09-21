#Sklearn is library
#preprocessing : Its section where we make the data prepare or can find the tools
#LabelEncode : Its tool to use 

from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv(r"C:\Users\ravin\Desktop\Ravindra\mylab\AI-ML\Phase0\sample_data.csv", encoding="latin1")

df_label = df.copy()

le = LabelEncoder()

df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender'])
df_label['Passed_Encoded'] = le.fit_transform(df_label['Passed'])

## Labele Encoding
print('\nLabelled Encoded Data')
print(df_label[['Name', 'Gender', 'Gender_Encoded', 'Passed', 'Passed_Encoded']])

## ONE-Hot encoding
df_encoded = pd.get_dummies(df_label, columns=['City'])

print('\nOne-Hot Encoding Data')
print(df_encoded)
