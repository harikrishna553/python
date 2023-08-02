import matplotlib.pyplot as plt
import numpy as np

age = [34, 35, 31, 36, 45, 23, 51, 29, 32, 30]
salary = [500000, 450000, 600000, 550000, 300000, 350000, 450000, 432500, 495000, 425000]

plt.scatter(age, salary, label="y = x^2", color='r')

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Scatter Plot Example')

plt.legend()
plt.show()