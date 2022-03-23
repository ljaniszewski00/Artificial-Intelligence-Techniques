from Exercise_1_PSO_DE.PSO import PSO
from Exercise_1_PSO_DE.DE import DE
from Exercise_1_PSO_DE.Particle import Particle
from Utils.utils import generate_chart


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

    generate_chart("PSO", pso_best_globals_iterations, pso_best_globals, "DE", de_best_globals_iterations,
                   de_best_globals)

    input("Press Enter to continue...")
