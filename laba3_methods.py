import numpy as np
from scipy.optimize import minimize

def func(x):
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

h1 = lambda x: (x[0] - 2 * x[1] + 2)
h2 = lambda x: (-x[0] - 2 * x[1] + 6)
h3 = lambda x: (-x[0] + 2 * x[1] + 2)

x0 = np.array([2.3, 5])
i = 1
r = 1
b = 0.2
eps = 0.01

def penalty_func(x0, h1, h2, h3, i, r, b, eps):
    curr_func = lambda x: func(x)
    while i < 1000:
        if curr_func(x0) < eps:
            break
        curr_func = lambda x: func(x) + r*(1.0/(h1(x)**2 + h2(x)**2 + h3(x)**2))
        x0 = minimize(curr_func, x0).x;
        i += 1
        r *= b

    return x0, func(x0)

print(penalty_func(x0, h1, h2, h3, i, r, b, eps))
    