import numpy as np

# Define a vector V
V = np.array([3, 4])  # This represents a vector (3, 4).

# Calculate the magnitude of V
magnitude_V = np.linalg.norm(V)

# Calculate the unit vector in the same direction as V
unit_vector_V = V / magnitude_V

print("Vector V:", V)
print("Magnitude of V:", magnitude_V)
print("Unit vector in the direction of V:", unit_vector_V)
