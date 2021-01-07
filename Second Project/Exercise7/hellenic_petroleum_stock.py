from Exercise5.leastSquares import least_squares_fit, calculate_polynomial
import matplotlib.pyplot as plt
from math import sqrt


def main():
    # HELLENIC PETROLEUM
    # next stock predict 18/3 index 10
    # after 5 meetings stock predict 24/3 index 14
    #     Ημ/νία	    Κλείσιμο	 ΜΕΤ.%	    Άνοιγμα	    Υψηλό	    Χαμηλό	    Όγκος	    Τζίρος
    #   24/3/2020	    5,2800	    6,02%	    5,2000	    5,3400	    5,1500	    140.934	    740.384,35
    #   23/3/2020	    4,9800	    -6,92%	    5,0000	    5,1300	    4,9100	    77.921	    392.288,62
    #   20/3/2020	    5,3500	    11,57%	    5,2600	    5,4200	    4,9500	    320.114	    1.676.990,20
    #   19/3/2020	    4,7950	    5,27%	    4,5550	    4,8800	    4,5550	    120.000	    569.829,09
    #   18/3/2020	    4,5550	    -2,98%	    4,6950	    4,7200	    4,5000	    142.129	    656.205,35
    #   17/3/2020	    4,6950	    0,97%	    4,8100	    4,8100	    4,5000	    153.115	    709.026,29
    #   16/3/2020	    4,6500	    -6,63%	    4,6500	    4,8800	    4,4000	    206.275	    947.322,04
    #   13/3/2020	    4,9800	    3,32%	    4,9000	    5,0100	    4,7000	    175.710	    867.315,54
    #   12/3/2020	    4,8200	    -7,31%	    4,8400	    5,0000	    4,7000	    241.361	    1.164.723,50
    #   11/3/2020	    5,2000	    -2,80%	    5,4900	    5,5400	    5,1000	    237.401	    1.265.878,96
    #   10/3/2020	    5,3500	    7,86%	    5,1900	    5,5600	    5,1000	    225.354	    1.206.633,72
    #   09/3/2020	    4,9600	    -17,61%	    5,4200	    5,5500	    4,8600	    444.826	    2.364.207,13
    #   06/3/2020	    6,0200	    -4,60%	    6,3100	    6,3200	    6,0000	    228.595	    1.397.621,49
    #   5/3/2020	    6,3100	    -7,34%	    6,8200	    6,8400	    6,3000	    207.228	    1.377.130,98
    #   04/3/2020	    6,8100	    -0,58%	    6,6800	    6,9700	    6,6800	    222.806	    1.524.382,01
    x = [i for i in range(0, 15)]
    y = [6.81, 6.31, 6.02, 4.96, 5.35, 5.2, 4.82, 4.98, 4.65, 4.695, 4.555, 4.795, 5.35, 4.98, 5.28]
    #  model_degree = 3  # number of unknowns, e.g model_degree = 3 equals 2nd degree polynomial
    for model_degree in range(3, 6):
        x_train = x[:10]
        print("x_train = " + str(x_train))
        y_train = y[:10]
        print("y_train = " + str(y_train))
        c = least_squares_fit(x_train, y_train, degree=model_degree)
        print("c = " + str(c))
        x_test = x[10:15]
        print("x_test = " + str(x_test))
        y_test = y[10:15]
        print("y_test = " + str(y_test))

        y_plot = []
        x_plot = range(0, 15)
        for x_plot_value in x_plot:
            y_plot.append(calculate_polynomial(c, x_plot_value, degree=model_degree))

        se = 0
        index = 0
        y_predict_list = []
        for x_test_value in x_test:
            y_predict = calculate_polynomial(c, x_test_value, degree=model_degree)
            se += (y_predict-y_test[index])**2
            y_predict_list.append(y_predict)
            index += 1

        plt.figure(figsize=(10, 10))
        plt.grid(True, which='both')
        plt.xlim([-0.25, 15])
        plt.ylim([min(y_plot)-0.25, max(y_plot)+1])

        plt.scatter(9, y[9])
        plt.scatter(9, calculate_polynomial(c, 9, degree=model_degree))
        plt.annotate("17/3", xy=(9, y[9]), xycoords='data',
                     xytext=(0.65, 0.20), textcoords='axes fraction',
                     horizontalalignment='right', verticalalignment='top', fontsize="x-large")

        plt.scatter(10, y[10])
        plt.scatter(10, y_predict_list[0])
        plt.annotate("18/3", xy=(10, y[10]), xycoords='data',
                     xytext=(0.715, 0.20), textcoords='axes fraction',
                     horizontalalignment='right', verticalalignment='top', fontsize="x-large")

        plt.scatter(14, y[14])
        plt.scatter(14, y_predict_list[4])
        plt.annotate("24/3", xy=(14, y[14]), xycoords='data',
                     xytext=(0.96, 0.30), textcoords='axes fraction',
                     horizontalalignment='right', verticalalignment='top', fontsize="x-large")

        plt.xlabel("Day", fontsize="xx-large")
        plt.ylabel("Stock Price", fontsize="xx-large")
        plt.title("Prediction of Hellenic Petroleum stock using " + str(model_degree-1) + " degree polynomial.",
                  fontsize="xx-large")
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.legend(["Predict Stock Price", "Real Stock Price"], loc='upper left', fontsize="xx-large")
        p = plt.plot(x_plot, y_plot, x, y)
        type(p)
        type(p[0])
        plt.gca().get_legend().legendHandles[0].set_color(p[0].get_color())
        plt.gca().get_legend().legendHandles[1].set_color(p[1].get_color())
        plt.show()

        print("y_predict = [", end="")
        for value in y_predict_list[:len(y_predict_list)-1]:
            print('{:.2f}'.format(value), end=", ")
        print('{:.2f}'.format(y_predict_list[len(y_predict_list)-1]), end="]")
        print()
        rmse = sqrt(se/len(x_test))
        print("rmse = "+str(rmse))
        print("next meeting stock predict = "+str(calculate_polynomial(c, 10, degree=model_degree)))
        print("real next meeting stock value = " + str(y[10]))
        print("after 5 meetings stock predict = "+str(calculate_polynomial(c, 14, degree=model_degree)))
        print("after 5 meetings real stock value ="+str(y[14]))
        print()
        print()


main()
