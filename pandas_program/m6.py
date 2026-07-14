import pandas as pd 
data = pd.read_excel("../Excel Work/Basic Excel.xlsx")
# print(data)
# print(data.isna())
data.dropna(axis=0,inplace=True)
print(data)