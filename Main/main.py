import argparse
import sys
sys.path.append("Q:/BACKUP/UCZELNIA/SEMESTR 6/Techniki sztucznej inteligencji/Artificial Intelligence Techniques")
sys.path.append("Q:/BACKUP/UCZELNIA/SEMESTR 6/Techniki sztucznej inteligencji/Artificial Intelligence Techniques/Exercise_1_PSO_DE")

from Exercise_1_PSO_DE.PSO import PSO


def intro():
    parser = argparse.ArgumentParser(description="exercise_number, static_coefficients, population_number, "
                                                 "function_number, dimensions_number, stop_condition_number, max_iterations_number_or_accuracy")
    parser.add_argument('exercise_number')
    parser.add_argument('static_coefficients')
    parser.add_argument('population_number')
    parser.add_argument('function_number')
    parser.add_argument('dimensions_number')
    parser.add_argument('stop_condition_number')
    parser.add_argument('max_iterations_number_or_accuracy')
    args = parser.parse_args()

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
        if args.exercise_number == '1':
            if args.static_coefficients not in ['true', 'True', 'false', 'False', True, False] \
                    or args.function_number not in ['1', '2', '3', '4'] or args.stop_condition_number not in ['1', '2']:
                exercise1_intro()
            else:
                if args.stop_condition_number == '1':
                    pso = PSO(args.static_coefficients, int(args.population_number), int(args.function_number),
                              int(args.dimensions_number),
                              int(args.max_iterations_number_or_accuracy), None)

                else:
                    pso = PSO(args.static_coefficients, int(args.population_number), int(args.function_number),
                              int(args.dimensions_number), None, float(args.max_iterations_number_or_accuracy))
                global_best = pso.start_algorithm()
                print(global_best)
                print()
                input("Press Enter to continue...")

        elif args.exercise_number == '2':
            print("HI")
        elif args.exercise_number == '3':
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
3). Zakharov
4). Easom""")
    function_number = int(input("Your choice: "))
    while function_number not in [1, 2, 3, 4]:
        int(input("\nPlease choose correct function number: "))

    if function_number == 4:
        dimensions = 2
    else:
        dimensions = int(input("\nProvide dimension number from range (20, 30): "))
        while dimensions < 20 or dimensions > 30:
            dimensions = int(input("\nProvide correct dimension number from range (20, 30): "))

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
            accuracy = 0.001
        elif function_number == 4:
            accuracy = 0.000001

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

