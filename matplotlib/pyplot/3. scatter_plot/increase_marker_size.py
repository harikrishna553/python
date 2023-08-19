import matplotlib.pyplot as plt
import numpy as np

age = [34, 35, 31, 36, 45, 23, 51, 29, 32, 30, 34]
salary = [200000, 450000, 55000, 150000, 550000, 600000, 350000, 450000, 95000, 495000, 425000]
min_value = min(salary)

marker_sizes = [((n/min_value) *50) for n in salary]
plt.scatter(age, salary, label="Employees salaries plot", s=marker_sizes)

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Scatter Plot Example')

plt.legend()
plt.show()