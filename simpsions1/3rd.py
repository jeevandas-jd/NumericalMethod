
import sympy as sp
fun = input("Enter function in terms of x: ")
a, b = map(float, input("Enter limits (a b): ").split())
h = int(input("Enter step size: "))
x=sp.symbols('x')
f=sp.sympify(fun)

n=int((b-a)/2)

if n % 2 != 0:
    print("n must be even for Simpson's 1/3 rule")
    exit()
result = f.subs(x, a) + f.subs(x, b)

for i in range(1, n):
    xi = a + i * h
    if i%2 ==0:
        coeff=2
    else:
        coeff=4

    result += coeff * f.subs(x, xi)