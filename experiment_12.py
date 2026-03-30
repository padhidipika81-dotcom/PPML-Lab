#1.WAP to plot a simple line graph
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x,y)
plt.title("Simple Line Plot")
plt.plot(x,y, linestyle='--', color='r', marker='o', label="Data line")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.grid()

plt.show()

#2.WAP to draw scatter plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,6,7,8,7]

plt.scatter(x,y,color='b',label="scatter points")

plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.show()

# draw bar plot
import matplotlib.pyplot as plt

categories = ['A','B','C','D']
values = [3,7,8,5]

plt.bar(categories, values, color='g', label="Bar Data")

plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.legend()
plt.show()

#3.WAP to draw histograms and box plot
import matplotlib.pyplot as plt

data = [22,37,5,43,6,73,55,54,11,20,51,8]

plt.hist(data, bins=5, color='purple', label='Histogram Data')
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()
#boxplot
import matplotlib.pyplot as plt

data = [7,8,5,6,9,10,15,20,21]

plt.boxplot(data)
plt.title("Boxplot")
plt.show()

#4.WAP to draw pie charts and contour plots
import matplotlib.pyplot as plt

sizes = [15,30,45,10]
labels = ['A','B','C','D']
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode = (0,0,0,0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Pie chart")
plt.axis('equal')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,50)
y = np.linspace(-5,5,50)

x, y = np.meshgrid(x,y)

z = np.sin(np.sqrt(x**2 + y**2))

plt.title("Contour plot")
plt.contour(x, y, z, levels=10, cmap='viridis')
plt.colorbar()
plt.show()


#5.WAP to draw the 3D plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5]
y = [5,6,7,8,9]
z = [2,3,3,3,2]

ax.scatter(x, y, z, color='r', label='3D points')

ax.set_title("3D scatter plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

plt.legend()
plt.show()