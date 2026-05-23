import matplotlib.pyplot as plt
import matplotlib
import numpy as np

x = np.array([2, 4, 6, 8, 10])
y = np.array([50, 120, 180, 90, 200])
# for i in dir(matplotlib):
#     print(i) 

def line_plot(x, y, color='red'):
    plt.plot(x, y, color=color, marker='o')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Line Plot')
    plt.grid(True)
    plt.show()

def bar_plot(x, y, color='purple'):
    plt.bar(x, y, color=color)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Bar Plot')
    plt.grid(True)
    plt.show()

def scatter_plot(x, y, color='blue', marker='o'):
    plt.scatter(x, y, color=color, marker=marker)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Scatter Plot')
    plt.grid(True)
    plt.show()

def histogram_plot(data, bins=5, color='green'):
    plt.hist(data, bins=bins, color=color)
    plt.xlabel('Data Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

line_plot(x, y)
bar_plot(x, y)
scatter_plot(x, y)
histogram_plot(x)

