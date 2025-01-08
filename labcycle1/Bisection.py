import sympy as sp
def Bisection(f,a,b):
    if f(a)*f(b)>=0:
        raise ValueError("Function values at the endpoints must have opposite signs.")
    while (b-a)/2 > 1e-6:
        c=(a+b)/2
        if f(c)==0:
            return c
        if f(a)*f(b)<0:
            b=c
        else:
            a=c
    return (a+b)/2

func_str = input("Enter the function in terms of x (e.g., x**3 - x - 2): ")
a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))
tol = float(input("Enter the tolerance (e.g., 1e-6): "))

x = sp.Symbol('x')
func_expr = sp.sympify(func_str)
f = sp.lambdify(x, func_expr)  # Convert symbolic expression to a Python function

# Call the bisection method
try:
    root = Bisection(f, a, b)
    print(f"Root: {root}")
except ValueError as e:
    print(e)