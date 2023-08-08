import torch

# nn contains all the Nerual Network building blocks of PyTorch
from torch import nn

# To visualize the model
import matplotlib.pyplot as plt


def plot_predictions(train_data, train_labels, test_data, test_labels, predictions=None):
    plt.figure(figsize=(15, 10))

    # plot training data in blue
    plt.scatter(train_data, train_labels, c='b', s=4, label='Training data')

    # plot test data in green
    plt.scatter(test_data, test_labels, c='g', s=4, label='Test data')

    # Plot predictions vs actual values of test data set
    if predictions is not None:
        plt.scatter(test_data, predictions, c='r', s=4, label='predictions')

    # Show the legend
    plt.legend(prop={'size': 14})
    plt.show()


# Build the linear regression model
# Inherit from nn.Module class, nn.Module is the base class for all the Neural Network modules
# We should override forward method
class LinearRegressionModel(nn.Module):
    # constructor
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        self.bias = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))

    # Define the computations performed at each method call
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weight * x + self.bias


# Class to track internal metrics
class Metrics:
    # constructor
    def __init__(self):
        self.run_count = []
        self.weight = []
        self.bias = []
        self.loss = []
        self.test_loss = []

    def to_string(self):
        string = ""
        for key, value in self.__dict__.items():
            string += f"{key}: {value}, "
            string += "'\n"

        return string


# Step 1: Prepare the data using formula (y = mX + c),
weight = 0.5
bias = 0.2
start = 0
end = 1
step = 0.02
X = torch.arange(start, end, step).unsqueeze(dim=1)
Y = weight * X + bias

# Divide the data into two sets
# 1. training set and
# 2. test set
# 80% data is used for training

# Training set
training_set_size = int(0.8 * len(X))
X_training_set = X[:training_set_size]
Y_training_set = Y[:training_set_size]

# Test set
X_test_set = X[training_set_size:]
Y_test_set = Y[training_set_size:]

# Go with random seed to get similar values for our testing on multiple runs
random_seed = 53
torch.manual_seed(random_seed)
first_model = LinearRegressionModel()
print('Initial Model parameters : ', first_model.state_dict())

# Loss function
loss_fn = nn.L1Loss()

# Optimizer to adjust the model parameters
# lr is learning rate, it is a hyperparameter
optimizers = torch.optim.SGD(params=first_model.parameters(), lr=0.01)

# Build a training loop
no_of_times_to_loop = 500
metric_step_count = 30
metric = Metrics()
for counter in range(no_of_times_to_loop):
    # Set the model in training mode
    first_model.train()

    # Forward pass
    Y_training_predictions = first_model(X_training_set)

    # Calculate loss
    loss = loss_fn(Y_training_predictions, Y_training_set)

    # Optimizer zero grad
    optimizers.zero_grad()

    # Perform back propagation with respect to the models
    loss.backward()

    # Step the optimizer
    optimizers.step()

    # Call eval() while testing the model
    # It turns of the various settings in the model that are not needed while evaluating the model
    first_model.eval()
    # Turns off gradient tracking
    with torch.inference_mode():
        # Do the forward pass
        Y_test_predictions = first_model(X_test_set)

        # Calculate the loss
        test_loss = loss_fn(Y_test_predictions, Y_test_set)

    if counter % metric_step_count == 0:
        metric.run_count.append(counter)
        current_model_params_dict = first_model.state_dict()
        metric.weight.append(current_model_params_dict['weight'][0].item())
        metric.bias.append(current_model_params_dict['bias'][0].item())
        metric.loss.append(loss.item())
        metric.test_loss.append(test_loss.item())

    # We can stop training early when the criteria met
    if test_loss < 0.01 and loss < 0.01:
        print(f'Training stopped as the convergence criteria is met at {counter} iteration')
        break

plot_predictions(X_training_set, Y_training_set, X_test_set, Y_test_set, Y_test_predictions)
print(metric.to_string())

print('Initial Model parameters : ', first_model.state_dict())