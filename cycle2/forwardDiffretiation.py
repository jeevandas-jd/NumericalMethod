
def forward_difference(f,x,h=1e-5):
    return (f(x + h) - f(x)) / h


if __name__ == "__main__":

    def f(x):
        return x ** 3+(2*x)**2-5*x+7


    x0 = 2
    derivative = forward_difference(f, x0)

    print(f"Approximate derivative of f(x) = x^2 at x = {x0} is {derivative}")
