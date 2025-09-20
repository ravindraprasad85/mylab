import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("Line Chart")

plt.subplot(1, 2, 2)
plt.bar(x,y)
plt.title("Bar Chart")

# plt.subplot(1, 2, 3)
# plt.pie(x,y)
# plt.title("Bar Chart")

plt.show()