import numpy as np


def calculate_function_value(function_number, particle):
    value = 0
    if function_number == 1:
        for iteration_number in range(1, len(particle.positions) + 1):
            # print()
            # print(value)
            # print()

            print()
            print(value)
            print()
            value += pow(particle.positions[iteration_number-1], 2)
        return value
    elif function_number == 2:
        for iteration_number in range(1, len(particle.positions) + 1):
            value += pow(abs(particle.positions[iteration_number-1]), 2)
        temp_value = 1
        for iteration_number in range(1, len(particle.positions) + 1):
            temp_value *= abs(particle.positions[iteration_number-1])
        value += temp_value
        return value
    elif function_number == 3:
        for iteration_number in range(1, len(particle.positions) + 1):
            value += particle.positions[iteration_number-1]
        value = -value
        temp_value = 0
        for iteration_number in range(1, len(particle.positions) + 1):
            temp_value += iteration_number-1 / 2 * particle.positions[iteration_number-1]
        value += pow(temp_value, 2)
        value += pow(temp_value, 4)
        return value
    elif function_number == 4:
        return -np.cos(particle.positions[0]) * np.cos(particle.positions[1]) * \
               np.exp(pow(-particle.positions[0]-np.pi, 2) - pow(-particle.positions[1]-np.pi, 2))


