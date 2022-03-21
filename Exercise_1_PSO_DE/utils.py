import matplotlib.pyplot as plt


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


def generate_chart(pso_best_globals_iterations, pso_best_global_values, de_best_globals_iterations, de_best_global_values):
    plt.plot(pso_best_globals_iterations, pso_best_global_values, color='r',
             label='Best PSO values (iteration by iteration)')
    plt.plot(de_best_globals_iterations, de_best_global_values, color='b',
             label='Best DE values (iteration by iteration)')

    best_pso_value = round(pso_best_global_values[-1], 6)
    best_de_value = round(de_best_global_values[-1], 6)

    plt.plot(pso_best_globals_iterations[-1], best_pso_value, marker="o", markersize=7, markeredgecolor="red",
             markerfacecolor="red", label=f"Best PSO value: {best_pso_value}")
    plt.plot(de_best_globals_iterations[-1], best_de_value, marker="o", markersize=7, markeredgecolor="blue",
             markerfacecolor="blue", label=f"Best DE value: {best_de_value}")
    plt.ylim(0, 20000)
    plt.xlabel("Iteration number")
    plt.ylabel("Best global value")
    plt.legend()
    plt.show()
