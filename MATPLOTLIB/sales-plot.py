import matplotlib.pyplot as plt
months = ["Jan", "Fab", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [1000, 1500, 2000, 2500, 4000, 6000, 3500, 5000, 6500, 9000, 7000, 8500]
#legend=loc="upper left" / "lower right" / "lower left"

plt.title("Monthly Sales Report 2025")
plt.xlabel("Sales per Month")
plt.ylabel("Amounts per Month")
plt.plot(months, sales, color="blue", linestyle="--", linewidth=2, marker="o",label="2025 Sales Data")

###This will show a legend in Graph
plt.legend(loc="lower right", fontsize=10, title="Sales Data" )

###To show the grid in the backend of plot 
plt.grid(color="gray", linestyle=":", linewidth=1 )

###This will zoom the grap for these value only (lim is "limit")
#plt.xlim("Jan", "Jun")
#plt.ylim(1000, 5000)

##This will replace with actual plot value in Graph
plt.xticks(["Jan", "Fab", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"], ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"])
plt.yticks([1000, 1500, 2000, 2500, 4000, 6000, 3500, 5000, 6500, 9000, 7000, 8500], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000])

###To show the plot
plt.show()