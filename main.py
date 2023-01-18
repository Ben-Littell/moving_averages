import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

x = [1, 4, 5, 6, -2, 9, 3, 4, 0, 2]
W = [1, 2, 3, 2, 1]
X = [4 , 7, 8, 2 , 10 , 23 , 9 , 5]


def moving_avg(data, w=None):
    if w is None:
        w = [1, 1, 1, 1]
    new_list = []
    for i in range(len(data) - len(w)+1):
        k = []
        for j in range(len(w)):
            k.append(data[i + j]*w[j])
        new_list.append(sum(k)/sum(w))
    return new_list


x3 = [4 , 7, 8, 2 , 10 , 23 , 9 , 5]
w3 = [.5, .5]


def fading_moving_avg(data, w_list):
    output = []
    w1, w2 = w_list[0], w_list[1]
    if sum(w_list) == 1:
        for i in range(len(data)):
            if i == 0:
                output.append(data[i])
            else:
                output.append((w1 * output[i - 1]) + (w2 * data[i]))

    return output









# test = moving_avg(x)
# test2 = moving_avg(X, W)
# print(test)
# print(test2)


