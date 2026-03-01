#load and inspect
import pandas as pd
import numpy as np
df=pd.read_csv("students.csv")
df["marks"]=pd.to_numeric(df["marks"],errors="coerce")

mean = df["marks"].mean()
df_fillmean = df.copy()
df_fillmean["marks"]=df_fillmean["marks"].fillna(mean)
df_fillmean["age"]=df_fillmean["age"].fillna(df["age"].mean())
print(df_fillmean)
df=df.dropna(subset=["marks","age"])
print(df.info())
print(df)

marks=np.array(df["marks"])
print(marks)
print(type(marks))
print(marks+5)

df["grade"]=pd.cut(
    df["marks"],
    bins=[0,60,80,100],
    labels=['C','B','A'],
    right=True
)
print(df)