import matplotlib.pyplot as plt
import numpy as np
from Exercise1.newton_raphson import newton_raphson
from Exercise1.bisection import bisection
from Exercise1.secant import secant
from Exercise1.mult_newton_raphson import mult_newton_raphson
from Exercise1.iterations_comparison import bisection_iterations, newton_iterations, secant_iterations


def g(x):
    # return np.sin(x) + (x ** 2) * np.cos(x) - x ** 2 - x
    return np.e ** ((np.sin(x)) ** 3) + x ** 6 - 2 * (x ** 4) - x ** 3 - 1


def gprime(x):
    # return np.cos(x) + 2 * x * np.cos(x) + (x ** 2) * (-np.sin(x)) - 2 * x - 1
    return 3 * (np.e ** ((np.sin(x)) ** 3)) * ((np.sin(x)) ** 2) * np.cos(x) + 6 * (x ** 5) - 8 * (x ** 3) - 3 * (
           x ** 2)


def g_second_der(x):
    # return 3 * np.cos(x) * (216 * np.cos(x) ** 2 - 432 * np.cos(x)) * np.sin(x) ** 2 + np.sin(x) * (
    #        576 * np.cos(x) ** 3 * np.sin(x) + 564 * np.cos(x) * np.sin(x)
    #        - 354 * np.sin(x)) + np.sin(x) ** 3 * (432 * np.sin(x) - 432 * np.cos(x) * np.sin(x)) \
    #       + np.cos(x) * (-144 * np.cos(x) ** 4 - 282 * np.cos(x) ** 2 + 354 * np.cos(x) + 24)
    h = 0.001
    return (gprime(x + h) - gprime(x)) / h


def main():

    root, iterations_num = secant(g, 1.3, 1.9)

    print("Root = " + '{:.4f}'.format(root))
    print("Iterations = " + str(iterations_num))

    """
    x_values = np.arange(-2.0, 2.0, 0.001)
    y_values = g(x_values)
    plt.figure(figsize=(10, 10))
    plt.grid(True, which='both')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel("x", fontsize="xx-large")
    plt.ylabel("f(x)", fontsize="xx-large")
    plt.title("Plot of " + r'$f(x) = e^{sin^{3}x} + x^{6} -2x^{4} -x^{3} - 1$', fontsize="xx-large")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    # root, iterations_num = bisection(g, 0, 0.5)

    # root, iterations_num = newton_raphson(g, gprime, 1)

    root, iterations_num = secant(g, 0.0, 1.5)

    # root, iterations_num = mult_newton_raphson(g, gprime, 1, 3)


    plt.scatter(root, g(root))
    plt.annotate("root 1", xy=(root, g(root)), xycoords='data',
                 xytext=(root + 0.04, 0.06), fontsize=15
                 )

    
    plt.scatter(-1.198, g(-1.198))
    plt.annotate("root 2", xy=(-1.198, g(-1.198)), xycoords='data',
                 xytext=(-1.198 + 0.04, 0.06), fontsize=15
                 )

    plt.scatter(1.53, g(1.53))
    plt.annotate("root 3", xy=(1.53, g(1.53)), xycoords='data',
                 xytext=(1.53 + 0.04, 0.06), fontsize=15
                 )
    
    print("Root = " + '{:.5f}'.format(root))
    print("Iterations = " + str(iterations_num))

    plt.legend(["f(x)"], loc='upper left', fontsize="xx-large")
    plt.plot(x_values, y_values)
    #plt.show()

    
    x_values = np.arange(-2.0, 2.0, 0.001)
    g_prime_values = gprime(x_values)
    g_second_der_values = g_second_der(x_values)
    plt.figure(figsize=(10, 10))
    plt.grid(True, which='both')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel("x", fontsize="xx-large")
    plt.title("Plot of first and second derivative of " + r'$f(x)$', fontsize="xx-large")
    plt.legend(["f'(x)", "f\"(x)"], loc='upper left', fontsize="xx-large")
    p = plt.plot(x_values, g_prime_values)
    plt.gca().get_legend().legendHandles[0].set_color(p[0].get_color())
    p = plt.plot(x_values, g_second_der_values)
    plt.gca().get_legend().legendHandles[1].set_color(p[0].get_color())
    plt.show()
    """
    """
    for root in roots:
        print('{:.5f}'.format(root) ,end=", ")
    print()
    print(iterations)
    print("number of roots : " + str(len(roots)))
    

    #roots, iterations, num_of_calls = bisection_iterations()
    # roots, iterations, num_of_calls = newton_iterations()
    # roots, iterations, num_of_calls = secant_iterations()
    if np.nan in roots: print("found nan")
    print("number of calls = " + str(num_of_calls))
    print("roots len = " + str(len(roots)))
    print("iterations len =" + str(len(iterations)))
    print(iterations)
    if len(roots) == len(iterations):
        print("same length")
    else:
        print("not same length")
    print("roots = "+str(roots))
    frequencies = []
    for i in range(52):
        frequencies.append(0)
    for i in range(2,52):
        for iteration in iterations:
            if iteration == i:
                frequencies[i] += 1
    while 0 in frequencies: frequencies.remove(0)
    print("frequencies =" + str(frequencies))
    print("frequencies len ="+str(len(frequencies)))
    iterations_set = set(iterations)
    print("iterations set = " + str(iterations_set))
    hist, bin_edges = np.histogram(iterations)
    bin_edges = np.round(bin_edges, 0)
    plt.style.use('ggplot')
    plt.figure(figsize=[11, 11])
    plt.bar(bin_edges[:-1], hist, width=0.8, color='#2b2b2b', alpha=0.9)
    plt.xlim(min(bin_edges - 1), max(bin_edges + 1))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Number of Iterations', fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.xticks(fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.title('Bisection iterations for root ='+str(roots[0])+'\n function calls = ' + str(num_of_calls), fontsize='xx-large')
    plt.show()
    """

main()
