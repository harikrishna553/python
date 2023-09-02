import numpy as np

data = np.array([1, 10, 100, 1000, 10000, 100000, 1000000])

# Perform natural logarithm (base e) transformation
log_transformed_data = np.log(data)

# Perform base 10 logarithm transformation
log10_transformed_data = np.log10(data)

print("Original Data:")
print(data)

print("\nNatural Logarithm Transformation:")
print(log_transformed_data)

print("\nBase 10 Logarithm Transformation:")
print(log10_transformed_data)
