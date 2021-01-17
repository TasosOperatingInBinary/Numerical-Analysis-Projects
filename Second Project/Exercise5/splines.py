import numpy as np
from Exercise5.lu_decomposition import lu


def splines_interpolation(x, y):
    """
        Computes c of the natural cubic spline interpolating the points given.

        Parameters
        ----------
        x : list
            The values of the independent variable. <b>Must be sorted.</b>
        y : list
            The values of f(x) for every x, where x is the independent variable

        Returns
        -------
        c : list
           coefficients of interpolating polynomial
    """
    # create the values for a(i)
    a = []
    d = []
    delta = []
    for i in range(len(x) - 1):
        a.append(y[i])
        d.append(x[i + 1] - x[i])
        delta.append(y[i + 1] - y[i])

    # create the system matrix
    system_matrix = [[0.0 for j in range(len(x))] for i in range(len(x))]
    system_matrix[0][0] = 1
    system_matrix[len(x) - 1][len(x) - 1] = 1
    for row in range(1, len(x) - 1):
        system_matrix[row][row - 1] = d[row - 1]
        system_matrix[row][row] = 2 * (d[row - 1] + d[row])
        system_matrix[row][row + 1] = d[row]

    # create the constant vector of the system
    constant_vector = [0.0 for i in range(len(x))]
    for row in range(1, len(x) - 1):
        constant_vector[row] = 3 * ((delta[row] / d[row]) - (delta[row - 1] / d[row - 1]))

    # solve the system using lu decomposition, c_vector contains the values for c(i)
    c_vector = lu(system_matrix, constant_vector)

    # find the c for b(i) and d(i)
    b = list(d)
    final_d = list(d)
    for i in range(len(x) - 1):
        final_d[i] = (c_vector[i + 1] - c_vector[i]) / (3 * d[i])
        b[i] = (delta[i] / d[i]) - (d[i] / 3) * (2 * c_vector[i] + c_vector[i + 1])

    return a, b, c_vector, final_d


def find_interval_index(array, low, high, search_value):
    """
        Finds the position index that the search_value should be inserted in the array.

        Parameters
        ----------
        array : list
            The array for searching where to insert the search_value. <b>Must be sorted.</b>
        low : int
            The low index of the interval that we are going to search in the array.
        high : int
            The max index of the interval that we are going to search in the array.
        search_value : float
            The value for which we search to find where it should be inserted.

        Returns
        -------
        int
            The index that should be the search_value inserted in the array.
    """
    while low < high:
        mid = int((high+low)//2)
        if array[mid] == search_value:
            break
        elif array[mid] > search_value:
            high = mid - 1
        else:
            low = mid + 1

    mid = int((high+low)//2)
    if search_value <= array[mid]:
        return mid

    return mid + 1


def calculate_polynomial(a, b, c, d, x_values, x):
    """
        Computes the value of the natural cubic spline.

        Parameters
        ----------
        a, b, c, d : list
            The essential c of the natural cubic spline.
        x_values : list
            The values of the independent variable in the data points that were used when calculating the c
            of the natural cubic spline.
        x : int
            The point at which the polynomial will be calculated

        Returns
        -------
        value : float
            The value of the interpolating polynomial at point x.
    """
    i = find_interval_index(x_values, 0, len(x_values)-1, x) - 1
    return a[i] + b[i]*(x-x_values[i]) + c[i]*((x-x_values[i])**2) + d[i]*((x-x_values[i])**3)


def custom_sin(value):
    """
        Approximates sin curve with natural cubic splines.

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
    a, b, c, d = splines_interpolation(x, y)

    value = value % (2*np.pi)
    return calculate_polynomial(a, b, c, d, x, value)
