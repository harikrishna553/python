import matplotlib.pyplot as plt

# Sample data
x1 = [5, 10, 15, 20, 25]
y1 = [20, 40, 60, 80, 100]

plt.plot(x1, y1, 'rs--', label='4x', markersize=5)

# To display the legend on the plot
plt.legend()

my_title_font = {
    'family': 'serif',
    'size': 20,
    'weight': 'bold',
    'color': 'blue',
    'style': 'italic',
    'stretch' : 'expanded',
    'variant' : 'small-caps'
}

plt.title('font dictionary example', fontdict=my_title_font)

plt.show()
