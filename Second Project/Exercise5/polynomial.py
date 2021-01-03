import numpy as np


def polynomial_interpolation(x, y):
    """
        Computes coefficients of interpolating polynomial using Newton method.

        Parameters
        ----------
        x : ndarray
            The values of the independent variable
        y : list
            The values of f(x) for every x, where x is the independent variable

        Returns
        -------
        c : list
            coefficients c of interpolating polynomial
    """
    v = []
    [v.append([0 for j in range(len(x))]) for i in range(len(x))]
    for j in range(len(x)):
        v[j][0] = y[j]

    for i in range(1, len(x)):
        for j in range(len(x) - i):
            v[j][i] = (v[j + 1][i - 1] - v[j][i - 1]) / (x[j + i] - x[j])

    c = []
    for i in range(len(x)):
        c.append(v[0][i])

    return c


def calculate_polynomial(degree, x_data, coefficients, x):
    """
        Computes the value of the interpolating polynomial.

        Parameters
        ----------
        degree : int
            The degree of the interpolating polynomial.
        x_data : list
            The values that were used when calculating the coefficients of the interpolating polynomial.
        coefficients : list
            The coefficents of the interpolating polynomial, constant term first.
        x : int
            The point at which the polynomial will be calculated

        Returns
        -------
        value : float
            The value of the interpolating polynomial at point x.
    """
    value = 0.0
    for i in range(degree + 1):
        temp = coefficients[i]
        for j in range(i):
            temp *= (x - x_data[j])
        value += temp

    return value


def custom_sin(value):
    """
        Approximates sin curve with degree 9 polynomial.

        Parameters
        ----------
        value : float
            The point at which the sin will be approximated

        Returns
        -------
        float
            The approximation value of the sin curve at point x.
    """
    x = [0.0, 0.65, 1.3, 1.9500000000000002, 2.6, 3.25, 3.9000000000000004, 4.55, 5.2, 2*np.pi]
    y = [0.0, 0.6051864057, 0.9635581854, 0.9289597150, 0.5155013718, -0.1081951345, -0.6877661591, -0.9868438585,
         -0.8834546557, 0]
    c = polynomial_interpolation(x, y)
    value = value % (2 * np.pi)

    return calculate_polynomial(len(x) - 1, x, c, value)
