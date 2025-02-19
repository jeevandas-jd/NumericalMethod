import math
def forward_difference(f,x,h=1e-5):
    return (f(x + h) - f(x)) / h


if __name__ == "__main__":

    def f(x):
        return  math.exp(x)


    x0 = 2
    derivative = forward_difference(f, x0)

    print(f"Approximate derivative of f(x) = x^2 at x = {x0} is {derivative}")
