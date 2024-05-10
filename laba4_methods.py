import numpy as np
import sympy as sp
from sympy import Max, Abs, Pow

x = sp.Symbol('x')
y = sp.Symbol('y')

f = lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

h1 = lambda x, y: (x - 2 * y + 2)
h2 = lambda x, y: (-x - 2 * y + 6)
h3 = lambda x, y: (-x + 2 * y + 2)

g1 = lambda x, y: x - y

x0 = np.array([1.5, 1.5])
r = 2
b = 0.5
eps = 0.001
delta = 0.1

p = 2


def penalty_func(x0, r, b, eps):

    def hooke_jeeves(func, x0, step_size=0.1, max_iter=1000, tolerance=1e-6):

        x = x0.copy()
        f_x = func(x[0], x[1])
        n = len(x)
        
        for i in range(max_iter):
            improved = False
            
            # Поисковый шаг
            for j in range(n):
                x_temp = x.copy()
                x_temp[j] += step_size
                f_temp = func(x_temp[0], x_temp[1])
                
                if f_temp < f_x:
                    x = x_temp.copy()
                    f_x = f_temp
                    improved = True
                else:
                    x_temp[j] -= 2 * step_size
                    f_temp = func(x_temp[0], x_temp[1])
                    
                    if f_temp < f_x:
                        x = x_temp.copy()
                        f_x = f_temp
                        improved = True
            
            # Шаг поиска по образцу
            if improved:
                x_temp = x.copy()
                x_temp += step_size * (x - x0)
                f_temp = func(x_temp[0], x_temp[1])
                
                if f_temp < f_x:
                    x0 = x.copy()
                    x = x_temp.copy()
                    f_x = f_temp
                else:
                    step_size *= 0.5
            else:
                step_size *= 0.5
            
            if step_size < tolerance:
                break
        
        return x

    p = lambda x, y: r * (1 / h1(x, y) + 1 / h2(x, y) + 1 / h3(x, y))
    z = lambda x, y: f(x, y) + p(x, y)

    result = hooke_jeeves(z, x0)

    if abs(p(result[0], result[1])) < eps:
        return result
    
    else:
        while True:
            r *= b
            p = lambda x, y: r * (1 / h1(x, y) + 1 / h2(x, y) + 1 / h3(x, y))
            z = lambda x, y: f(x, y) + p(x, y)
            result = hooke_jeeves(z, x0)
            if abs(p(result[0], result[1])) < eps:
                return result


answ = penalty_func(x0, r, b, eps)
print(answ)


def barrier_func(x0, r, b, eps, p):

    def hooke_jeeves(func, x0, step_size=0.1, max_iter=1000, tolerance=1e-6):

        x = x0.copy()
        f_x = func(x[0], x[1])
        n = len(x)
        
        for i in range(max_iter):
            improved = False
            
            # Поисковый шаг
            for j in range(n):
                x_temp = x.copy()
                x_temp[j] += step_size
                f_temp = func(x_temp[0], x_temp[1])
                
                if f_temp < f_x:
                    x = x_temp.copy()
                    f_x = f_temp
                    improved = True
                else:
                    x_temp[j] -= 2 * step_size
                    f_temp = func(x_temp[0], x_temp[1])
                    
                    if f_temp < f_x:
                        x = x_temp.copy()
                        f_x = f_temp
                        improved = True
            
            # Шаг поиска по образцу
            if improved:
                x_temp = x.copy()
                x_temp += step_size * (x - x0)
                f_temp = func(x_temp[0], x_temp[1])
                
                if f_temp < f_x:
                    x0 = x.copy()
                    x = x_temp.copy()
                    f_x = f_temp
                else:
                    step_size *= 0.5
            else:
                step_size *= 0.5
            
            if step_size < tolerance:
                break
        
        return x
    
    p = lambda x, y: r *(Pow((Max(0, -h1(x, y))), p) + Pow((Max(0, -h2(x, y))), p) + Pow(Max(0, -h3(x, y)), p) + Pow(Abs(g1(x, y)), p))
    z = lambda x, y: f(x, y) + p(x, y)

    result = hooke_jeeves(z, x0)

    if abs(p(result[0], result[1])) < eps:
        return result
    
    else:
        r *= b
        p = lambda x, y: r *(Pow((Max(0, -h1(x, y))), p) + Pow((Max(0, -h2(x, y))), p) + Pow(Max(0, -h3(x, y)), p) + Pow(Abs(g1(x, y)), p))
        z = lambda x, y: f(x, y) + p(x, y)
        result = hooke_jeeves(z, x0)
        if abs(p(result[0], result[1])) < eps:
            return result

answ = barrier_func(x0, r, b, eps, p)
print(answ)