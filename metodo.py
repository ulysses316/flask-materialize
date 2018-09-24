import math
def f(x):
    return math.exp(x) - (3*x)

def biseccion(xi, xs, tolerancia, iteraciones):
    if (xi > xs):
        return biseccion(xs, xi, tolerancia, iteraciones)
    iter=0
    c=(xi+xs) * (0.5)
    while (abs(f(c)) > tolerancia and iter < iteraciones):
        if (f(xi) * f(c) < 0):
            xs = c
        if (f(c) * f(xs) < 0):
            xi = c
        c = (xi+xs) * (0.5)
        iter = iter + 1
    return c
