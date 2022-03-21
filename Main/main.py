import argparse
import sys

sys.path.append("Q:/BACKUP/UCZELNIA/SEMESTR 6/Techniki sztucznej inteligencji/Artificial Intelligence Techniques")
sys.path.append(
    "Q:/BACKUP/UCZELNIA/SEMESTR 6/Techniki sztucznej inteligencji/Artificial Intelligence Techniques/Exercise_1_PSO_DE")

from Exercise_1_PSO_DE.PSO import PSO
from Exercise_1_PSO_DE.Particle import Particle
from Exercise_1_PSO_DE.utils import generate_chart


def intro():
    # Parsing arguments given by user along with program execution
    parser = argparse.ArgumentParser(description="exercise_number, static_coefficients, population_number, "
                                                 "function_number, dimensions_number, stop_condition_number, "
                                                 "max_iterations_number_or_accuracy")
    parser.add_argument('exercise_number')
    parser.add_argument('static_coefficients')
    parser.add_argument('population_number')
    parser.add_argument('function_number')
    parser.add_argument('dimensions_number')
    parser.add_argument('stop_condition_number')
    parser.add_argument('max_iterations_number_or_accuracy')
    args = parser.parse_args()

    # Checking if correct number of exercise was given
    if args.exercise_number not in ['1', '2', '3']:
        print("------------------------------------------------------------------")
        print("Artificial Intelligence Techniques")
        print("Lukasz Janiszewski, Jakub Muszynski")
        print()
        print("Choose which exercise's algorithms you would like to use:")
        print("1 - Particle Swarm Optimization, Differential Evolution")
        print("2 - ")
        print("3 - ")
        print()
        user_choice = int(input("Your choice: "))
        while user_choice not in [1, 2, 3]:
            print("Please choose option 1 or 2 or 3!")
            user_choice = int(input("Your choice: "))
        if user_choice == 1:
            exercise1_intro()
        elif user_choice == 2:
            exercise2_intro()
        elif user_choice == 3:
            exercise3_intro()
    else:
        # Assigning args to variables
        exercise_number = int(args.exercise_number)
        static_coefficients = True
        if args.static_coefficients not in [True, 'True', 'true', 'T', 't']:
            static_coefficients = False
        population_number = int(args.population_number)
        function_number = int(args.function_number)
        dimensions_number = int(args.dimensions_number)
        stop_condition_number = int(args.stop_condition_number)
        if stop_condition_number == 1:
            # If stop condition was max iterations number we want to cast it as INT
            max_iterations_number_or_accuracy = int(args.max_iterations_number_or_accuracy)
        else:
            # If stop condition was desired accuracy we want to cast it as FLOAT
            max_iterations_number_or_accuracy = float(args.max_iterations_number_or_accuracy)

        if exercise_number == 1:
            # Some more checking
            if static_coefficients not in [True, False] \
                    or function_number not in [1, 2, 3] or stop_condition_number not in [1, 2]:
                exercise1_intro()
            else:

                # Setting function range depending on selected function
                function_range = [-100, 100]
                if args.function_number == 1:
                    function_range = [-100, 100]
                elif args.function_number == 2:
                    function_range = [-10, 10]
                elif args.function_number == 3:
                    function_range = [-2.048, 2.048]

                # Creating particles
                particles = [Particle(function_number, function_range, dimensions_number) for e in
                             range(int(population_number))]
                # Parsing to vectors
                particles_for_de = [e.get_particle_as_vector() for e in particles]

                if args.stop_condition_number == '1':
                    # Creating PSO with max iterations number specified
                    pso = PSO(static_coefficients, population_number, function_number,
                              dimensions_number, particles, max_iterations_number_or_accuracy, None)

                else:
                    # Creating PSO with desired accuracy specified
                    pso = PSO(static_coefficients, population_number, function_number,
                              dimensions_number, particles, None, max_iterations_number_or_accuracy)

                # Starting PSO algorithm and displaying results
                best_global, best_global_positions, best_globals, best_globals_iterations, iterations_passed = pso.start_algorithm()
                print(f"A minimum of a function was found and it is equal to: {best_global}")
                print()
                print(f"A minimum of a function is located at: {best_global_positions}")
                print()
                print(f"{iterations_passed} iterations passed until the solution was found")
                print()
                generate_chart(best_globals_iterations, best_globals)
                input("Press Enter to continue...")

        elif exercise_number == 2:
            print("HI")

        elif exercise_number == 3:
            print("HI")


def exercise1_intro():
    print()
    print("------------------------------------------------------------------")
    print("Exercise 1 - Particle Swarm Optimization, Differential Evolution")
    print("------------------------------------------------------------------")
    coefficient_method = str(input("\nDo you wish to use static, fixed coefficient? Y/N: "))
    coefficient_method = coefficient_method.lower()
    while coefficient_method not in ['y', 'n']:
        coefficient_method = str(input("\nDo you wish to use static, fixed coefficient? Y/N: "))
        coefficient_method = coefficient_method.lower()
    coefficients_changed_over_iterations = False
    if coefficient_method == 'y':
        coefficients_changed_over_iterations = False
    elif coefficient_method == 'n':
        coefficients_changed_over_iterations = True

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

    dimensions = int(input("\nProvide dimensions number: "))
    while dimensions <= 0:
        dimensions = int(input("\nProvide correct dimensions number: "))

    print("""
Choose algorithm stop condition:
1). max iterations
2). achieved accuracy""")
    stop_condition = int(input("Your choice: "))
    while stop_condition not in [1, 2]:
        stop_condition = int(input("Please provide correct stop condition number: "))

    max_iterations = None
    accuracy = None
    if stop_condition == 1:
        max_iterations = int(input("\nChoose max iterations number: "))
    else:
        if function_number == 1:
            accuracy = 0.0001
        elif function_number == 2:
            accuracy = 0.000001
        elif function_number == 3:
            accuracy = 30

    pso = PSO(coefficients_changed_over_iterations, population_number, function_number, dimensions, max_iterations,
              accuracy)
    global_best = pso.start_algorithm()
    print(global_best)


def exercise2_intro():
    print("temp2")


def exercise3_intro():
    print("temp3")


# Beginning of the program execution
intro()
