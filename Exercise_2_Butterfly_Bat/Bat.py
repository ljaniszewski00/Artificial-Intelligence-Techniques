"""
The scheme of Bat algorithm
1. Create particles (bats) on the basis of data given by the user (dimensions number, function range, parameters) and
for every bat:
    1.1. Assign random starting position from given range for each dimension
    1.2. Assign random velocities from given range for each dimension
    1.3. Assign pulse rate r as random number from range (0, 1)
    1.4. Assign loudness A as random number from range (1, 2)
    1.5. Save initial pulse rate and loudness for later change of these parameters
    1.5. Assign frequency = 0, minimum frequency = 0 and maximum frequency = 2
2. Set parameters for algorithm:
    2.1. Set gamma = 0.5
    2.2. Set alpha = 0.5
3. For every bat from set:
    3.1. Calculate the current value of function with bat's positions
    3.2. Save current position of the bat as it's best local solution
    3.3. If bat's position is better than the global solution, assign it as global one
4. Until end condition has not been fulfilled (max iteration number or given accuracy):
    4.1. For every bat from set:
        4.1.1. Update velocity using the equation:
            v = v + (xbest - x) * f
                where:
                    v - bat's velocity
                    x - current bat's position
                    xbest - current best global solution
                    f - frequency
        4.1.2. Update positions for every bat with the equation:
            x = x + v
                where:
                    x - bat's position
                    v - bat's velocity
        4.1.3. Update it's adaptation (calculate function value)
        4.1.4. Update frequency using the equation:
            f = fmin + (fmax - fmin) * B
                where:
                    fmin - frequency range minimum = 0
                    fmax - frequency range maximum = 1
                    B - random number between 0 and 1
    4.2. Determine best global value along with position of the bat that achieved it
    4.3. For every bat from set:
        4.3.1. If pulse rate > random value from range (0, 1):
            4.3.1.1. Update bat's position:
                x = x + ε * A,
                    where:
                        x - current bat's position
                        ε - random number between -1 and 1
                        A - loudness value of current bat OR average loudness value of all bats
        4.3.2. If rand < A and function value < current best function value, save calculated
        function value as current best solution, reduce loudness and increase pulse rate with equations:
            A = α * A,
                where:
                    A - loudness value OR initial loudness value
                    α - alpha value - random value between 0 and 1
            r = r * (1 - e ** (-yt)),
                where:
                    r - pulse rate value OR initial pulse rate value
                    γ - gamma value - random value between 0 and 1
                    t - iteration number
    4.4 Determine best global value along with position of the bat that achieved it
"""
import copy
import random
from Utils.utils import calculate_function_value


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
        self.gamma = 0.5
        self.alpha = 0.5

        self.update_adaptations_for_whole_population()
        self.best_global = min(bat.adaptation for bat in self.bats)
        self.best_global_positions = [0 for e in range(dimensions)]
        self.best_globals = [self.best_global]
        self.best_globals_iterations = [0]

        self.start_algorithm()

    def update_bats_frequency(self, bat):
        bat.update_frequency()

    def update_bats_velocities(self, bat):
        bat.update_velocities(self.best_global_positions)

    def calculate_avg_loudness(self):
        avg_loudness = 0
        for bat in self.bats:
            avg_loudness += bat.loudness
        return avg_loudness / self.population_number

    def update_bats_positions(self, bat, second_time=False, avg_loudness=None):
        if not second_time:
            bat.update_positions()
        else:
            bat.update_positions(True, avg_loudness)

    def update_adaptations_for_whole_population(self):
        for bat in self.bats:
            bat.update_adaptation()

    def update_bats_adaptations(self, bat):
        bat.update_adaptation()

    def update_bats_pulse_rate_and_loudness(self, bat):
        rand = random.uniform(0, 1)
        if rand < bat.loudness and calculate_function_value(self.function_number, bat) < self.best_global:
            bat.update_pulse_rate_and_loudness(self.gamma, self.alpha, self.current_iteration)

    def update_global_best(self):
        for bat in self.bats:
            if bat.adaptation < self.best_global:
                self.best_global = bat.adaptation
                self.best_global_positions = copy.copy(bat.positions)
                self.best_globals.append(self.best_global)
                self.best_globals_iterations.append(self.current_iteration)

    def print_particles_positions(self):
        print()
        print("Particles Positions:")
        for bat in self.bats:
            print(bat.positions)
        print()

    def print_particles_velocities(self):
        print()
        print("Particles Velocities:")
        for bat in self.bats:
            print(bat.velocities)
        print()

    def execute_algorithm_operations(self):
        avg_loudness = self.calculate_avg_loudness()
        for bat in self.bats:
            self.update_bats_velocities(bat)
            self.update_bats_positions(bat)
            self.update_bats_adaptations(bat)
            self.update_bats_frequency(bat)
        self.update_global_best()
        for bat in self.bats:
            self.update_bats_positions(bat, True, avg_loudness)
            self.update_bats_pulse_rate_and_loudness(bat)
        self.update_global_best()
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
