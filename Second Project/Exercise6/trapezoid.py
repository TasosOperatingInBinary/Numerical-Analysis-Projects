def trapezoid_integrate(f, a, b, N, points):
    """
        Computes the integral value from a to b for function f using Trapezoid method.

        Parameters
        ----------
        f : callable
            The integrating function
        a,b : float
            The min and max value of the integrating interval
        N : int
            Number of partitions.
        points : ndarray
            The partition points

        Returns
        -------
        return_value : float
            The value of the integral from a to b of the function f
    """
    total_sum = 0
    total_sum += f(points[0]) + f(points[N])

    first_sum = 0.0
    for i in range(1, N):
        first_sum += f([points[i]])
    first_sum *= 2
    total_sum += float(first_sum)

    interval_length = b - a
    denominator = 2 * N

    return (interval_length / denominator) * total_sum


def trapezoid_error_bound(a, b, N, M):
    """
        Computes the theoretical error bound when calculating an integral using Trapezoid method.

        Parameters
        ----------
        a,b : float
            The min and max value of the integrating interval
        N : int
            Number of partitions.
        M : float
            The value of local max on [a,b] of the <b>absolute</b> 2nd derivative of function f used in Trapezoid
            integration

        Returns
        -------
        return_value : float
            The value of theoretical error bound when calculating an integral using Trapezoid method
    """
    interval_length = b - a
    denominator = 12 * (N ** 2)
    return ((interval_length**3)/denominator)*M
