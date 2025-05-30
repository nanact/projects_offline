import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
categories = ["A", "B", "C", "D"]
values = [10, 15, 7, 20]
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 40, 10]
data = np.random.randn(100)  
df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
                   'Values': [5, 7, 10, 12, 8, 9, 15, 17]})

fig, axs = plt.subplots(2, 3, figsize=(15, 10))

axs[0, 0].plot(x, y, marker='o', linestyle='-')
axs[0, 0].set_title("Line Plot")

axs[0, 1].bar(categories, values, color='skyblue')
axs[0, 1].set_title("Bar Chart")

axs[0, 2].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'lightblue', 'pink', 'lightgreen'])
axs[0, 2].set_title("Pie Chart")

sns.histplot(data, kde=True, bins=10, ax=axs[1, 0])
axs[1, 0].set_title("Histogram with KDE")

sns.boxplot(x="Category", y="Values", data=df, palette="coolwarm", ax=axs[1, 1])
axs[1, 1].set_title("Box Plot")

plt.tight_layout()
plt.show()