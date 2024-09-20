import random
import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 0.0  # Lower limit of integration
b = 3.0  # Upper limit of integration
num_steps = 1000000  # Number of random points
seed = 2  # Seed for reproducibility

# Initialize the PRNG with a specific seed
random.seed(seed)

# Define the function f(x) = x^2
def f(x):
    return x ** 2

# Generate random x points and compute corresponding y points
x_points = [random.uniform(a, b) for _ in range(num_steps)]
y_points = [f(x) for x in x_points]

# Calculate the area under the curve using Monte Carlo integration
# The area of the rectangle is (b - a) * max(f(x))
max_y = max(y_points)
rectangle_area = (b - a) * max_y
average_y = sum(y_points) / num_steps
integral_estimate = (b - a) * average_y

print(f"Estimated integral: {integral_estimate:.4f}")

# Initialize lists for plotting
x_plot = np.linspace(a, b, 100)
y_plot = f(x_plot)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the function f(x) = x^2
ax.plot(x_plot, y_plot, color='blue', label='$f(x) = x^2$')

# Plot the random points
ax.scatter(x_points, y_points, color='red', s=1, alpha=0.2, label='Random Points')

# Set labels, title, and legend
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Monte Carlo Integration of $f(x) = x^2$')
ax.legend()

# Display the plot
plt.show()