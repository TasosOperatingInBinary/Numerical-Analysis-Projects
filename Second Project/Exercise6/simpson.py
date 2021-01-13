def simpson_integrate(f, a, b, N, points):
    """
        Computes the integral value from a to b for function f using Simpson method.

        Parameters
        ----------
        f : callable
            The integrating function
        a,b : float
            The min and max value of the integrating interval
        N : int
            Number of partitions.
            <b>Needs to be even.<b>
        points : ndarray
            The partition points

        Returns
        -------
        return_value : float
            The value of the integral from a to b of the function f
    """
    total_sum = 0
    total_sum += f(points[0]) + f(points[N])

    first_sum = 0
    for i in range(1, N // 2):
        first_sum += f(points[2 * i])
    first_sum *= 2
    total_sum += first_sum

    second_sum = 0
    for j in range(1, (N // 2) + 1):
        second_sum += f(points[2 * j - 1])
    second_sum *= 4
    total_sum += second_sum

    interval_length = b - a
    denominator = 3 * N

    return (interval_length / denominator) * total_sum


def simpson_error_bound(a, b, N, M):
    """
        Computes the theoretical error bound when calculating an integral using Simpson method.

        Parameters
        ----------
        a,b : float
            The min and max value of the integrating interval
        N : int
            Number of partitions.
            <b>Needs to be even.<b>
        M : float
            The value of local max on [a,b] of the <b>absolute</b> 4th derivative of function f used in Simpson
            integration

        Returns
        -------
        return_value : float
            The value of theoretical error bound when calculating an integral using Simpson method
    """
    interval_length = b - a
    denominator = 180 * (N ** 4)
    return ((interval_length ** 5) / denominator) * M
