import numpy as np
from bisection import bisection
from newton_raphson import newton_raphson
from secant import secant


def g(x):
    # return np.sin(x) +(x**2)*np.cos(x) - x**2 -x
    return np.e ** ((np.sin(x)) ** 3) + x ** 6 - 2 * (x ** 4) - x ** 3 - 1


def g_second_der(x):
    h = 0.001
    return (gprime(x + h) - gprime(x)) / h


def find_x0(a, b, g, g_second_der):
    for i in np.arange(a, b, 0.01):
        if g(i) * g_second_der(i) > 0:
            return i

    print("could not find x0")
    return (a + b) / 2


def gprime(x):
    # return np.cos(x) +2*x*np.cos(x) +(x**2)*(-np.sin(x)) -2*x -1
    return 3 * (np.e ** ((np.sin(x)) ** 3)) * ((np.sin(x)) ** 2) * np.cos(x) + 6 * (x ** 5) - 8 * (x ** 3) - 3 * (
            x ** 2)


def bisection_iterations():
    iterations_per_interval = []
    root_per_interval = []

    num_of_calls = 0
    for i in np.arange(-1.0, 1.0, 0.008): # for first root -> np.arange(-2.0, -0.1, 0.008):
                                         # for third root -> np.arange(0.1, 2.0, 0.008):
        if num_of_calls >= 10000:
            break
        for j in np.arange(1.0, i, -0.008): # for first root -> np.arange(-0.1, i, -0.008)
                                            # for third root -> np.arange(2.0, i, -0.008)
            if num_of_calls >= 10000:
                break
                #return root_per_interval, iterations_per_interval, num_of_calls
            if g(i) * g(j) < 0:
            current_root, current_iterations = bisection(g, i, j)
            num_of_calls = num_of_calls + 1
            root_per_interval.append(current_root)
            iterations_per_interval.append(current_iterations)

    while np.nan in root_per_interval: root_per_interval.remove(np.nan)
    while -1 in iterations_per_interval: iterations_per_interval.remove(-1)
    return root_per_interval, iterations_per_interval, num_of_calls


def newton_iterations():
    iterations_per_interval = []
    root_per_interval = []
    num_of_calls = 0
    for i in np.arange(1.251, 2, 0.003): # for first root -> np.arange(-2.0, -0.9684, 0.003)
        if num_of_calls >= 10000:
            break
        for j in np.arange(2, i, -0.003): # for first root -> np.arange(-0.9684, i, -0.003)
            if num_of_calls >= 10000:
                break
                #return root_per_interval, iterations_per_interval, num_of_calls
            if g(i) * g(j) < 0:
                current_root, current_iterations = newton_raphson(g, gprime, find_x0(i, j, g, g_second_der))
                num_of_calls += 1
                root_per_interval.append(current_root)
                iterations_per_interval.append(current_iterations)

    while np.nan in root_per_interval: root_per_interval.remove(np.nan)
    while -1 in iterations_per_interval: iterations_per_interval.remove(-1)
    return root_per_interval, iterations_per_interval, num_of_calls


def secant_iterations():
    iterations_per_interval = []
    root_per_interval = []
    num_of_calls = 0
    for i in np.arange(1.251, 2, 0.003): # for first root -> np.arange(-2.0, -0.9684, 0.003)
        if num_of_calls >= 10000:
            break
        for j in np.arange(2, i, -0.003): # for first root -> np.arange(-0.9684, i, -0.003)
            if num_of_calls >= 10000:
                break
                #return root_per_interval, iterations_per_interval, num_of_calls
            if g(i) * g(j) < 0:
                current_root, current_iterations = secant(g, i, j)
                num_of_calls += 1
                root_per_interval.append(current_root)
                iterations_per_interval.append(current_iterations)

    while np.nan in root_per_interval: root_per_interval.remove(np.nan)
    while -1 in iterations_per_interval: iterations_per_interval.remove(-1)
    return root_per_interval, iterations_per_interval, num_of_calls