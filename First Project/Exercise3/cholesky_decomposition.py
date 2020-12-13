from math import sqrt
from Exercise3.util import vector_mult, transpose


def chol(matrix):
    """
        Function that finds the Cholesky decomposition of the symmetric positive-definite matrix a
        Function does not make any changed to incoming matrix a. Function does not check that the incoming matrix is
        symmetric positive-definite matrix so if the matrix is not symmetric positive-definite computations won't be
        correct.

        Parameters
        ----------
        matrix : a list of lists
            The matrix whose Cholesky decomposition will be calculated

        Returns
        -------
        l : a list of lists
            The lower triangle matrix that consists the Cholesky decomposition of matrix a.
    """
    # Copy the incoming matrix so the function does not make any change
    a = []
    for i in range(len(matrix)):
        a.append(list(matrix[i]))
    # Create the r matrix that will be the upper triangular Cholesky decomposition matrix of the incoming matrix
    r = []
    for i in range(len(a)):
        r.append([0.0 for j in range(len(a))])
    # Cholesky decomposition
    for k in range(len(a)):
        if a[k][k] < 0:
            return transpose(r)
        # For each row k of the incoming matrix calculate r[k][k]
        r[k][k] = sqrt(a[k][k])
        # initialize the u vector
        u = [0.0 for i in range(len(a))]
        # calculate the u vector
        for j in range(k+1, len(a)):
            u[j] = (1/r[k][k]) * a[k][j]
        # copy the u vector to the elements next to the r[k][k] element
        for j in range(k+1, len(a)):
            r[k][j] = u[j]
        # calculate the matrix u*(u^T)
        u_u_transpose = vector_mult(u, u)
        # subtract the matrix u*(u^T) from the proper submatrix of A
        for i in range(k+1, len(a)):
            for j in range(k + 1, len(a)):
                a[i][j] = a[i][j] - u_u_transpose[i][j]

    return transpose(r)
