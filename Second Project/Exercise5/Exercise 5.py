from Exercise5 import polynomial
from Exercise5 import splines
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def main():
    # Polynomial Interpolation
    """
    x_values = np.arange(-np.pi, np.pi, 0.05)
    y_values = []
    for value in x_values:
        y_values.append(polynomial.custom_sin(value))

    real_sin_values = np.sin(x_values)

    plt.figure(figsize=(10, 10))
    plt.grid(True, which='both')
    plt.xlim([min(x_values) - 0.2, max(x_values) + 0.2])
    plt.ylim([-1.1, 1.1])
    plt.xlabel("x", fontsize="xx-large")
    plt.ylabel("f(x)", fontsize="xx-large")
    plt.title("Approximation of " + r'$sinx$' + " using Newton method", fontsize="xx-large")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(["f(x)"], loc='upper left', fontsize="xx-large")
    plt.plot(x_values, y_values)
    plt.plot(x_values, real_sin_values)
    plt.show()

    # TODO ADD THIS TO LATEX WHEN COMPARING THE THREE METHODS
    print("Root Mean Squared Error of prediction = " + str(sqrt(sum((real_sin_values-y_values)**2)/len(x_values))))
    """
    # Splines Interpolation
    x_values = [0, 1, 2]
    y_values = [3, -2, 1]
    splines.splines_interpolation(x_values, y_values)


main()
