import numpy as np
from Exercise5.lu_decomposition import lu


def splines_interpolation(x, y):
    """
        Computes coefficients of the natural cubic spline interpolating the points given.

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
    a = []
    d = []
    delta = []
    for i in range(len(x)-1):
        a.append(y[i])
        d.append(x[i+1]-x[i])
        delta.append(y[i+1]-y[i])

    print("a = " + str(a))
    print("d = " + str(d))
    print("delta = " + str(delta))
