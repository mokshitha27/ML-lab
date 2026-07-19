import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


def read_data():

    data = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")

    return data


def numpy_mean(price):

    return np.mean(price)



def numpy_variance(price):

    return np.var(price)


def my_mean(price):

    total = 0

    for value in price:

        total = total + value

    return total / len(price)


def my_variance(price):

    mean = my_mean(price)

    total = 0

    for value in price:

        total = total + (value - mean) ** 2

    return total / len(price)


def execution_time(fun, price):

    total = 0

    for i in range(10):

        start = time.time()

        fun(price)

        end = time.time()

        total = total + (end - start)

    return total / 10



def wednesday_mean(data):

    wed = data[data["Day"] == "Wed"]

    return np.mean(wed["Price"])


def april_mean(data):

    april = data[data["Month"] == "Apr"]

    return np.mean(april["Price"])


def change_column(data):

    chg = data["Chg%"].astype(str)

    chg = chg.str.replace("%", "", regex=False)

    chg = chg.astype(float)

    return chg


def loss_probability(chg):

    loss = len(chg[chg < 0])

    total = len(chg)

    return loss / total


def profit_wednesday(data):

    wed = data[data["Day"] == "Wed"]

    chg = wed["Chg%"].astype(str)

    chg = chg.str.replace("%", "", regex=False)

    chg = chg.astype(float)

    profit = len(chg[chg > 0])

    total = len(chg)

    return profit / total


def conditional_probability(data):

    return profit_wednesday(data)


def scatter_plot(data, chg):

    plt.scatter(data["Day"], chg)

    plt.title("Change Percentage vs Day")

    plt.xlabel("Day")

    plt.ylabel("Change Percentage")

    plt.show()


def main():

    data = read_data()

    price = data["Price"]

    chg = change_column(data)

    mean1 = numpy_mean(price)

    var1 = numpy_variance(price)

    mean2 = my_mean(price)

    var2 = my_variance(price)

    time1 = execution_time(numpy_mean, price)

    time2 = execution_time(my_mean, price)

    wed = wednesday_mean(data)

    april = april_mean(data)

    loss = loss_probability(chg)

    profit = profit_wednesday(data)

    cond = conditional_probability(data)

    print("Mean using NumPy =", mean1)
    print("Variance using NumPy =", var1)
    print()

    print("Mean using Own Function =", mean2)
    print("Variance using Own Function =", var2)
    print()

    print("Average Time using NumPy =", time1)
    print("Average Time using Own Function =", time2)
    print()

    print("Population Mean =", mean1)
    print("Wednesday Sample Mean =", wed)
    print()

    print("April Sample Mean =", april)
    print()

    print("Probability of Making Loss =", loss)
    print()

    print("Probability of Profit on Wednesday =", profit)
    print()

    print("Conditional Probability of Profit given Wednesday =", cond)

    scatter_plot(data, chg)


main()