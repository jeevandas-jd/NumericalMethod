import numpy as np

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

# Function and parameters
f = np.sin
x = np.pi / 4
h = 0.05

# Estimate the first derivative
estimated_derivative = central_difference(f, x, h)

# Estimate the second derivative
estimated_second_derivative = second_derivative(f, x, h)

# True derivatives
true_derivative = np.cos(x)
true_second_derivative = -np.sin(x)

print(f"Estimated first derivative at x=π/4: {estimated_derivative}")
print(f"True first derivative at x=π/4: {true_derivative}")
print(f"Error in first derivative: {abs(estimated_derivative - true_derivative)}")

print(f"Estimated second derivative at x=π/4: {estimated_second_derivative}")
print(f"True second derivative at x=π/4: {true_second_derivative}")
print(f"Error in second derivative: {abs(estimated_second_derivative - true_second_derivative)}")
