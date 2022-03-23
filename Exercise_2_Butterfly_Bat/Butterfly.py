"""
The scheme of Butterfly algorithm
1. Generate initial population of butterflies:
    1.1. Assign random starting position from given range for each dimension
    1.2. Calculate Intensity values
2. Define:
    2.1. sensor modality c -
    2.2. power exponent a -
    2.3. switch probability p -
3. Calculate function value from every butterfly positions and determine the best solution
value holds the best solution
4. Until end condition has not been fulfilled (max iteration number or given accuracy):
    4.1. For each butterfly in the population calculate fragrance f with equation:
        f = c(I**a),
        where:
            c - the sensor modality
            I - the stimulus intensity
            a - the power exponent dependent on modality
    4.2. For each butterfly in the population:
        4.2.1. Generate a random number r from 0 to 1
        4.2.2. If r < p,
                then move towards best butterfly / solution with the equation:
                    x = x + (r**2 * gbest - x) * f,
                    where:
                        x - current position
                        r - random value from 0 to 1
                        gbest - currenst best solution's position
                        f - fragrance
                If not,
                then move butterfly randomly with the equation:
                    x = x + (r**2 * xj - xk) * f,
                    where:
                        x - current position
                        r - random value from 0 to 1
                        xj, xk - current positions of two random butterflies from the solution space
                        f - fragrance
        4.2.3. Calculate function value from butterfly positions and determine if it's better than the best solution.
        If yes, save it as the best solution
        4.2.4. Update the value of a

"""
import copy
import random
import sys


class Butterfly:
    def __init__(self, static_coefficients, population_number, function_number, dimensions, butterflies,
                 max_iterations=None, accuracy=None):
        self.static_coefficients = static_coefficients
        self.population_number = population_number
        self.function_number = function_number
        self.dimensions = dimensions
        self.butterflies = butterflies
        self.max_iterations = max_iterations
        self.accuracy = accuracy

        self.current_iteration = 0
        self.c = 0
        self.a = 0
        self.p = 0

        self.update_adaptations_for_whole_population()
        self.best_global = sys.float_info.max
        self.best_global_positions = [0 for e in range(dimensions)]
        self.best_globals = [self.best_global]
        self.best_globals_iterations = [0]

        self.start_algorithm()

    def update_fragrance_for_whole_population(self):
        for butterfly in self.butterflies:
            butterfly.update_fragrance(self.c, self.a)

    def update_adaptations_for_whole_population(self):
        for butterfly in self.butterflies:
            butterfly.update_adaptation()

    def update_butterfly_positions(self, butterfly):
        first_random_butterfly_number = random.randint(0, self.population_number-1)
        second_random_butterfly_number = random.randint(0, self.population_number - 1)
        butterfly.update_positions(self.p, self.best_global_positions,
                                   self.butterflies[first_random_butterfly_number].positions,
                                   self.butterflies[second_random_butterfly_number].positions)

    def update_butterfly_adaptations(self, butterfly):
        butterfly.update_adaptation()

    def update_global_best_for_whole_population(self):
        for butterfly in self.butterflies:
            if butterfly.adaptation < self.best_global:
                self.best_global = butterfly.adaptation
                self.best_global_positions = copy.copy(butterfly.positions)
                self.best_globals.append(self.best_global)
                self.best_globals_iterations.append(self.current_iteration)

    def update_global_best(self, butterfly):
        if butterfly.adaptation < self.best_global:
            self.best_global = butterfly.adaptation
            self.best_global_positions = copy.copy(butterfly.positions)
            self.best_globals.append(self.best_global)
            self.best_globals_iterations.append(self.current_iteration)

    def update_power_exponent(self):
        self.a = 0

    def print_particles_positions(self):
        print()
        print("Particles Positions:")
        for butterfly in self.butterflies:
            print(butterfly.positions)
        print()

    def print_particles_velocities(self):
        print()
        print("Particles Velocities:")
        for butterfly in self.butterflies:
            print(butterfly.velocities)
        print()

    def start_algorithm(self):
        if self.max_iterations is not None:
            while self.current_iteration < self.max_iterations:
                self.update_fragrance_for_whole_population()
                for butterfly in self.butterflies:
                    self.update_butterfly_positions(butterfly)
                    self.update_butterfly_adaptations(butterfly)
                    self.update_global_best(butterfly)
                    self.update_power_exponent()
                self.current_iteration += 1
        else:
            while abs(self.best_global) >= self.accuracy:
                self.update_fragrance_for_whole_population()
                for butterfly in self.butterflies:
                    self.update_butterfly_positions(butterfly)
                    self.update_butterfly_adaptations(butterfly)
                    self.update_global_best(butterfly)
                    self.update_power_exponent()
                self.current_iteration += 1

        return round(self.best_global, 4), self.best_global_positions, self.best_globals, self.best_globals_iterations, \
               self.current_iteration
