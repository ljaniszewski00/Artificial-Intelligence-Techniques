import sys

def intro():
    while True:
        print("------------------------------------------------------------------")
        print("Artificial Intelligence Techniques")
        print("Lukasz Janiszewski, Jakub Muszynski")
        print()
        print("Choose which exercise's algorithms you would like to use:")
        print("Exercise 1 - Particle Swarm Optimization, Differential Evolution")
        print("Exercise 2 - ")
        print("Exercise 3 - ")
        print()
        user_choice = int(input("Your choice: "))
        while user_choice not in [1, 2, 3]:
            print("Please choose option 1 or 2 or 3!")
            user_choice = int(input("\nYour choice: "))
        if user_choice == 1:
            exercise1_intro()
        elif user_choice == 2:
            sys.exit()
        elif user_choice == 3:
            sys.exit()


def exercise1_intro():
    print("------------------------------------------------------------------")
    print("Exercise 1 - Particle Swarm Optimization, Differential Evolution")
    print("------------------------------------------------------------------")
    variables_number = int(input("\nChoose variables number: "))



intro()

