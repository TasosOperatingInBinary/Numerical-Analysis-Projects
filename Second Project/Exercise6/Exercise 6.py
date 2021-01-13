import numpy as np
from simpson import simpson_integrate, simpson_error_bound
from trapezoid import trapezoid_integrate, trapezoid_error_bound


def f(x):
    return np.sin(x)


def main():
    points = np.linspace(0.0, np.pi/2, 11)

    print("Simpson integration result = "+str(simpson_integrate(f, 0.0, np.pi/2, 10, points)))
    print("Simpson integration error = "+str(abs(simpson_integrate(f, 0.0, np.pi/2, 10, points)-1.0)))
    print("Simpson theoretical error bound = "+str(simpson_error_bound(0.0, np.pi/2, 10, 1)))
    print()
    print("Trapezoid integration result = "+str(trapezoid_integrate(f, 0.0, np.pi/2, 10, points)))
    print("Trapezoid integration error = "+str(abs(trapezoid_integrate(f, 0.0, np.pi/2, 10, points)-1.0)))
    print("Trapezoid theoretical error bound = "+str(trapezoid_error_bound(0.0, np.pi/2, 10, 1)))


main()
