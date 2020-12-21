import matplotlib.pyplot as plt
import numpy as np
from Exercise1.newton_raphson import newton_raphson
from Exercise1.bisection import bisection
from Exercise1.secant import secant
from Exercise1.mult_newton_raphson import mult_newton_raphson
from Exercise1.iterations_comparison import bisection_iterations, newton_iterations, secant_iterations


def g(x):
    return np.e ** ((np.sin(x)) ** 3) + x ** 6 - 2 * (x ** 4) - x ** 3 - 1


def gprime(x):
    return 3 * (np.e ** ((np.sin(x)) ** 3)) * ((np.sin(x)) ** 2) * np.cos(x) + 6 * (x ** 5) - 8 * (x ** 3) - 3 * (
           x ** 2)


def g_second_der(x):
    # return 3 * np.cos(x) * (216 * np.cos(x) ** 2 - 432 * np.cos(x)) * np.sin(x) ** 2 + np.sin(x) * (
    #        576 * np.cos(x) ** 3 * np.sin(x) + 564 * np.cos(x) * np.sin(x)
    #        - 354 * np.sin(x)) + np.sin(x) ** 3 * (432 * np.sin(x) - 432 * np.cos(x) * np.sin(x)) \
    #       + np.cos(x) * (-144 * np.cos(x) ** 4 - 282 * np.cos(x) ** 2 + 354 * np.cos(x) + 24)
    h = 0.001
    return (gprime(x + h) - gprime(x)) / h


def main():
    # sub question a
    print("Bisection")

    root, iterations = bisection(g, -1.5, -1.0)
    print("root = "+str(root))
    print("iterations ="+str(iterations))

    root, iterations = bisection(g, 1.25, 1.75)
    print("root = "+str(root))
    print("iterations ="+str(iterations))

    root, iterations = bisection(g, -0.05, 0.05)
    print("root = "+str(root))
    print("iterations ="+str(iterations))

    root, iterations = bisection(g, -0.5, 0.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = bisection(g, 0, 1)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = bisection(g, -1.5, 1.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    print()
    print("Newton-Raphson")

    root, iterations = newton_raphson(g, gprime, -1.4)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = newton_raphson(g, gprime, 1.7)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = newton_raphson(g, gprime, 0.25)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = newton_raphson(g, gprime, 0.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = newton_raphson(g, gprime, -0.25)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = newton_raphson(g, gprime, -0.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = newton_raphson(g, gprime, 0)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    print()
    print("Secant")

    root, iterations = secant(g, -1.5, -1.0)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = secant(g, 1.3, 1.9)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = secant(g, -0.25, 0.25)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = secant(g, -0.5, 0.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))

    root, iterations = secant(g, 0, 1.5)
    print("root = " + str(root))
    print("iterations =" + str(iterations))


main()
