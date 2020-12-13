def matrix_mult(a, b):
    """
        Function that multiplies two matrices a and b

        Parameters
        ----------
        a,b : matrices

        Returns
        -------
        new_array : matrix
            The matrix product of the inputs
    """
    new_array = []
    for i in range(len(a)):
        new_array.append([0 for i in range(len(b[0]))])
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                new_array[i][j] += a[i][k] * b[k][j]

    return new_array


def matrix_vector_mult(matrix, vector):
    new_vector = []
    for row in range(len(matrix)):
        new_vector.append(0)
        for column in range(len(matrix[row])):
            new_vector[row] += matrix[row][column] * vector[column]

    return new_vector


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print('{:4}'.format(val), end=" ")
        print()

    print()


def vector_inf_norm(vector):
    maximum = abs(vector[0])
    for i in range(1, len(vector)):
        if abs(vector[i]) > maximum:
            maximum = abs(vector[i])

    return maximum


def sub_vector(vector1, vector2):
    # TODO check that vector1 and vector2 have the same length
    new_vector = []
    for i in range(len(vector1)):
        new_vector.append(vector1[i] - vector2[i])
    return new_vector


def vector_mult(vector1, vector2):
    # TODO check that vector1 and vector2 can be multiplied
    new_matrix = []
    for i in range(len(vector1)):
        new_matrix.append([0 for i in range(len(vector2))])
        for j in range(len(vector2)):
            new_matrix[i][j] = vector1[i]*vector2[j]
    return new_matrix


def transpose(matrix):
    transposed_matrix = []
    [transposed_matrix.append(list(matrix[i])) for i in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            transposed_matrix[column][row] = matrix[row][column]

    return transposed_matrix


def equal_matrices(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True
