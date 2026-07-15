import pandas as pd
df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Raj","Aman"],
    "Marks": [70, 30, 65,25]
})

# df["Marks"]=df["Marks"].apply(lambda x: x + 10)

df = df.replace({"Amit":"Amit Kumar","Neha":"Neha sharms",30:35})
df["bonus"]=5
df["total"] = df["Marks"]+df["bonus"]
df["result"] =df["Marks"].apply(lambda x : "pass" if x>34 else "fail" )
df["Name"] =df["Name"].replace("Raj","Rajan")
print(df)
# print(df)