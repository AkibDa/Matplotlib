# Why do we need Data Visualization ?
# Human brain can process information easily when it is in pictorial or graphical form.

# What is Data Visualization ?
# Data visualization is the presentation of data in a pictorial or graphical format

# What is Matplotlib ?
# Matplotlib is a Python package used for 2D graphics

# Types of Plots
# 1. Bar Graph
# 2. Histograms
# 3. Scatter Plot
# 4. Pie Plot
# 5. Hexagonal Bin Plot
# 6. Area Plot

from matplotlib import pyplot as plt
# Plotting to our canvas
plt.plot([1,2,3],[4,5,1])
# Showing what we plotted
plt.show()

from matplotlib import style

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y, 'g' ,label = 'line one', linewidth = 5)
plt.plot(x2,y2, 'c' ,label = 'line two', linewidth = 5)

plt.title('Epic Info')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend()
plt.grid(True,color = 'k')

plt.show()