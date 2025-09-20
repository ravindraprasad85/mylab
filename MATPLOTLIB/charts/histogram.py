#Histogram used to show the distiribution of contineous data by dividation into ranges 
import matplotlib.pyplot as plt
scores = [45,46,60,68,90,65,78,54,48,82,65,72,83,49,56,68,70,93,99]
plt.hist(scores, bins=5, color="lightgreen", edgecolor="black")
plt.xlabel("Score Ranges")
plt.ylabel("No of Students")
plt.title("Score Distribution of Students")
plt.legend()
plt.show()