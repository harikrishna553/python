import pandas as pd
import matplotlib.pyplot as plt
import random

def random_hex_color():
    # Generate random values for red, green, and blue components
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Convert the values to hexadecimal and format the color string
    color_string = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    print(color_string)
    return color_string

students_percentage = [71, 25, 34, 95, 45,  81, 76, 45, 31, 65, 89, 56, 78, 45, 56, 90, 32, 24, 46, 69]
n, bins, patches = plt.hist(students_percentage, edgecolor='white', linewidth=1)

# Add frequency annotations to the histogram bars
for i in range(len(n)):
    patches[i].set_facecolor(random_hex_color())
    plt.annotate(f'Freq: {int(n[i])}', xy=(bins[i] + (bins[i + 1] - bins[i]) / 2, n[i]),
                 xytext=(0, 3), textcoords='offset points', ha='center', fontsize=8, color='black')

plt.xlabel('Percentage')
plt.ylabel('Count of students')

plt.title('Students percentage histogram')
plt.show()