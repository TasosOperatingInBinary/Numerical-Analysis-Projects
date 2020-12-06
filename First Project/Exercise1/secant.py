
def secant(f, x0, x1, eps=5e-6, max_iterations=50):
    """
    Function that finds a root using Secant method for a given function f(x). The function finds the root of f(x)
    with a predefined absolute accuracy epsilon. The function excepts two starting points x0,x1 that belong to an
    interval [a,b] in which is known that f has a root. If the function f has multiple roots in this interval then
    Secant method converges randomly to one of them. If in the interval [a,b] f(x) doesn't change sign (Bolzano
    theorem can not be applied) the function has unpredictable behavior and will execute max_iterations iterations
    and converge to a false result or converge to a partial correct root with less than max_iterations number of
    iterations but not with the predefined accuracy. Also the function checks if either x0 or x1 is a root of f(x), if
    both are then the function returns the value of x0.

        Parameters
        ----------
        f : callable
            The function to find a root of.
        x0 : float
            The first point for secant method.
        x1: float
            The second point for secant method.
        eps : float
            The target accuracy.
            The iteration stops when the distance between successive iterates is below eps.
            Default value is 5e-6.
        max_iterations : int
            The maximum number of iterations.
            The function terminates if the number of iterations exceeds the max_iterations value.
            The parameter is used to avoid infinite loops.
            Default value is 50.

        Returns
        -------
        root : float
            The estimated value for the root.
        iterations_num : int
            The number of iterations.
    """

    if f(x0) == 0:  # check if x0 is root of f
        return x0, 0
    elif f(x1) == 0:  # or x1 is root of f
        return x1, 0

    # initializations, create variables according to n, with n >= 1
    x_n_minus_1 = x0
    x_n = x1
    x_n_plus_1 = x_n - ((f(x_n) * (x_n - x_n_minus_1)) / (f(x_n) - f(x_n_minus_1)))
    iterations_num = 0

    # Secant method algorithm
    # iterate while the error is larger that predefined argument eps or we have more iterations to do until
    # max_iterations
    while abs(x_n_plus_1 - x_n) >= eps and iterations_num < max_iterations:
        # on each step update variables x according to n and also increase iterations_num
        x_n_minus_1 = x_n
        x_n = x_n_plus_1
        x_n_plus_1 = x_n - ((f(x_n) * (x_n - x_n_minus_1)) / (f(x_n) - f(x_n_minus_1)))
        iterations_num += 1

    return x_n_plus_1, iterations_num
