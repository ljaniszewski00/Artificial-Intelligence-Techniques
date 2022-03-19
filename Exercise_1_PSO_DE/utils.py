import matplotlib.pyplot as plt
import numpy as np

def calculate_function_value(function_number, particle):
    value = 0
    if function_number == 1:
        # Sphere
        for iteration_number in range(1, particle.dimensions + 1):
            value += pow(particle.positions[iteration_number-1], 2)
        return value
    elif function_number == 2:
        # Schwefel
        for iteration_number in range(1, particle.dimensions + 1):
            value += pow(abs(particle.positions[iteration_number-1]), 2)
        temp_value = 1
        for iteration_number in range(1, particle.dimensions + 1):
            temp_value *= abs(particle.positions[iteration_number-1])
        value += temp_value
        return value
    elif function_number == 3:
        # Rosenbrock
        for iteration_number in range(1, particle.dimensions):
            value += 100 * (pow(particle.positions[iteration_number] -
                            pow(particle.positions[iteration_number-1], 2), 2) +
                            pow(particle.positions[iteration_number-1] - 1, 2))
        return value


def generate_chart(best_globals_iterations, pso_best_global_values, de_best_global_values=None):
    plt.plot(best_globals_iterations, pso_best_global_values, color='r', label='PSO')
    # # plt.plot(iterations_numbers, de_best_global_values, color='b', label='DE')
    plt.xlim(0, max(best_globals_iterations))
    plt.ylim(0, 1000)
    plt.xlabel("Iteration number")
    plt.ylabel("Best global value")
    plt.legend()
    plt.show()

