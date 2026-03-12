import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data={
    "hours":[4,6,8,10,12],
    "marks":[50,65,78,86,95]
}
df=pd.DataFrame(data)
print("Covariance Matrix")
print(df.cov())
#covariance between hours and marks
print("Covariance between hours and marks")
print(df["hours"].cov(df["marks"]))
#heatmap- covariance visualization
sns.heatmap(df.cov(),annot=True)
plt.title("Covariance Heatmap")
plt.show()
#correlation
print("Correlation Matrix")
print(df.corr())
#correlation between hours and marks
print("Correlation between hours and marks")
print(df["hours"].corr(df["marks"]))
#correlation visualization using heatmap
sns.heatmap(df.corr(),annot=True)
plt.title("Correlation Heatmap")
plt.show()
#Scatter plot between hours and marks
plt.scatter(df["hours"], df["marks"])
plt.title("Scatter plot between hours and marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()