# TODO ADD DESCRIPTION IN .TEX FOR WHEN METHOD DOES NOT CONVERGE FROM THE PAPERS IN CHROME BOOKMARKS
def modified_newton_raphson(f, fprime, f_second_der, x0, eps=5e-6, max_iterations=50):
    """
        Function that finds a root using a modified Newton's iteration for a given function f(x) with known derivative
        f'(x) and second derivative f''(x).
        The function finds the root of f(x) with a predefined absolute accuracy epsilon. The function excepts a
        starting point x0 that belongs to an interval [a,b] in which is known that f has a root.If the function f has
        multiple roots in this interval then Newton's method converges randomly to one of them.If in the interval [a,b]
        f(x) doesn't change sign (Bolzano theorem can not be applied) the function has unpredictable behavior and will
        execute max_iterations iterations and converge to a false result or converge to a partial correct root with less
        than max_iterations number of iterations but not with the predefined accuracy. Also the function checks if x0 is
        a root of f(x) and if it is then the function returns the value of x0.

        Parameters
        ----------
        f : callable
            The function to find a root of.
        fprime : callable
            The derivative of function f(x).
        f_second_der : callable
            The second derivative of function f(x).
        x0 : float
            The initial value for the Newton's iteration.
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

    # initializations
    current_x = x0 - f(x0) / fprime(x0) - 0.5 * (((f(x0) ** 2) * f_second_der(x0)) / (fprime(x0) ** 3))
    previous_x = x0
    iterations_num = 0

    # Modified Newton's method algorithm
    # iterate while the error is larger that predefined argument eps or we have more iterations to do until
    # max_iterations
    while abs(current_x - previous_x) >= eps and iterations_num < max_iterations:
        # on each step update variables x and also increase iterations_num
        previous_x = current_x
        current_x = current_x - f(current_x) / fprime(current_x) - 0.5 * ((f(current_x) ** 2) *
                                                                          f_second_der(current_x)) / (fprime(current_x)
                                                                                                      ** 3)
        iterations_num += 1

    return current_x, iterations_num
