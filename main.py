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

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)
plt.title('Info')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()