from Exercise_2_Butterfly_Bat.Bat import Bat
from Exercise_2_Butterfly_Bat.Butterfly import Butterfly
from Exercise_2_Butterfly_Bat.Bat_Particle import BatParticle
from Exercise_2_Butterfly_Bat.Butterfly_Particle import ButterflyParticle
from Utils.utils import generate_chart


def create_butterfly_and_bat_objects(stop_condition_number, static_coefficients, population_number, function_number,
                                     dimensions_number, max_iterations_number_or_accuracy):
    function_range = [-100, 100]
    if function_number == 1:
        function_range = [-100, 100]
    elif function_number == 2:
        function_range = [-10, 10]
    elif function_number == 3:
        function_range = [-2.048, 2.048]

    # Creating bats
    bats = [BatParticle(function_number, function_range, dimensions_number) for e in range(int(population_number))]

    # Creating butterflies
    butterlies = [ButterflyParticle(function_number, function_range, dimensions_number) for e in range(int(population_number))]

    if stop_condition_number == 1:
        # Creating Bat and Butterfly algorithms objects with max iterations number specified
        bat_algorithm = Bat(static_coefficients, population_number, function_number, dimensions_number, bats,
                            max_iterations_number_or_accuracy, None)

        butterfly_algorithm = Butterfly(static_coefficients, population_number, function_number, dimensions_number,
                                        butterlies, max_iterations_number_or_accuracy, None)

        return bat_algorithm, butterfly_algorithm
    else:
        # Creating Bat and Butterfly algorithms objects with desired accuracy specified
        bat_algorithm = Bat(static_coefficients, population_number, function_number, dimensions_number, bats, None,
                            max_iterations_number_or_accuracy)

        butterfly_algorithm = Butterfly(static_coefficients, population_number, function_number, dimensions_number,
                                        butterlies, None, max_iterations_number_or_accuracy)

        return bat_algorithm, butterfly_algorithm


def start_algorithms(bat_algorithm, butterfly_algorithm):
    # Starting Bat and Butterfly algorithms and displaying results in console and on charts
    bat_best_global, bat_best_global_positions, bat_best_globals, bat_best_globals_iterations, \
    bat_iterations_passed = bat_algorithm.start_algorithm()

    butterfly_best_global, butterfly_best_global_positions, butterfly_best_globals, butterfly_best_globals_iterations, \
    butterfly_iterations_passed = butterfly_algorithm.start_algorithm()

    print("Bat algorithm:")
    print(f"A minimum of a function was found and it is equal to: {bat_best_global}")
    print()
    print(f"{bat_iterations_passed} iterations passed until the solution was found")
    print()

    print("Butterfly algorithm:")
    print(f"A minimum of a function was found and it is equal to: {butterfly_best_global}")
    print()
    print(f"{butterfly_iterations_passed} iterations passed until the solution was found")
    print()

    generate_chart("Bat", bat_best_globals_iterations, bat_best_globals, "Butterfly", butterfly_best_globals_iterations,
                   butterfly_best_globals)

    input("Press Enter to continue...")
