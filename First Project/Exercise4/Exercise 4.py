from Exercise4.power_method import power_method


def main():
    """
    # subquestion 1
    a = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

    q = 0.15
    g = []
    n = len(a)
    for i in range(n):
        g.append([])
        for j in range(n):
            g[i].append(q / n + (a[j][i] * (1 - q)) / sum(a[j]))

    dom_eigen_value, dom_eigen_vector = power_method(g)
    print("\n\np = \n[", end=" ")
    for i in range(len(dom_eigen_vector)-1):
        print(dom_eigen_vector[i], end=" ,\n")
    print(str(dom_eigen_vector[len(dom_eigen_vector)-1]), end="]\n")
    print("\ndominant eigenvalue = "+str(dom_eigen_value))
    print("sum p = "+str(sum(dom_eigen_vector)))
    ########################################
    """
    # subquestion 2
    a = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], #1
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], #2
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], #3
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #4
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #5
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #8
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #9
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], #11
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0], #12
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], #13
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1], #14
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0]] #15

    q = 0.15
    g = []
    n = len(a)
    for i in range(n):
        g.append([])
        for j in range(n):
            if sum(a[j])!=0:
                g[i].append(q / n + (a[j][i] * (1 - q)) / sum(a[j]))
            else:
                g[i].append(1/n)

    dom_eigen_value, dom_eigen_vector = power_method(g)
    print("\n\np = \n[", end=" ")
    for i in range(len(dom_eigen_vector)-1):
        print(dom_eigen_vector[i], end=" ,\n")
    print(str(dom_eigen_vector[len(dom_eigen_vector)-1]), end="]\n")
    print("\ndominant eigenvalue = "+str(dom_eigen_value))
    print("sum p = "+str(sum(dom_eigen_vector)))

    column_sums = []
    for column in range(len(a)):
        current_sum = 0
        for row in range(len(a)):
            current_sum += a[row][column]
        column_sums.append(current_sum)

    print(str(column_sums))


main()
