from Exercise3.util import matrix_vector_mult, print_matrix


def lu(a, b):
    """
        Function that solves the square linear system Ax = b using PA = LU decomposition method.
        Function does not make any changes to incoming matrix a and does not check that a and b have the correct
        size, e.g. if a and b do not have the same number of rows then a runtime error will occur

        Parameters
        ----------
        a : a list of lists
            The system matrix
        b : list
            The right hand side vector

        Returns
        -------
        x : list
            The solution vector of the linear system ax = b
    """
    # First create an n by n identity matrix, where n is the number of rows or columns of matrix a
    # This identity matrix will be the initial p, if any rows are swapped then p's rows will be swapped too
    p = []
    for i in range(len(a)):
        p.append([0.0 for j in range(len(a))])
        p[i][i] = 1

    # Create the l matrix that will hold the multipliers of each elimination
    l = []
    for i in range(len(a)):
        l.append([0.0 for j in range(len(a))])

    # Create the u matrix that will be the upper triangular matrix at the end of the elimination
    # At first, u is the same as the incoming matrix a, but we make a copy in order to make no changes in the incoming
    # matrix
    u = []
    for i in range(len(a)):
        u.append(list(a[i]))

    # start from row 0 and column 0, at each iteration assume that max_element of current column is at diagonal
    # save the current row, and iterate through the rest rows to find if there is a larger element
    # when the rest rows end if the max element is not in the diagonal swap row that has the max element and row that
    # has the current diagonal element, swap these rows in u,p and l matrix
    for row in range(len(u) - 1):
        max_pivot = u[row][row]
        max_pivot_row = row
        # find the current pivot with partial pivoting
        for partial_pivoting_row in range(row, len(u)):
            if abs(u[partial_pivoting_row][row]) > abs(max_pivot):
                max_pivot = u[partial_pivoting_row][row]
                max_pivot_row = partial_pivoting_row
        # swap rows if needed
        if max_pivot_row != row:
            u[max_pivot_row], u[row] = u[row], u[max_pivot_row]
            p[max_pivot_row], p[row] = p[row], p[max_pivot_row]
            l[max_pivot_row], l[row] = l[row], l[max_pivot_row]
        # gaussian elimination
        for gauss_current_row in range(row + 1, len(u)):
            multiplier = u[gauss_current_row][row] / u[row][row]
            l[gauss_current_row][row] = multiplier
            for current_column in range(row, len(u)):
                u[gauss_current_row][current_column] -= multiplier * u[row][current_column]

    # fill the diagonal of l with 1
    for i in range(len(u)):
        l[i][i] = 1
    # Solve Lc = Pb for c, starting from the top
    # first find pb vector
    pb = matrix_vector_mult(p, b)
    # create the c vector
    c = [0.0 for i in range(len(l))]
    for row in range(len(l)): # TODO MAKE FUNCTION FOR SOLVING TRIANGULAR SYSTEMS
        previous_variables_sum = 0
        for column in range(row):
            previous_variables_sum += l[row][column]*c[column]
        c[row] = pb[row] - previous_variables_sum
    # Solve Ux = c for x, starting from the bottom
    # create the x vector
    x = [0.0 for i in range(len(u))]
    for row in range(len(l)-1, -1, -1):
        previous_variables_sum = 0
        for column in range(len(l)-1, row, -1):
            previous_variables_sum += u[row][column]*x[column]
        x[row] = (c[row] - previous_variables_sum) / u[row][row]

    print("p :")
    print_matrix(p)
    print("a :")
    print_matrix(a)
    print("l :")
    print_matrix(l)
    print("u :")
    print_matrix(u)

    return x
