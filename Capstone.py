import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

print("First 5 rows of dataset:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nChecking for missing values:")
print(df.isnull().sum())

df.fillna(df.mean(), inplace=True)  

bill_array = np.array(df["total_bill"])
print("\nNumPy Operations:")
print(f"Mean of Total Bill: {np.mean(bill_array)}")
print(f"Standard Deviation of Total Bill: {np.std(bill_array)}")

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(df["total_bill"], bins=20, kde=True, color='blue', ax=axs[0, 0])
axs[0, 0].set_title("Histogram of Total Bill")

sns.boxplot(x="day", y="total_bill", data=df, palette="coolwarm", ax=axs[0, 1])
axs[0, 1].set_title("Box Plot of Total Bill by Day")

sns.regplot(x="total_bill", y="tip", data=df, scatter_kws={'color':'red'}, line_kws={'color':'black'}, ax=axs[1, 0])
axs[1, 0].set_title("Scatter Plot of Total Bill vs Tip")

sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=axs[1, 1])
axs[1, 1].set_title("Heatmap of Correlation Matrix")

plt.tight_layout()
plt.show()