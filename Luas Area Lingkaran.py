import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_circle_area(radius, num_points):
    points_inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_points):
        # Generate random point (x, y) within the square
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)

        # Check if the point is inside the circle
        if x**2 + y**2 <= radius**2:
            points_inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # Area of the square is (2*radius)^2, and the ratio of points inside the circle
    # to total points gives us the ratio of the circle's area to the square's area.
    square_area = (2 * radius) ** 2
    circle_area = (points_inside_circle / num_points) * square_area

    return circle_area, x_inside, y_inside, x_outside, y_outside

# Parameters
radius = 1  # Radius of the circle
num_points = 10000  # Number of random points

# Calculate the area using Monte Carlo method
estimated_area, x_inside, y_inside, x_outside, y_outside = monte_carlo_circle_area(radius, num_points)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-radius, radius)
ax.set_ylim(-radius, radius)
ax.set_aspect('equal')
ax.set_title(f'Monte Carlo Simulation: Estimated Area = {estimated_area:.4f}')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Plot all points
ax.scatter(x_inside, y_inside, color='blue', s=10, label='Inside Circle')
ax.scatter(x_outside, y_outside, color='red', s=10, label='Outside Circle')
ax.legend()

plt.show()