from Exercise5 import polynomial
from Exercise5 import splines
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from Exercise5 import leastSquares


def plot_two_functions(x_values, y_values, z_values, plot_text):
    plt.figure(figsize=(10, 10))
    plt.grid(True, which='both')
    plt.xlim([min(x_values) - 0.2, max(x_values) + 0.2])
    plt.ylim([-1.1, 1.1])
    plt.xlabel("x", fontsize="xx-large")
    plt.ylabel("f(x)", fontsize="xx-large")
    plt.title("Approximation of " + r'$sinx$' + plot_text, fontsize="xx-large")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(["f(x)"], loc='upper left', fontsize="xx-large")
    plt.plot(x_values, y_values)
    plt.plot(x_values, z_values)
    plt.show()


def main():
    step = 0.0315

    # Polynomial Interpolation
    x_values = np.arange(-np.pi, np.pi, step)
    print("len x newton = " + str(len(x_values)))
    y_values = []
    for value in x_values:
        y_values.append(polynomial.custom_sin(value))
    real_sin_values = np.sin(x_values)
    plot_two_functions(x_values, y_values, real_sin_values, " using Newton method")
    print("Newton Root Mean Squared Error of prediction = " + str(sqrt(sum((real_sin_values - y_values) ** 2) /
                                                                       len(x_values))))
    # Splines Interpolation
    x_values = np.arange(-np.pi, np.pi, step)
    print("len x splines = " + str(len(x_values)))
    y_values = []
    for value in x_values:
        y_values.append(splines.custom_sin(value))
    real_sin_values = np.sin(x_values)
    plot_two_functions(x_values, y_values, real_sin_values, " using natural cubic Splines")
    print(
        "Splines Root Mean Squared Error of prediction = " + str(sqrt(sum((real_sin_values - y_values) ** 2) /
                                                                      len(x_values))))
    # Least Squares Interpolation
    degree = 10
    x_values = np.arange(-np.pi, np.pi, step)
    print("len x least squares = " + str(len(x_values)))
    y_values = []
    for value in x_values:
        y_values.append(leastSquares.custom_sin(value, degree))
    real_sin_values = np.sin(x_values)
    plot_two_functions(x_values, y_values, real_sin_values, " using Least Squares with " + str(degree) +
                       " degree polynomial")
    rmse = sqrt(sum((real_sin_values - y_values) ** 2) / len(x_values))
    print(
        "Least Squares using " + str(degree) + " degree polynomial model Root Mean Squared Error of prediction = " +
        str(rmse))

    # Comparison on [-π,π]

    # Newton Method
    x_values = np.arange(-np.pi, np.pi, step)
    y_values = []
    for value in x_values:
        y_values.append(polynomial.custom_sin(value))
    real_sin_values = np.sin(x_values)
    error = abs(real_sin_values - y_values)
    for value in error:
        if value > 0.5 * (10 ** (-3)):
            print("newton false assumption of correct digits")
            print(value)
            break
    print("newton max error = " + str(max(error)))
    print("newton min error = " + str(min(error)))
    for i in range(len(error)):
        error[i] *= 100000
    hist, bin_edges = np.histogram(error)
    bin_edges = np.round(bin_edges, 0)
    plt.style.use('ggplot')
    plt.figure(figsize=[11, 11])
    plt.bar(bin_edges[:-1], hist, width=0.8, color='#2b2b2b', alpha=0.9)
    plt.xlim(min(bin_edges - 1), max(bin_edges + 1))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Error multiplied by 100000', fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.xticks(fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.title("Histogram for error using Newton method", fontsize='xx-large')
    plt.show()

    # Splines method
    x_values = np.arange(-np.pi, np.pi, step)
    y_values = []
    for value in x_values:
        y_values.append(splines.custom_sin(value))
    real_sin_values = np.sin(x_values)
    error = abs(real_sin_values - y_values)
    for value in error:
        if value > 0.5 * (10 ** (-2)):
            print("splines false assumption of correct digits")
            print(value)
            break
    print("splines max error = " + str(max(error)))
    print("splines min error = " + str(min(error)))
    multiplier = 1000
    for i in range(len(error)):
        error[i] *= multiplier
    hist, bin_edges = np.histogram(error)
    bin_edges = np.round(bin_edges, 0)
    plt.style.use('ggplot')
    plt.figure(figsize=[11, 11])
    plt.bar(bin_edges[:-1], hist, width=0.8, color='#2b2b2b', alpha=0.9)
    plt.xlim(min(bin_edges - 1), max(bin_edges + 1))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Error multiplied by ' + str(multiplier), fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.xticks(fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.title("Histogram for error using natural cubic Splines", fontsize='xx-large')
    plt.show()

    # Least Squares
    x_values = np.arange(-np.pi, np.pi, step)
    y_values = []
    for value in x_values:
        y_values.append(leastSquares.custom_sin(value))
    real_sin_values = np.sin(x_values)
    error = abs(real_sin_values - y_values)
    for value in error:
        if value > 0.5 * (10 ** (-3)):
            print("least squares false assumption of correct digits")
            print(value)
            break
    print("least squares max error = " + str(max(error)))
    print("least squares min error = " + str(min(error)))
    multiplier = 100000
    for i in range(len(error)):
        error[i] *= multiplier
    hist, bin_edges = np.histogram(error)
    bin_edges = np.round(bin_edges, 0)
    plt.style.use('ggplot')
    plt.figure(figsize=[11, 11])
    plt.bar(bin_edges[:-1], hist, width=0.8, color='#2b2b2b', alpha=0.9)
    plt.xlim(min(bin_edges - 1), max(bin_edges + 1))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Error multiplied by ' + str(multiplier), fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.xticks(fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    plt.ylabel('Frequency', fontsize='xx-large')
    plt.title("Histogram for error using least squares with 10th degree polynomial model", fontsize='xx-large')
    plt.show()


main()
