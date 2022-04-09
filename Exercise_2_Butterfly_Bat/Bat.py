"""
The scheme of Bat algorithm
1. Create particles (bats) on the basis of data given by the user (dimensions number, function range, parameters) and:
    1.1. Assign random starting position from given range for each dimension
    1.2. Assign velocity v = rand(1, function_range)
    1.3. Assign pulse rate r = rand(N, 1) or rand(0, 1)
    1.4. Assign loudness A = rand(N, 1) * 2 or rand(0, 1) * 2
    1.5. Assign frequency f = 2 * rand(0, 1) -> (save this rand for later)
2. For every bat from set:
    2.1. Calculate the current value of function with bat's positions
    2.2. Save current position of the bat as it's best local solution
    2.3. If bat's position is better than the global solution, assign it as global one
3. Until end condition has not been fulfilled (max iteration number or given accuracy):
    3.1. For every bat from set:
        3.1.1. Update frequency using the equation:
            f = fmin + (fmax - fmin) * B
                where:
                    fmin - frequency range minimum = 0
                    fmax - frequency range maximum = 1
                    B - random number between 0 and 1
        3.1.2. Update velocity using the equation:
            v = v + (x - xbest) * f
                where:
                    v - bat's velocity
                    x - current bat's position
                    xbest - current global best bat's position
                    f - frequency
        3.1.3. Update positions for every bat with the equation:
            x = x + v
                where:
                    x - bat's position
                    v - bat's velocity
    3.2. For every bat from set:
        3.2.1. If r > rand(0, 1) -> same rand as used in 1.1.5.:
            3.2.1.1. Select a solution among the bats as the best solution (bat with the biggest frequency value)
            3.2.1.2. Generate local solution around best solution with equation:
                x = x + ε * A,
                    where:
                        x - current bat's position
                        ε - random number between -1 and 1
                        A - loudness value
        3.2.2. If rand < A and function value < current best function value, save calculated
        function value as current best solution, reduce loudness and increase pulse rate with equations:
            A = α * A,
                where:
                    A - loudness value
                    α - alpha value - random value between 0 and 1
            r = r * (1 - e ** (-yt)),
                where:
                    r - pulse rate
                    γ - gamma value - random value between 0 and 1
                    t - iteration number
        3.2.3. Calculate bat's function value with it's positions
        3.2.4. If bat's new function value is better than global's best solution, assign it as global's best
"""
import copy
import random

from Utils.utils import calculate_function_value_with_positons


class Bat:
    def __init__(self, static_coefficients, population_number, function_number, dimensions, bats,
                 max_iterations=None, accuracy=None):
        self.static_coefficients = static_coefficients
        self.population_number = population_number
        self.function_number = function_number
        self.dimensions = dimensions
        self.bats = bats
        self.max_iterations = max_iterations
        self.accuracy = accuracy

        self.current_iteration = 0
        self.alpha = 0
        self.gamma = 0

        self.update_adaptations_for_whole_population()
        self.best_global = min(bat.adaptation for bat in self.bats)
        self.best_global_positions = [0 for e in range(dimensions)]
        self.best_globals = [self.best_global]
        self.best_globals_iterations = [0]

        self.start_algorithm()

    def update_adaptations_for_whole_population(self):
        for bat in self.bats:
            bat.update_adaptation()

    def adjust_frequencies(self, bat):
        bat.update_frequency()

    def update_velocities(self, bat):
        bat.update_velocities(self.best_global_positions)

    def update_positions(self, bat):
        bat.update_positions()

    def generate_new_solutions(self, avg_loudness):
        for bat in self.bats:
            self.adjust_frequencies(bat)
            self.update_velocities(bat)
            self.update_positions(bat)
            if random.uniform(0, 1) > bat.pulse_rate:
                self.move_current_solution_to_the_best_solution(bat, avg_loudness)

    def calculate_avg_loudness(self):
        loudness = 0
        for bat in self.bats:
            loudness += bat.loudness
        avg_loudness = loudness / self.population_number
        return avg_loudness

    def move_current_solution_to_the_best_solution(self, bat, avg_loudness):
        bat.move_current_solution_to_the_best_solution(self.best_global, avg_loudness)

    def generate_new_solution_by_flying_randomly(self, bat):
        new_solution = bat.generate_new_solution_by_flying_randomly()
        return new_solution

    def check_condition(self, bat, new_solution):
        if random.uniform(0, 1) < bat.loudness and calculate_function_value_with_positons(self.function_number, new_solution) < self.best_global:
            return True
        else:
            return False

    def accept_new_solution(self, bat, new_solution):
        bat.accept_new_solution(new_solution)

    def update_pulse_rate_and_loudness(self, bat):
        bat.update_pulse_rate_and_loudness(self.alpha, self.gamma, self.current_iteration)

    def find_current_best(self):
        for bat in self.bats:
            if bat.adaptation < self.best_global:
                self.best_global = bat.adaptation
                self.best_global_positions = copy.copy(bat.positions)
                self.best_globals.append(self.best_global)
                self.best_globals_iterations.append(self.current_iteration)

    def execute_algorithm_operations(self):
        avg_loudness = self.calculate_avg_loudness()
        self.generate_new_solutions(avg_loudness)
        for bat in self.bats:
            new_solution = self.generate_new_solution_by_flying_randomly(bat)
            if self.check_condition(bat, new_solution):
                self.accept_new_solution(bat, new_solution)
                self.update_pulse_rate_and_loudness(bat)
        self.update_adaptations_for_whole_population()
        self.find_current_best()
        self.current_iteration += 1

    def start_algorithm(self):
        if self.max_iterations is not None:
            while self.current_iteration < self.max_iterations:
                print(self.best_global)
                print()
                self.execute_algorithm_operations()
        else:
            while abs(self.best_global) >= self.accuracy:
                self.execute_algorithm_operations()

        return round(self.best_global, 4), self.best_global_positions, self.best_globals, \
               self.best_globals_iterations, self.current_iteration
