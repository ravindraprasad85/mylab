import matplotlib.pyplot as plt
months = ["Jan", "Fab", "Mar", "Apr", "May", "Jun"]
sales = [1000, 1500, 2000, 3500, 4000, 5000]

plt.barh(months, sales, color="orange", label="Sales 2025")
plt.xlabel("Sales Months")
plt.ylabel("Sales Amount")
plt.title("Monthly Sales Review")
plt.legend(loc="lower right")
plt.show()