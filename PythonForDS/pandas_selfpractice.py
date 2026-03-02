import pandas as pd
df=pd.read_csv("sales.csv")
df["price"]=pd.to_numeric(df["price"],errors="coerce")
df["quantity"]=pd.to_numeric(df["quantity"],errors="coerce")
df=df.dropna(subset=["price","quantity"])
df["amount"]=df["price"]*df["quantity"]
print(df)
print(df.info())
#total sales per category
sales_per_cat=df.groupby("category")["amount"].sum()
print(sales_per_cat)
#category with the highest total sales
print(f"Category {sales_per_cat.idxmax()} has highest total sales")
#Product with the highest amount
print("Product with highest total amount")
cat_highest_sales=df.loc[df["amount"].idxmax()]
print(cat_highest_sales)
#average price of products
avg_price=df["price"].mean()
print(f"Average price of products is {avg_price}")