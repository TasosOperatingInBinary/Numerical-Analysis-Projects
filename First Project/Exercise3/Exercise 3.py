from Exercise3.lu_decomposition import lu
from Exercise3.gauss_seidel import gauss_seidel
from Exercise3.cholesky_decomposition import chol
from Exercise3.util import matrix_mult, print_matrix, transpose, equal_matrices


def main():
    # subquestion 1
    a = [[3, 1, -4, 1], [-5, 2, 1, -2], [-1, 6, -3, -4], [-2, 1, -4, 2]]
    b = [1, -3, 2, 0]
    print("x = " + str(lu(a, b)))

    # subquestion 2
    a = [[9, 0, -27, 18], [0, 9, -9, -27], [-27, -9, 99, -27], [18, -27, -27, 121]]
    l = chol(a)
    print("l :")
    print_matrix(l)
    if not equal_matrices(matrix_mult(l, transpose(l)), a):  # works only with integers due to accuracy limitations
        print("Not correct Cholesky decomposition")
    else:
        print("Correct Cholesky decomposition")

    # subquestion 3 for n = 10
    n = 10  # define the size of the sparse matrix
    # create the sparse matrix a for the required size n
    a = []
    [a.append([0.0 for j in range(n)]) for i in range(n)]
    for i in range(n):
        a[i][i] = 5
    for i in range(n - 1):
        a[i + 1][i] = a[i][i + 1] = -2
    b = [3]
    for i in range(1, n - 1):
        b.append(1)
    b.append(3)
    x, iterations = gauss_seidel(a, b)
    print("x = [", end="")
    for i in range(len(x) - 1):
        print('{:.5f}'.format(x[i]), end=", ")
    print('{:.5f}'.format(x[len(x) - 1]), end="]")
    print()
    print("iterations = " + str(iterations))

    # subquestion 3 for n = 10000
    n = 10000  # define the size of the sparse matrix
    # create the sparse matrix a for the required size n
    a = []
    [a.append([0.0 for j in range(n)]) for i in range(n)]
    for i in range(n):
        a[i][i] = 5
    for i in range(n - 1):
        a[i + 1][i] = a[i][i + 1] = -2
    b = [3]
    for i in range(1, n - 1):
        b.append(1)
    b.append(3)
    x, iterations = gauss_seidel(a, b)
    print("x = [", end="")
    for i in range(len(x) - 1):
        print('{:.5f}'.format(x[i]), end=", ")
    print('{:.5f}'.format(x[len(x) - 1]), end="]")
    print()
    print("iterations = " + str(iterations))


main()
