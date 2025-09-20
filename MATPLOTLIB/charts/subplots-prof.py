import matplotlib.pyplot as plt

#fig.ax = plt.subplot(nrows, ncol, figsize=(width, height))

fig, ax = plt.subplots(1, 2, figsize=(10, 5) )
x = [1,2,3,4,5]
y = [10,20,30,25,50]

ax[0].plot(x,y, color="blue")
ax[0].set_title("Line Plot")

ax[1].bar(x,y, color="green")
ax[1].set_title("Bar Chart")

fig.suptitle("Comparison in between Bar and Line Chart")
fig.align_titles()
plt.tight_layout()
plt.show()