import argparse


def intro():
    parser = argparse.ArgumentParser(description="exercise_number, minimum_or_maximum, variables_number, max_iterations")
    parser.add_argument('exercise_number')
    parser.add_argument('minimum_or_maximum')
    parser.add_argument('variables_number')
    parser.add_argument('max_iterations')
    args = parser.parse_args()

    if args.exercise_number not in ['1', '2', '3'] or args.minimum_or_maximum not in ['minimum', 'maximum']:
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
            user_choice = int(input("\nYour choice: "))
        if user_choice == 1:
            exercise1_intro()
        elif user_choice == 2:
            exercise2_intro()
        elif user_choice == 3:
            exercise3_intro()
    else:
        print("HI")


def exercise1_intro():
    print("------------------------------------------------------------------")
    print("Exercise 1 - Particle Swarm Optimization, Differential Evolution")
    print("------------------------------------------------------------------")
    print("Do you want to find:")
    print("1). minimum")
    print("2). maximum")
    extremum = int(input("Your choice: "))
    variables_number = int(input("\nChoose variables number: "))
    max_iterations = int(input("\nChoose max iterations number: "))


def exercise2_intro():
    print("temp2")


def exercise3_intro():
    print("temp3")


# Beginning of the program execution
intro()

