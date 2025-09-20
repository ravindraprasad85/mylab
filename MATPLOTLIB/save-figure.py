#savefig(fileneame.extension, dpi = value, bbox_inches = 'tight')

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 25, 50]

#create plot
plt.plot(x, y, color='blue', marker='o')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Simple line plot')
plt.legend('upper left')
plt.grid('True')

#save plot
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
plt.show()