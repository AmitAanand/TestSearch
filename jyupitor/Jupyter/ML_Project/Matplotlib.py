###################################### Matplotlib ##############################################
'''
Humans are very visual creatures: we understand things better when we see things visualized.
pyplot is a module in the matplotlib package. That’s why you often see matplotlib.pyplot in code.
pylab is another module, but it gets installed alongside the matplotlib package.
It bulk imports pyplot and the numpy library and was generally recommended when you were 
working with arrays, doing mathematics interactively and wanted access to plotting features.
But before using them, we need to understand the anatomy of a matplotlib plot.
'''
# Example
import matplotlib.pyplot as plt # Import the necessary packages and modules
import numpy as np
plt.isinteractive() # Checking if interactive mode is OFF/ON
plt.ioff() # Making it OFF; plt.ion() # Making it ON
# if interactive mode is off use plt.show() after the plot command
x = np.linspace(0, 10, 100) # Prepare the data
plt.plot(x, x, label='linear') # Plot the data
plt.legend() # Add a legend
# plt.savefig('myplot.jpg', dpi=600, format='jpg', transparent=True)
plt.show() # Show the plot

###################################### Matplotlib ##############################################
'''
There are 2 big components -
The Figure is the overall window or page that everything is drawn on. You can create 
multiple independent Figures. 
1. A Figure can have several other things in it, such as a suptitle, which is a centered 
title to the figure. You’ll also find that you can add a legend and color bar to your Figure.
2. To the figure you add Axes. The Axes is the area on which the data is plotted with functions 
such as plot() and scatter() and that can have ticks, labels, etc. associated with it. 
This explains why Figures can contain multiple Axes.
When you see, for example, plt.xlim, you’ll call ax.set_xlim() behind the covers. 
All methods of an Axes object exist as a function in the pyplot module and vice versa. 
Note that mostly, you’ll use the functions of the pyplot module because they’re much cleaner.
'''
# Example - with using pyplot (Cleaned Plot)
plt.figure(figsize=(5,4), dpi=200)
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='red', marker='*')
plt.xlim(1.5, 3.0)
plt.show()

###################################### Matplotlib ##############################################
'''
3. Each Axes has an x-axis and a y-axis, which contain ticks, which have major and minor ticklines
and ticklabels. There’s also the axis labels, title, and legend to consider when you want 
to customize your axes, but also taking into account the axis scales and gridlines.
4. In most cases, you’ll use add_subplot() to create axes; Only in cases where the 
positioning matters, you’ll resort to add_axes(). Alternatively, you can also use 
subplots() if you want to get one or more subplots at the same time.
'''
# 
plt.figure(figsize=(20,10), dpi=100)
plt.subplot(1,2,1)
plt.bar([1,2,3],[3,4,5]) # First plot
plt.subplot(1,2,2)
plt.barh([0.5,1,2.5],[0,1,2]) # Second plot
plt.show()

###################################### Matplotlib ##############################################
'''
ax.bar()	        Vertical rectangles
ax.barh()	        Horizontal rectangles
ax.axhline()	    Horizontal line across axes
ax.vline()	        Vertical line across axes
ax.fill()	        Filled polygons
ax.fill_between()	Fill between y-values and 0
ax.stackplot()	    Stack plot
ax.arrow()	        Arrow
ax.quiver()	        2D field of arrows
ax.streamplot()	    2D vector fields
ax.hist()	        Histogram
ax.boxplot()	    Boxplot
ax.violinplot()	    Violinplot
plt.imshow() - Display images data
'''

from sklearn.datasets import load_digits
data = load_digits()['data']
data.shape
plt.imshow(data[323].reshape(8,8))

plt.subplot(2,2,1)
plt.boxplot(irisDF['sepal_length_(cm)'])
plt.subplot(2,2,2)
plt.boxplot(irisDF['sepal_width_(cm)'])
plt.subplot(2,2,3)
plt.boxplot(irisDF['petal_length_(cm)'])
plt.subplot(2,2,4)
plt.boxplot(irisDF['petal_width_(cm)'])
plt.show()

plt.boxplot([1,2,5,7,8,10,12,15,50])
plt.show()

# Example
plt.figure(figsize=(20,10), dpi=100)
plt.subplot(1,3,1)
plt.bar([1,2,3],[3,4,5]) # First plot
plt.axvline(x=0.65) # Add Vertical line across the axes
plt.title("Bar plot")
plt.subplot(1,3,2)
plt.barh([0.5,1,2.5],[0,1,2]) # Second plot
plt.axhline(y=0.45) # Add Horizontal line across the axes
plt.subplot(1,3,3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='red', marker='*')
plt.suptitle('Main title')
plt.show()

# Add legend
plt.legend() 
# Change plot title and axes labels 
plt.xlabel("X"); plt.ylabel("Y"); plt.title("All types of plots")
# plt.xlim(0.5, 4.5); plt.xlabel(0.5, 4.5)
plt.yticks([0, 2, 4, 6, 8, 10]) # Ticks on y-axis
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B']) # Labels for Ticks

# Histogram
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 5)
plt.show()

# Example
plt.plot([1,2,3], label='Increasing')
plt.plot([3,2,1], label='Decreasing')
plt.legend()
plt.show()
