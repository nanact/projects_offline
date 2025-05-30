import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
categories = ["A", "B", "C", "D"]
values = [10, 15, 7, 20]
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 40, 10]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(x, y, marker='o', linestyle='-')
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].set_title("Line Plot")

axs[1].bar(categories, values, color='skyblue')
axs[1].set_xlabel("Categories")
axs[1].set_ylabel("Values")
axs[1].set_title("Bar Chart")

axs[2].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'lightblue', 'pink', 'lightgreen'])
axs[2].set_title("Pie Chart")

plt.tight_layout()
plt.show()