from Exercise3.util import matrix_vector_mult, vector_magnitude


def power_method(matrix):
    """
        Function that calculates the dominant eigenvalue and the dominant eigenvector of the provided matrix using
        Power Method

        Parameters
        ----------
        matrix : a list of lists
            The matrix whose dominant eigenvalue and eigenvector will be calculated

        Returns
        -------
        eigenvalue : float
            The dominant eigenvalue of the provided matrix
        eigenvector : list
            The vector that corresponds to the dominant eigenvalue of the provided matrix, normalized so its magnitude
            is equal to 1
    """
    u = [1.0 for i in range(len(matrix))]
    for i in range(len(matrix)):
        w = matrix_vector_mult(matrix, u)
        eigenvalue = vector_magnitude(w)
        u = [element/eigenvalue for element in w]
    normalize_value = sum(u)
    return eigenvalue, [element/normalize_value for element in u]
