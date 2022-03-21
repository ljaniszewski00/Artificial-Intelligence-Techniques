import argparse
import sys

sys.path.append("C:\\Users\\jakub\\Desktop\\DE\\Artificial-Intelligence-Techniques")
sys.path.append("C:\\Users\\jakub\\Desktop\\DE\\Artificial-Intelligence-Techniques\\Exercise_1_PSO_DE")
sys.path.append("Q:/BACKUP/UCZELNIA/SEMESTR 6/Techniki sztucznej inteligencji/Artificial Intelligence Techniques")
sys.path.append("Q:/BACKUP/UCZELNIA/SEMESTR 6/Techniki sztucznej inteligencji/Artificial Intelligence Techniques/Exercise_1_PSO_DE")

from Exercise_1_PSO_DE.Manager import create_pso_and_de_objects, get_data_for_first_exercise, start_algorithms


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
            stop_condition_number, static_coefficients, population_number, function_number, dimensions_number, \
            max_iterations_number_or_accuracy = get_data_for_first_exercise()

            pso, de = create_pso_and_de_objects(stop_condition_number, static_coefficients, population_number,
                                                function_number, dimensions_number,
                                                max_iterations_number_or_accuracy)

            start_algorithms(pso, de)

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
                stop_condition_number, static_coefficients, population_number, function_number, dimensions_number, \
                max_iterations_number_or_accuracy = get_data_for_first_exercise()

            pso, de = create_pso_and_de_objects(stop_condition_number, static_coefficients, population_number,
                                                function_number, dimensions_number,
                                                max_iterations_number_or_accuracy)
            start_algorithms(pso, de)

        elif exercise_number == 2:
            print("HI")

        elif exercise_number == 3:
            print("HI")


def exercise2_intro():
    print("temp2")


def exercise3_intro():
    print("temp3")


# Beginning of the program execution
intro()
