import numpy as np
from Exercise5.util import matrix_mult, transpose, matrix_vector_mult
from Exercise5.lu_decomposition import lu


def least_squares_fit(x, y, degree=10):
    """
        Computes the coefficients of the 5th degree polynomial of the least squares fit. <br>Constant term first.</br>

        Parameters
        ----------
        x : list
            The values of the independent variable. <b>Must be sorted.</b>
        y : list
            The values of f(x) for every x, where x is the independent variable
        degree : int
            The degree of the polynomial model fitting the data.

        Returns
        -------
        c : list
            c c of interpolating polynomial
    """
    # construct A
    a = []
    for row in range(len(x)):
        a.append([])
        for column in range(degree):
            a[row].append(x[row]**column)
    # construct A^T * A
    a_transpose = transpose(a)
    a_transpose_a = matrix_mult(a_transpose, a)

    # solve (A^T * A) * x = A^T * y
    return lu(a_transpose_a, matrix_vector_mult(a_transpose, y))


def calculate_polynomial(c, x, degree=10):
    """
        Computes the value of the 5th degree least squares fit polynomial.

        Parameters
        ----------
        c : list
            The coefficients of the 5th degree polynomial. <b>Constant term first.</br>
        x : int
            The point at which the polynomial will be calculated
        degree : int
            The degree of the polynomial model that was used when fitting the data.

        Returns
        -------
        return_value : float
            The value of the interpolating polynomial at point x.
    """
    return_value = 0.0
    for i in range(degree):
        return_value += c[i] * (x ** i)
    return return_value


def custom_sin(value, d=10):
    """
        Approximates sin curve with least squares using 5th degree polynomial model.

        Parameters
        ----------
        value : float
            The point at which the sin will be approximated
        d : int
            The degree of the polynomial model fitting the data.

        Returns
        -------
        float
            The approximation value of the sin curve at point x.
    """
    x = [0.0, 0.65, 1.3, 1.9500000000000002, 2.6, 3.25, 3.9000000000000004, 4.55, 5.2, 2*np.pi]
    y = [0.0, 0.6051864057, 0.9635581854, 0.9289597150, 0.5155013718, -0.1081951345, -0.6877661591, -0.9868438585,
         -0.8834546557, 0]
    c = least_squares_fit(x, y, degree=d)

    value = value % (2*np.pi)
    return calculate_polynomial(c, value, degree=d)
