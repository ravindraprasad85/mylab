import matplotlib.pyplot as plt
x = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
y = [7, 10, 15, 25, 20, 30]

plt.plot(x, y)

plt.title("Baker sales this week")
plt.xlabel("Sale Week Days")
plt.ylabel("Sales per Day")

plt.show()