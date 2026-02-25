import pandas as pd
df=pd.read_csv("students.csv")
print(df)
print(type(df))
print(type(df.marks))
print(df.head()) #gives preview of the df
print(df.info()) #gives structure+missing values+no of entries,dtypes...
print(df.describe()) #gives statistical info of numerical column
df["marks"]=pd.to_numeric(df["marks"],errors="coerce")
print(df)
print(df.info())
df=df.dropna()
print(df)
def grade(marks):
    if (marks>=80):
        return 'A'
    elif (marks>=60 and marks<80):
        return 'B'
    else:
        return 'C'
df["grade"]=df["marks"].apply(grade)
print(df)
df.to_csv("clean_students_pandas.csv",index=False)