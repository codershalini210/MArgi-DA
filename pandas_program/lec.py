import pandas as pd
# df = pd.read_excel("../Excel work/Basic Excel.xlsx")
# print(df.head(1))
# # print(df.info())
# # print(df.describe)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# df = pd.DataFrame({
#     "Name": ["Amit", "Neha", "Raj"],
#     "Marks": [80, 90, 85]
# }, index=["a", "b", "c"])
# print(df)
# print(df.loc["b"])

# import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Raj"],
    "Marks": [80, 90, 85]
})

df["Bonus"] = [5,42,12]
df["Total"] = df["Marks"] + df["Bonus"]

# df["Marks"]=df["Marks"].map(lambda x:x*10)
df["Marks"]=df["Marks"].apply(lambda x :x+2)
print(df)