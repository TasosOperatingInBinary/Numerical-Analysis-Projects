import numpy as np
from Exercise2.modified_secant import modified_secant
from Exercise2.modified_newton_raphson import modified_newton_raphson
from Exercise1.newton_raphson import newton_raphson
from Exercise1 import iterations_comparison
from Exercise1.secant import secant
import matplotlib.pyplot as plt
from Exercise1.bisection import bisection
from Exercise2.modified_bisection import modified_bisection
import time


def find_x0(a, b, g, g_second_der):
    for i in np.arange(a, b, 0.01):
        if g(i) * g_second_der(i) > 0:
            return i

    print("could not find x0")
    return (a + b) / 2


def f(x):
    return 94 * (np.cos(x) ** 3) - 24 * np.cos(x) + 177 * (np.sin(x) ** 2) - 108 * (np.sin(x) ** 4) - 72 * (
            np.cos(x) ** 3) * (np.sin(x) ** 2) \
           - 65


def fprime(x):
    return -282 * (np.cos(x) ** 2) * np.sin(x) + 24 * np.sin(x) + 177 * np.sin(2 * x) - 432 * (np.sin(x) ** 3) * np.cos(
        x) + 216 * \
           (np.cos(x) ** 2) * (np.sin(x) ** 3) - 72 * (np.cos(x) ** 3) * (np.sin(2 * x))


def f_second_der(x):
    # return 3 * np.cos(x) * (216 * np.cos(x) ** 2 - 432 * np.cos(x)) * np.sin(x) ** 2 + np.sin(x) * (
    #        576 * np.cos(x) ** 3 * np.sin(x) + 564 * np.cos(x) * np.sin(x)
    #        - 354 * np.sin(x)) + np.sin(x) ** 3 * (432 * np.sin(x) - 432 * np.cos(x) * np.sin(x)) \
    #       + np.cos(x) * (-144 * np.cos(x) ** 4 - 282 * np.cos(x) ** 2 + 354 * np.cos(x) + 24)
    h = 0.001
    return (fprime(x + h) - fprime(x)) / h


def main():
    print("Modified Newton-Raphson")
    root, iterations = modified_newton_raphson(f, fprime, f_second_der, 0.5)
    print("root = "+str(root))
    print("iterations ="+str(iterations))

    root, iterations = modified_newton_raphson(f, fprime, f_second_der, 2.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = modified_newton_raphson(f, fprime, f_second_der, 1.4)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    print()
    print("Modified Bisection")

    root, iterations = modified_bisection(f, 0.5, 1.0)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = modified_bisection(f, 1.0, 1.25)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = modified_bisection(f, 2.0, 2.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    print()
    print("Modified Secant")

    root, iterations = modified_secant(f, 0.0, 0.5, 0.75)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = modified_secant(f, 1.5, 1.8, 2.3)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = modified_secant(f, 0.9, 1.1, 1.2)
    print("root = " + str(root))
    print("iterations =" + str(iterations))


main()
