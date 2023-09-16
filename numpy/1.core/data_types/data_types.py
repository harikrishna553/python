import numpy as np

# Get a dictionary of NumPy data types categorized by type
all_data_types = np.sctypes

# Print the list of all NumPy data types
for data_type_category, data_types in all_data_types.items():
    print(f"{data_type_category} data types:")
    for data_type in data_types:
        print(f"- {data_type.__name__}")
