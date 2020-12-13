from Exercise3.util import vector_inf_norm, sub_vector


def gauss_seidel(a, b, eps=5e-5):
    """
        Function that solves the linear system ax = b using Gauss-Seidel method.
        Function does not make any changes to incoming matrix a and does not check that a has strict diagonal
        dominance so if a does not have strict diagonal dominance no convergence is guaranteed.

        Parameters
        ----------
        a : list of lists
            The system matrix
        b : list
            The right hand side vector
        eps : float
            The target accuracy

        Returns
        -------
        x : list
            The solution vector of the linear system ax = b
    """
    # Create the x vector and copy the incoming matrix a. Also create previous_x vector so accuracy can be calculated
    # at each step. Gauss-Seidel method converges with any initial vector x0 if a has strict diagonal dominance, here we
    # start iterating from the vector (0,0,....,0)
    x = []
    [x.append(0.0) for i in range(len(b))]
    matrix = []
    for i in range(len(a)):
        matrix.append(list(a[i]))
    previous_x = []
    [previous_x.append(x[i]) for i in range(len(b))]
    iterations = 0
    # Gauss-Seidel algorithm
    while True:
        # for every row of a find the sum of updated x's at "iterations" step, for the x's that are not updated
        # in the current ("iterations") step use their previous value
        for row in range(len(a)):
            multiplier = 1 / matrix[row][row]
            updated_variables_sum = 0.0
            for j in range(row):
                updated_variables_sum += matrix[row][j] * x[j]
            not_updated_variables_sum = 0.0
            for j in range(row + 1, len(a)):
                not_updated_variables_sum += matrix[row][j] * x[j]
            # save the previous approximation for the solution vector x
            # and update the current approximation for the solution vector x
            previous_x[row] = x[row]
            x[row] = multiplier * (b[row] - updated_variables_sum - not_updated_variables_sum)
        # update the iterations variable and if target accuracy is achieved return the solution vector x
        iterations += 1
        if vector_inf_norm(sub_vector(x, previous_x)) <= eps:
            break

    return x, iterations
