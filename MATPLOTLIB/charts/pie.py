import matplotlib.pyplot as plt
regions = ("North", "East", "West", "South")
sales = (5000, 7000, 4000, 8000)

plt.pie(sales, labels=regions, colors=["skyblue", "gold", "lightgreen", "coral"], autopct="%1.1f%%")
plt.legend(loc="upper left")
plt.title("Regional Sales Report 2025")
plt.show()
