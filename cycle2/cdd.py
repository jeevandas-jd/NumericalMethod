import numpy as np

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Function and parameters
f = np.sin
x = np.pi / 4
h = 0.05

# Estimate the derivative
estimated_derivative = central_difference(f, x, h)

# True derivative of sin(x) is cos(x)
true_derivative = np.cos(x)

print(f"Estimated derivative at x=π/4: {estimated_derivative}")
print(f"True derivative at x=π/4: {true_derivative}")
print(f"Error: {abs(estimated_derivative - true_derivative)}")
