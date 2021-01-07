from Exercise5.leastSquares import least_squares_fit, calculate_polynomial
import matplotlib.pyplot as plt
from math import sqrt


def main():
    # AUTO HELLAS
    # next stock predict 18/3 index 10
    # after 5 meetings stock predict 24/3 index 14
    #     Ημ/νία	    Κλείσιμο	 ΜΕΤ.%	    Άνοιγμα	    Υψηλό	    Χαμηλό	    Όγκος	    Τζίρος
    #   24/3/2020	    4,0000	    3,90%	    4,0600	    4,2100	    3,9600	    200.082	    810.144,02
    #   23/3/2020	    3,8500	    -15,94%	    4,3800	    4,5600	    3,8500	    52.175	    215.182,72
    #   20/3/2020	    4,5800	    20,21%	    3,9000	    4,6000	    3,8100	    166.562	    729.012,68
    #   19/3/2020	    3,8100	    -4,27%	    3,9500	    4,1900	    3,7300	    77.002	    298.750,55
    #   18/3/2020	    3,9800	    -2,93%	    3,7000	    4,1500	    3,7000	    26.884	    107.041,69
    # index 9  17/3/2020	    4,1000	    5,67%	    3,9600	    4,1400	    3,7200	    57.182	    222.971,36
    #   16/3/2020	    3,8800	    -16,92%	    4,3200	    4,3400	    3,8800	    43.723	    176.572,31
    #   13/3/2020	    4,6700	    -0,64%	    4,6000	    4,8500	    4,5300	    65.704	    308.324,82
    #   12/3/2020	    4,7000	    -6,00%	    4,6500	    4,7700	    4,4800	    56.904	    259.759,35
    #   11/3/2020	    5,0000	    0,00%	    5,0000	    5,1200	    4,8000	    26.535	    130.887,80
    #   10/3/2020	    5,0000	    2,04%	    4,9000	    5,3600	    4,9000	    96.974	    502.890,64
    #   09/3/2020	    4,9000	    -18,06%	    5,5000	    5,5000	    4,8400	    105.596	    547.208,54
    #   06/3/2020	    5,9800	    1,01%	    5,8000	    5,9800	    5,6400	    109.022	    628.751,12
    #   05/3/2020	    5,9200	    -11,38%	    6,6800	    6,7800	    5,8000	    147.849	    918.928,74
    #   04/3/2020	    6,6800	    -3,47%	    6,8000	    7,0000	    6,6400	    93.008	    634.530,58
    x = [i for i in range(0, 15)]
    y = [6.68, 5.92, 5.98, 4.90, 5.0, 5.0, 4.7, 4.67, 3.88, 4.1, 3.98, 3.81, 4.58, 3.85, 4.0]
    #  model_degree = 3  # number of unknowns, e.g model_degree = 3 equals 2nd degree polynomial
    for model_degree in range(3, 6):
        x_train = x[:10]
        print("x_train = " + str(x_train))
        y_train = y[:10]
        print("y_train = " + str(y_train))
        c = least_squares_fit(x_train, y_train, degree=model_degree)
        print("c = "+str(c))
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
                     xytext=(0.65, 0.17), textcoords='axes fraction',
                     horizontalalignment='right', verticalalignment='top', fontsize="x-large")

        plt.scatter(10, y[10])
        plt.scatter(10, y_predict_list[0])
        plt.annotate("18/3", xy=(10, y[10]), xycoords='data',
                     xytext=(0.71, 0.15), textcoords='axes fraction',
                     horizontalalignment='right', verticalalignment='top', fontsize="x-large")

        plt.scatter(14, y[14])
        plt.scatter(14, y_predict_list[4])
        plt.annotate("24/3", xy=(14, y[14]), xycoords='data',
                     xytext=(0.96, 0.25), textcoords='axes fraction',
                     horizontalalignment='right', verticalalignment='top', fontsize="x-large")

        plt.xlabel("Day", fontsize="xx-large")
        plt.ylabel("Stock Price", fontsize="xx-large")
        plt.title("Prediction of AUTO Hellas stock using " + str(model_degree-1) + " degree polynomial.",
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
