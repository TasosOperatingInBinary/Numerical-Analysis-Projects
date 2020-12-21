from math import ceil
import numpy as np


def bisection(f, a, b, eps=5e-6):
    """
        Function that finds a root using Bisection method for a given function f(x).
        The function finds the root of f(x) with a predefined absolute accuracy epsilon.
        The function excepts an interval [a,b] in which is known that the function f has a root.
        If the function f has multiple roots in this interval then Bisection method converges randomly to one of them.
        If in the interval [a,b] f(x) doesn't change sign (Bolzano theorem can not be applied) the function returns nan
        as root and -1 as the number of iterations.Also the function checks if either a or b is a root of f(x), if both
        are then the function returns the value of a.

        Parameters
        ----------
        f : callable
            The function to find a root of.
        a : float
            The start of the initial interval in which the function will find the root of f(x).
        b : float
            The end of the initial interval in which the function will find the root of f(x).
        eps : float
            The target accuracy.
            The iteration stops when the length of the current interval divided by 2 to the power of n+1 is below eps.
            Default value is 5e-6.

        Returns
        -------
        root : float
            The estimated value for the root.
        iterations_num : int
            The number of iterations.
    """

    # check if Bolzano theorem can not be applied or a is larger than b
    if f(a) * f(b) > 0 or a > b:
        return np.nan, -1
    elif f(a) == 0:  # check if a is root of f
        return a, 0
    elif f(b) == 0:  # or b is root of f
        return b, 0

    # find how many iterations are needed for achieving error less than eps
    iterations_num = ceil((np.log(b - a) - np.log(eps)) / np.log(2))

    # Bisection algorithm
    for i in range(0, iterations_num):
        current_root = (a + b) / 2  # each iteration root approximation is the middle of the current interval
        if f(current_root) == 0:
            return current_root, i+1
        elif f(a) * f(
                current_root) < 0:  # find out where Bolzano theorem still can be applied and update the interval [a,b]
            b = current_root
        else:
            a = current_root

    return current_root, iterations_num
