import torch
import matplotlib.pyplot as plt

# Set the image dimensions
image_height = 200
image_width = 400
channels = 3 # Represent RGB color coding

# Generate a random tensor of shape (channels, image_height, image_width)
random_tensor = torch.rand(channels, image_height, image_width)

# Display the random tensor as an image
plt.imshow(random_tensor.permute(1, 2, 0))
plt.axis('off')
plt.show()
