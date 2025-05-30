import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

fig, axs = plt.subplots(2, 3, figsize=(18, 12))

sns.violinplot(x="day", y="total_bill", data=tips, palette="coolwarm", ax=axs[0, 0])
axs[0, 0].set_title("Violin Plot of Total Bill by Day")

sns.swarmplot(x="day", y="total_bill", data=tips, palette="muted", ax=axs[0, 1])
axs[0, 1].set_title("Swarm Plot of Total Bill by Day")

corr = tips.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=axs[0, 2])
axs[0, 2].set_title("Heatmap of Correlation Matrix")

g = sns.FacetGrid(tips, col="sex", row="smoker", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", color="blue")
g.fig.suptitle("FacetGrid of Total Bill vs. Tip", y=1.02)

sns.pairplot(tips, hue="sex", palette="coolwarm")
plt.suptitle("Pair Plot of Tips Dataset", y=1.02)

sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex", cmap="coolwarm")

plt.tight_layout()
plt.show()