import matplotlib.pyplot as plt


def get_data_from_user(exercise_number):
    print()
    print("------------------------------------------------------------------")
    if exercise_number == 1:
        print("Exercise 1 - PSO and DE optimization algorithms")
    elif exercise_number == 2:
        print("Exercise 2 - Bat and Butterfly optimization algorithms")
    elif exercise_number == 3:
        print("Exercise 3 - ... optimization algorithms")
    print("------------------------------------------------------------------")
    coefficient_method = str(input("\nDo you wish to use static, fixed coefficient? Y/N: "))
    coefficient_method = coefficient_method.lower()
    while coefficient_method not in ['y', 'n']:
        coefficient_method = str(input("\nDo you wish to use static, fixed coefficient? Y/N: "))
        coefficient_method = coefficient_method.lower()
    static_coefficients = False
    if coefficient_method == 'y':
        static_coefficients = False
    elif coefficient_method == 'n':
        static_coefficients = True

    population_number = int(input("\nChoose population number: "))
    while type(population_number) != int:
        population_number = int(input("\nChoose correct population number: "))

    print("""
Choose function's number you would like to use:
1). Sphere
2). Schwefel
3). Rosenbrock""")
    function_number = int(input("Your choice: "))
    while function_number not in [1, 2, 3, 4]:
        int(input("\nPlease choose correct function number: "))

    dimensions_number = int(input("\nProvide dimensions number: "))
    while dimensions_number <= 0:
        dimensions_number = int(input("\nProvide correct dimensions number: "))

    print("""
Choose algorithm stop condition:
1). max iterations
2). achieved accuracy""")
    stop_condition = int(input("Your choice: "))
    while stop_condition not in [1, 2]:
        stop_condition = int(input("Please provide correct stop condition number: "))

    # Setting function range depending on selected function
    function_range = [-100, 100]
    if function_number == 1:
        function_range = [-100, 100]
    elif function_number == 2:
        function_range = [-10, 10]
    elif function_number == 3:
        function_range = [-2.048, 2.048]

    if stop_condition == 1:
        max_iterations = int(input("\nChoose max iterations number: "))
        return stop_condition, static_coefficients, population_number, function_number, dimensions_number, \
               max_iterations
    else:
        accuracy = 0.0001
        if function_number == 1:
            accuracy = 0.0001
        elif function_number == 2:
            accuracy = 0.000001
        elif function_number == 3:
            accuracy = 30

        return stop_condition, static_coefficients, population_number, function_number, dimensions_number, accuracy


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


def calculate_function_value_with_positons(function_number, positions):
    value = 0
    if function_number == 1:
        # Sphere
        for iteration_number in range(1, len(positions) + 1):
            value += pow(positions[iteration_number-1], 2)
        return value
    elif function_number == 2:
        # Schwefel
        for iteration_number in range(1, len(positions) + 1):
            value += pow(abs(positions[iteration_number-1]), 2)
        temp_value = 1
        for iteration_number in range(1, len(positions) + 1):
            temp_value *= abs(positions[iteration_number-1])
        value += temp_value
        return value
    elif function_number == 3:
        # Rosenbrock
        for iteration_number in range(1, len(positions)):
            value += 100 * (pow(positions[iteration_number] -
                            pow(positions[iteration_number-1], 2), 2) +
                            pow(positions[iteration_number-1] - 1, 2))
        return value


def generate_chart(first_algorithm_name, first_algorithm_best_globals_iterations, first_algorithm_global_values,
                   second_algorithm_name, second_algorithm_globals_iterations, second_algorithm_global_values):
    plt.plot(first_algorithm_best_globals_iterations, first_algorithm_global_values, color='r',
             label=f'Best {first_algorithm_name} values (iteration by iteration)')
    plt.plot(second_algorithm_globals_iterations, second_algorithm_global_values, color='b',
             label=f'Best {second_algorithm_name} values (iteration by iteration)')

    best_pso_value = round(first_algorithm_global_values[-1], 6)
    best_de_value = round(second_algorithm_global_values[-1], 6)

    plt.plot(first_algorithm_best_globals_iterations[-1], best_pso_value, marker="o", markersize=7,
             markeredgecolor="red", markerfacecolor="red", label=f"Best {first_algorithm_name} value: {best_pso_value}")
    plt.plot(second_algorithm_globals_iterations[-1], best_de_value, marker="o", markersize=7, markeredgecolor="blue",
             markerfacecolor="blue", label=f"Best {second_algorithm_name} value: {best_de_value}")
    plt.ylim(0, 20000)
    plt.xlabel("Iteration number")
    plt.ylabel("Best global value")
    plt.legend()
    plt.show()
