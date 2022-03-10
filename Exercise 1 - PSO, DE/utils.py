import numpy as np


def calculate_function_value(function_number, n, x1, x2=None):
    value = 0
    if function_number == 1:
        for iteration_number in range(1, n):
            value += pow(x1, 2)
        return value
    elif function_number == 2:
        return -np.cos(x1) * np.cos(x2) * pow(np.exp(-x1-np.pi), 2) - pow(-x2-np.pi)
    elif function_number == 3:
        for iteration_number in range(1, n):
            value += x1
        value = -value
        temp_value = 0
        for iteration_number in range(1, n):
            temp_value += iteration_number / 2 * x1
        value += pow(temp_value, 2)
        value += pow(temp_value, 4)
        return value


