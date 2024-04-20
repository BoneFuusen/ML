import sympy as sp
import numpy as np

def la_cringe():
    x, y, lambd = sp.symbols('x y λ')
    f = x**2 + y**2
    g = x + y - 1

    L = f + lambd * g
    grad_L = [sp.diff(L, var) for var in (x, y, lambd)]
    solution = sp.solve(grad_L, (x, y, lambd))

    print(solution)

def rosen():
    def rosen_projection(x0, f, g, c, epsilon=1e-6, max_iter=1000, penalty_coefficient=1e-4):
        x = x0
        for i in range(max_iter):
            f_val = f(x)
            g_val = g(x)
            c_val = c(x)

            if np.linalg.norm(c_val) < epsilon:
                return x

            penalty = (penalty_coefficient * np.sum(np.maximum(0, c_val) ** 2))

            f_penalized = lambda x: f(x) + penalty
            g_penalized = lambda x: g(x) + 2 * penalty * np.sum(c_val * g(x))

            x_new = x - g_penalized(x) / np.linalg.norm(g_penalized(x))

            if np.linalg.norm(x_new - x) < epsilon:
                return x_new

            x = x_new

        return x

    # Пример применения алгоритма

    # Функция f(x)
    def f(x):
        return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2

    # Градиент функции f(x)
    def g(x):
        return np.array([-2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0] ** 2), 200 * (x[1] - x[0] ** 2)])

    # Ограничения условной оптимизации
    def c(x):
        return np.array([x[0] ** 2 + x[1] ** 2 - 1])

    # Начальное приближение
    x0 = np.array([0, 0])

    # Вызов функции для решения задачи
    result = rosen_projection(x0, f, g, c)

    print("Минимум функции f(x) =", f(result))
    print("Решение x =", result)
