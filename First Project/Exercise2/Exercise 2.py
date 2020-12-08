import numpy as np
from Exercise2.modified_secant import modified_secant
from Exercise2.modified_newton_raphson import modified_newton_raphson
from Exercise1.newton_raphson import newton_raphson
from Exercise1 import iterations_comparison
from Exercise1.secant import secant
import matplotlib.pyplot as plt
from Exercise1.bisection import bisection
from Exercise2.modified_bisection import modified_bisection
import time


def find_x0(a, b, g, g_second_der):
    for i in np.arange(a, b, 0.01):
        if g(i) * g_second_der(i) > 0:
            return i

    print("could not find x0")
    return (a + b) / 2


def f(x):
    return 94 * (np.cos(x) ** 3) - 24 * np.cos(x) + 177 * (np.sin(x) ** 2) - 108 * (np.sin(x) ** 4) - 72 * (
            np.cos(x) ** 3) * (np.sin(x) ** 2) \
           - 65


def fprime(x):
    return -282 * (np.cos(x) ** 2) * np.sin(x) + 24 * np.sin(x) + 177 * np.sin(2 * x) - 432 * (np.sin(x) ** 3) * np.cos(
        x) + 216 * \
           (np.cos(x) ** 2) * (np.sin(x) ** 3) - 72 * (np.cos(x) ** 3) * (np.sin(2 * x))


def f_second_der(x):
    # return 3 * np.cos(x) * (216 * np.cos(x) ** 2 - 432 * np.cos(x)) * np.sin(x) ** 2 + np.sin(x) * (
    #        576 * np.cos(x) ** 3 * np.sin(x) + 564 * np.cos(x) * np.sin(x)
    #        - 354 * np.sin(x)) + np.sin(x) ** 3 * (432 * np.sin(x) - 432 * np.cos(x) * np.sin(x)) \
    #       + np.cos(x) * (-144 * np.cos(x) ** 4 - 282 * np.cos(x) ** 2 + 354 * np.cos(x) + 24)
    h = 0.001
    return (fprime(x + h) - fprime(x)) / h


def main():
    """
    x_values = np.arange(0, 3, 0.001)
    y_values = f(x_values)
    plt.figure(figsize=(10, 10))
    plt.grid(True, which='both')
    plt.xlim([0, 3])
    plt.ylim([-0.2, 0.2])
    plt.xlabel("x", fontsize="xx-large")
    plt.ylabel("f(x)", fontsize="xx-large")
    plt.title("Plot of " + r'$f(x) = 94cos^{3}x - 24cosx + 177sin^{2}x - 108sin^{4}x -72cos^{3}xsin^{2}x - 65 $',
              fontsize="xx-large")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(["f(x)"], loc='lower left', fontsize="xx-large")

    plt.scatter(0.8411, f(0.8411))
    plt.annotate("root 1", xy=(0.8411, f(0.8411)), xycoords='data',
                 xytext=(0.8411 - 0.2, -0.015), fontsize=15
                 )

    plt.scatter(1.0472, f(1.0472))
    plt.annotate("root 2", xy=(1.0472, f(1.0472)), xycoords='data',
                 xytext=(1.0472 + 0.02, -0.01), fontsize=15
                 )

    plt.scatter(2.3005, 0)
    plt.annotate("root 3", xy=(2.3005, 0), xycoords='data',
                 xytext=(2.3005 + 0.02, -0.01), fontsize=15
                 )

    x_values = np.arange(0, 3.0, 0.001)
    g_prime_values = fprime(x_values)
    g_second_der_values = f_second_der(x_values)
    plt.figure(figsize=(10, 10))
    plt.grid(True, which='both')
    plt.xlim([0, 3])
    plt.ylim([-0.2, 0.2])
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


    root, iterations_num = modified_bisection(f, 1.0, 1.25)
    print("Bisection Root = " + '{:.4f}'.format(root))
    print("Iterations = " + str(iterations_num))
    root, iterations_num = modified_newton_raphson(f, fprime, f_second_der, 1.04)
    print("Newton Root = " + '{:.4f}'.format(root))
    print("Iterations = " + str(iterations_num))

    root, iterations_num = modified_secant(f, 0.9, 1.1, 1.2)

    print()
    print("Root = " + '{:.4f}'.format(root))
    print("Iterations = " + str(iterations_num))
    print()
    # root, iterations_num = bisection(f, 2.0, 2.5)

    root, iterations_num = newton_raphson(f, fprime, 1.04)

    print("Classic Root = " + '{:.4f}'.format(root))
    print("Classic Iterations = " + str(iterations_num))

    # root, iterations_num = newton_raphson(f, fprime, 1.0)
    # print("Newton Root = " + '{:.5f}'.format(root))
    # print("Newton Iterations = " + str(iterations_num))
    # print(str(modified_secant(g, 0, 1, 2)))
    """

    """
    sample = 10000
    roots = [0 for i in range(sample)]
    iterations = [0 for i in range(sample)]
    for i in range(sample):
        roots[i], iterations[i] = modified_bisection(f, 2.0, 2.5)
    print(str(roots))
    print(str(iterations))


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
    plt.title('Modified Bisection\n'+str(sample)+' function calls ',
              fontsize='xx-large')
    plt.show()
    """
    # bisection_roots, bisection_iterations, bisection_num_of_calls = iterations_comparison.bisection_iterations(f)
    sample = 1000
    roots = []
    iterations = []
    num_of_calls = 0
    times = []
    total_time_ms = 0.0
    for i in np.arange(2, 3, 0.01):
        if num_of_calls >= sample:
            break
        for j in np.arange(3, i, -0.01):
            if num_of_calls >= sample:
                break
            if f(i) * f(j) < 0:
                start_time_ns = time.time()
                current_root, current_num_of_iterations = modified_secant(f, 1.5, 1.8, 2.3)
                    #secant(f, i, j)

                end_time_ns = time.time()
                times.append((end_time_ns-start_time_ns)*1000)
                total_time_ms += (end_time_ns - start_time_ns)*1000
                roots.append(current_root)
                iterations.append(current_num_of_iterations)
                num_of_calls = num_of_calls + 1
    print(str(roots))
    print(str(times))
    print("time in ms:" + str(total_time_ms))
    print("number of iterations = " + str(len(iterations)))
    print("sum of times list in ms= " + str(sum(times)))
    n, bins, patches = plt.hist(x=times, bins='auto', color='#2b2b2b',
                                alpha=0.7, rwidth=0.85) # 0.85

    plt.style.use('ggplot')
    plt.grid(axis='y', alpha=0.75)
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    plt.xlabel('Time in Milliseconds', fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.title(str(sample) + ' function calls ' + 'of modified Secant', fontsize='xx-large')
    maxfreq = n.max()
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.show()
    """
    hist, bin_edges = np.histogram(times)
    bin_edges = np.round(bin_edges, 0)
    plt.style.use('ggplot')
    plt.figure(figsize=[11, 11])
    plt.bar(bin_edges[:-1], hist, width=0.8, color='#2b2b2b', alpha=0.9)
    plt.xlim(min(bin_edges - 1), max(bin_edges + 1))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Time in Milliseconds', fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.xticks(fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    #plt.ylabel('Time In Milliseconds', fontsize='xx-large')
    plt.title(str(sample) + ' function calls ' + 'of classic Bisection', fontsize='xx-large')
    plt.show()
"""


main()
