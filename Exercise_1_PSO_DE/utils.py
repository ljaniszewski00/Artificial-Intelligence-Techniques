import numpy as np


def calculate_function_value(function_number, n, x, x2=None):
    value = 0
    if function_number == 1:
        for iteration_number in range(1, n):
            # print()
            # print(value)
            # print()
            value += pow(x, 2)
        return value
    elif function_number == 2:
        for iteration_number in range(1, n):
            value += pow(abs(x), 2)
        temp_value = 1
        for iteration_number in range(1, n):
            temp_value *= abs(x)
        value += temp_value
        return value
    elif function_number == 3:
        for iteration_number in range(1, n):
            value += x
        value = -value
        temp_value = 0
        for iteration_number in range(1, n):
            temp_value += iteration_number / 2 * x
        value += pow(temp_value, 2)
        value += pow(temp_value, 4)
        return value
    elif function_number == 4:
        return -np.cos(x) * np.cos(x2) * np.exp(pow(-x-np.pi, 2) - pow(-x2-np.pi, 2))


