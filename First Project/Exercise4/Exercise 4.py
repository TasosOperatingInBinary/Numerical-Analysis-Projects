from Exercise4.power_method import power_method


def main():

    # subquestion 2
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
        print(str(i+1)+" "+str(dom_eigen_vector[i]), end=" ,\n")
    print(str(i+1)+" "+str(dom_eigen_vector[len(dom_eigen_vector)-1]), end="]\n")
    print("\ndominant eigenvalue = "+str(dom_eigen_value))
    print("sum p = "+str(sum(dom_eigen_vector)))

    column_sums = []
    for column in range(len(a)):
        current_sum = 0
        for row in range(len(a)):
            current_sum += a[row][column]
        column_sums.append(current_sum)

    print(str(column_sums))
    ########################################
    
    # subquestion 3, 4
    a = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 1
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 3
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 4
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 5
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 6
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 7
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 8
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 9
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # 11
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],  # 12
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # 13
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],  # 14
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]  # 15

    q = 0.15
    g = []
    n = len(a)
    for i in range(n):
        g.append([])
        for j in range(n):
            if sum(a[j]) != 0:
                g[i].append(q / n + (a[j][i] * (1 - q)) / sum(a[j]))
            else:
                g[i].append(1 / n)

    print("q = " + str(q))
    dom_eigen_value, dom_eigen_vector = power_method(g)
    print("p = \n[", end=" ")
    for i in range(len(dom_eigen_vector) - 1):
        print('{:.5f}'.format(dom_eigen_vector[i]), end=" ,\n")
    print('{:.5f}'.format(dom_eigen_vector[len(dom_eigen_vector) - 1]), end="]\n")
    print("\ndominant eigenvalue = " + str(dom_eigen_value))
    print("sum p = " + str(sum(dom_eigen_vector)))

    column_sums = []
    for column in range(len(a)):
        current_sum = 0
        for row in range(len(a)):
            current_sum += a[row][column]
        column_sums.append(current_sum)

    print(str(column_sums))


    # subquestion 5
    a = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 1
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 3
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 4
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 5
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 6
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 7
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],  # 8
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 9
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 10
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 11
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 0, 0, 0],  # 12
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # 13
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],  # 14
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]  # 15

    q = 0.15
    g = []
    n = len(a)
    for i in range(n):
        g.append([])
        for j in range(n):
            g[i].append(q / n + (a[j][i] * (1 - q)) / sum(a[j]))

    dom_eigen_value, dom_eigen_vector = power_method(g)
    print("\n\np = \n[", end=" ")
    for i in range(len(dom_eigen_vector) - 1):
        print(dom_eigen_vector[i], end=" ,\n")
    print(str(dom_eigen_vector[len(dom_eigen_vector) - 1]), end="]\n")
    print("\ndominant eigenvalue = " + str(dom_eigen_value))
    print("sum p = " + str(sum(dom_eigen_vector)))


    previous_page_rank = dom_eigen_vector

    # subquestion 6
    #     1  2  3  4  5  6  7  8  9 11  12 13 14 15
    a = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 1
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 2
         [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 4
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 6
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 7
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 8
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 11
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],  # 12
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 13
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],  # 14
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]  # 15

    q = 0.15
    g = []
    n = len(a)
    for i in range(n):
        g.append([])
        for j in range(n):
            g[i].append(q / n + (a[j][i] * (1 - q)) / sum(a[j]))

    dom_eigen_value, dom_eigen_vector = power_method(g)
    print("\n\np = \n[", end=" ")
    for i in range(len(dom_eigen_vector) - 1):
        if i == 9:
            print("----------------------")
        print(str(i+1)+" "+str(dom_eigen_vector[i]), end=" ,\n")
    print(str(i+1)+" " +str(dom_eigen_vector[len(dom_eigen_vector) - 1]), end="]\n")
    print("\ndominant eigenvalue = " + str(dom_eigen_value))
    print("sum p = " + str(sum(dom_eigen_vector)))

    column_sums = []
    for column in range(len(a)):
        current_sum = 0
        for row in range(len(a)):
            current_sum += a[row][column]
        column_sums.append(current_sum)

    print(str(column_sums))

    print("\n\n")
    increase_sum = 0
    decrease_sum = 0
    increased = []
    for i in range(9):
        if dom_eigen_vector[i] > previous_page_rank[i]:
            increase_sum += dom_eigen_vector[i]-previous_page_rank[i]
            print("page "+str(i+1)+" increased by "+str(dom_eigen_vector[i]-previous_page_rank[i]))
            increased.append(i+1)
        else:
            decrease_sum += -dom_eigen_vector[i]+previous_page_rank[i]
    for i in range(10,15):
        if dom_eigen_vector[i-1] > previous_page_rank[i]:
            increase_sum += dom_eigen_vector[i-1] - previous_page_rank[i]
            print("page " + str(i + 1) + " increased by " + str(dom_eigen_vector[i-1] - previous_page_rank[i]))
            increased.append(i+1)
        else:
            decrease_sum += -dom_eigen_vector[i-1] + previous_page_rank[i]

    print(str(increased))
    print("total increase sum: "+str(increase_sum))
    print("total decrease sum: "+str(decrease_sum))
    print("difference: "+str(increase_sum-decrease_sum))


main()
