import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)

num_samples = 10000
cpu_usage = np.random.randint(0, 101, num_samples)
memory_usage = np.random.randint(0, 101, num_samples)
disk_usage = np.random.randint(0, 101, num_samples)
network_latency = np.random.randint(1, 21, num_samples)

system_state= []

for index in range(len(cpu_usage)):
    cpu = cpu_usage[index]
    memory = memory_usage[index]
    disk = disk_usage[index]
    latency = network_latency[index]

    if cpu > 80 | memory > 80 | disk > 80 | latency > 10:
        state = 'bad'
    elif cpu > 50 & memory > 85:
        state = 'bad'
    elif disk > 80 & memory > 85:
        state = 'bad'
    else:
        state = 'good'

    system_state.append(state)

application_state = np.array(system_state)

# Create a DataFrame
data = pd.DataFrame({
    'cpu_usage': cpu_usage,
    'memory_usage': memory_usage,
    'disk_usage': disk_usage,
    'network_latency': network_latency,
    'application_state': application_state
})

# Save data to CSV file
data.to_csv('system_metrics_data.csv', index=False)

# Display the first few rows of the generated data
print(data.head())
