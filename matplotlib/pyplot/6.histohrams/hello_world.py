import pandas as pd
import matplotlib.pyplot as plt

students_percentage = [71, 25, 34, 95, 45,  81, 76, 45, 31, 65, 89, 56, 78, 45, 56, 90, 32, 24, 46, 69]
plt.hist(students_percentage)

plt.xlabel('Percentage')
plt.ylabel('Count of students')

plt.title('Students percentage histogram')
plt.show()
