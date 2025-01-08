a=lambda a:a*3+a**2
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

f=lambda x:x**3-x-2

root=Bisection(f,5,5)

print(f"root {root}")