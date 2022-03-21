from Exercise_1_PSO_DE.PSO import PSO
from Exercise_1_PSO_DE.DE import DE
from Exercise_1_PSO_DE.Particle import Particle
from Exercise_1_PSO_DE.utils import generate_chart


def create_pso_and_de_objects(stop_condition_number, static_coefficients, population_number, function_number,
                              dimensions_number, max_iterations_number_or_accuracy):
    function_range = [-100, 100]
    if function_number == 1:
        function_range = [-100, 100]
    elif function_number == 2:
        function_range = [-10, 10]
    elif function_number == 3:
        function_range = [-2.048, 2.048]

    # Creating particles
    particles = [Particle(function_number, function_range, dimensions_number) for e in
                 range(int(population_number))]
    # Parsing to vectors
    particles_for_de = [e.get_particle_as_vector() for e in particles]

    if stop_condition_number == 1:
        # Creating PSO and DE objects with max iterations number specified
        pso = PSO(static_coefficients, population_number, function_number,
                  dimensions_number, particles, max_iterations_number_or_accuracy, None)

        de = DE(particles_for_de, function_number, static_coefficients, max_iterations_number_or_accuracy,
                None)

        return pso, de
    else:
        # Creating PSO and DE objects with desired accuracy specified
        pso = PSO(static_coefficients, population_number, function_number,
                  dimensions_number, particles, None, max_iterations_number_or_accuracy)

        de = DE(particles_for_de, function_number, static_coefficients, None,
                max_iterations_number_or_accuracy)

        return pso, de


def get_data_for_first_exercise():
    print()
    print("------------------------------------------------------------------")
    print("Exercise 1 - Particle Swarm Optimization, Differential Evolution")
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

    max_iterations = None
    accuracy = None

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
        if function_number == 1:
            accuracy = 0.0001
        elif function_number == 2:
            accuracy = 0.000001
        elif function_number == 3:
            accuracy = 30

        return stop_condition, static_coefficients, population_number, function_number, dimensions_number, accuracy


def start_algorithms(pso, de):
    # Starting PSO and DE algorithms and displaying results in console and on charts
    pso_best_global, pso_best_global_positions, pso_best_globals, pso_best_globals_iterations, \
    pso_iterations_passed = pso.start_algorithm()
    de_best_global, de_best_globals, de_iterations_passed = de.doDE()

    print("PSO:")
    print(f"A minimum of a function was found and it is equal to: {pso_best_global}")
    print()
    print(f"{pso_iterations_passed} iterations passed until the solution was found")
    print()

    de_best_globals_iterations = [d['iteration'] for d in de_best_globals]
    de_best_globals = [d['global_best'] for d in de_best_globals]

    print("DE:")
    print(f"A minimum of a function was found and it is equal to: {de_best_global}")
    print()
    print(f"{de_iterations_passed} iterations passed until the solution was found")
    print()

    generate_chart(pso_best_globals_iterations, pso_best_globals, de_best_globals_iterations,
                   de_best_globals)

    input("Press Enter to continue...")
