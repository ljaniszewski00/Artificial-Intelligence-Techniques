"""
The scheme of PSO algorithm
1. For every particle from set:
    1.1. Assign random starting position from given range
    1.2. Calculate the current value of function with every particle's position
    1.3. Save current position of the particle as it's best local solution
    1.4. If particle's position is better than the global solution, assign it as global one
    1.5. Assign random starting velocities for all particles
2. If end condition has not been made (max iteration number or given accuracy):
    2.1. For every particle from set:
        2.1.1. Update velocities for every particle with the formula:
                v = w * v + (c1 * r1) * (Pbest - Pi) + (c2 * r2) * (Gbest - Pi)
                    where:
                        v - particle's velocity
                        w - static parameter = 0.72984
                        c1, c2 - static parameters = 2.05
                        r1, r2 - weights with random values from set [0, 2]
                        Pbest - current particle's best solution
                        Gbest - global best solution
                        Pi - current solution
                        
                    additionally, parameters w, c1, c2 can be updated, for better results, over the iterations with
                    formulas:
                        w = ((0.4 * (t - N)) / N^2) + 0.4
                        c1 = (-3 * (t / N)) + 3.5
                        c2 = (3 * (t / N)) + 0.5
                        
                        where:
                        t - current iteration
                        N - all iterations number
        2.1.2. Update positions for every particle with the formula:
                Pi = Pi + v
                    where:
                        Pi - particle's position
                        v - particle's velocity
        2.1.3. If particle's new position is better than local's best solution, assign it as local's best
        2.1.4. If particle's new position is better than global's best solution, assign it as global's best


Questions:
    - I assume that particle is one list of different values?
    - How to determine particles number?
    - All particles and it's velocities list can both look like this?:
        [ []
        []
        []
        .
        .
        .
        [] ]
    - what is dimension, range of x, accuracy in test file?

"""
import random
import numpy as np
from Exercise_1_PSO_DE.utils import calculate_function_value


class PSO:
    def __init__(self, coefficients_changed_over_iterations, population_number, function_number, dimension,
                 max_iterations=None, accuracy=None):
        self.coefficients_changed_over_iterations = coefficients_changed_over_iterations
        self.population_number = population_number
        self.function_number = function_number
        self.dimension = dimension
        self.max_iterations = max_iterations
        self.accuracy = accuracy

        self.current_iteration = 0
        self.w, self.c1, self.c2 = 0.72984, 2.05, 2.05
        if function_number == 1:
            self.range = [-100, 100]
        elif function_number == 2 or function_number == 3:
            self.range = [-10, 10]

        self.particles = [[random.uniform(self.range[0], self.range[1]) for e in range(self.dimension)] for e in range(self.population_number)]
        self.velocities = [[0 for e in range(self.dimension)] for e in range(self.population_number)]

        # self.particles = np.random.random_integers(self.range[0], self.range[1], (self.population_number, self.dimension))
        # self.velocities = np.zeros((self.population_number, self.dimension))

        self.local_best = []
        for particle_number in range(self.population_number):
            row_values = []
            for dimension_number in range(self.dimension):
                row_values.append(calculate_function_value(self.function_number, self.population_number,
                                                           self.particles[particle_number][dimension_number]))
            self.local_best.append(min(row_values))

        self.global_best = min(self.local_best)

        self.start_algorithm()

    def update_parameters_values(self):
        self.w = ((0.4 * (self.current_iteration - self.max_iterations)) / pow(self.max_iterations, 2)) + 0.4
        self.c1 = (-3 * (self.current_iteration / self.max_iterations)) + 3.5
        self.c2 = (3 * (self.current_iteration / self.max_iterations)) + 0.5

    def update_velocities(self):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)

        for particle_number in range(self.population_number):
            for dimension_number in range(self.dimension):
                new_velocity = self.w * self.velocities[particle_number][dimension_number]
                new_velocity += (self.c1 * r1) * (
                            self.local_best[particle_number] - self.particles[particle_number][dimension_number])
                new_velocity += (self.c2 * r2) * (self.global_best - self.particles[particle_number][dimension_number])
                self.velocities[particle_number][dimension_number] = new_velocity

    def update_particles(self):
        for row_number in range(self.population_number):
            for column_number in range(self.dimension):
                if self.particles[row_number][column_number] >= self.range[1]:
                    self.particles[row_number][column_number] -= self.velocities[row_number][column_number]
                else:
                    self.particles[row_number][column_number] += self.velocities[row_number][column_number]

    def update_bests(self):
        for row_number in range(self.population_number):
            for column_number in range(self.dimension):
                function_value = calculate_function_value(self.function_number, self.population_number,
                                                          self.particles[row_number][column_number])
                if function_value < self.local_best[row_number]:
                    self.local_best[row_number] = function_value
                if function_value < self.global_best:
                    self.global_best = function_value

    def move_particles(self):
        self.update_velocities()
        if self.coefficients_changed_over_iterations:
            self.update_parameters_values()
        self.update_particles()
        self.update_bests()

    def print_particles(self):
        print()
        for row_number in range(self.population_number):
            print(self.particles[row_number])
        print()

    def start_algorithm(self):
        if self.max_iterations is not None:
            while self.current_iteration <= self.max_iterations:
                self.move_particles()
                self.print_particles()
                self.current_iteration += 1
        else:
            while self.global_best >= self.accuracy:
                self.move_particles()
                self.print_particles()
                self.current_iteration += 1

        return self.global_best



