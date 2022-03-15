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
"""
import random
import numpy as np
from Exercise_1_PSO_DE.utils import calculate_function_value


class Particle:
    def __init__(self, function_number, function_range, dimensions):
        self.function_number = function_number
        self.function_range = function_range
        self.dimensions = dimensions
        self.positions = [random.uniform(function_range[0], function_range[1]) for e in range(dimensions)]
        self.velocities = [0 for e in range(dimensions)]
        self.local_best = calculate_function_value(self.function_number, self)
        self.local_best_position = self.positions
        self.only_one = False

    def update_local_best(self):
        function_value = calculate_function_value(self.function_number, self)
        if function_value < self.local_best:
            self.local_best = function_value
            self.local_best_position = self.positions

    def update_positions(self):
        for position_number in range(len(self.positions)):
            # if self.positions[position_number] >= self.function_range[1]:
            #     self.positions[position_number] -= self.velocities[position_number]
            # else:
            #     self.positions[position_number] += self.velocities[position_number]
            self.positions[position_number] += self.velocities[position_number]

            # if self.positions[position_number] > self.function_range[1]:
            #     self.positions[position_number] = self.function_range[1]
            #
            # if self.positions[position_number] < self.function_range[0]:
            #     self.positions[position_number] = self.function_range[0]

            # if self.position_values_raising[position_number]:
            #     if self.positions[position_number] >= self.function_range[1]:
            #         self.position_values_raising[position_number] = False
            #         self.positions[position_number] -= self.velocities[position_number]
            #     else:
            #         self.positions[position_number] += self.velocities[position_number]
            #     # self.positions[position_number] = round(self.positions[position_number], 6)
            # else:
            #     if self.positions[position_number] <= self.function_range[0]:
            #         self.position_values_raising[position_number] = True
            #         self.positions[position_number] += self.velocities[position_number]
            #     else:
            #         self.positions[position_number] -= self.velocities[position_number]
            #     # self.positions[position_number] = round(self.positions[position_number], 6)

    def update_velocities(self, w, c1, r1, c2, r2, global_best_positions):
        for velocity_number in range(len(self.velocities)):
            if not self.only_one:
                print()
                print(f"w = {w}")
                print(f"velocity value for w = {self.velocities[velocity_number]}")
                print(f"c1 = {c1}")
                print(f"r1 = {r1}")
                print(f"local_best = {self.local_best}")
                print(f"position value for cognitive = {self.positions[velocity_number]}")
                print(f"c2 = {c2}")
                print(f"r2 = {r2}")
                print(f"global_best = {global_best_positions}")
                print(f"position value for social = {self.positions[velocity_number]}")
                # print(f"new_velocity = {new_velocity}")
                print()

            interia = w * self.velocities[velocity_number]
            cognitive = (c1 * r1) * (
                    self.local_best_position[velocity_number] - self.positions[velocity_number])
            social = (c2 * r2) * (global_best_positions - self.positions[velocity_number])

            new_velocity = interia + cognitive + social
            self.velocities[velocity_number] = round(new_velocity, 6)

            if not self.only_one:
                print()
                print(f"w = {w}")
                print(f"velocity value for w = {self.velocities[velocity_number]}")
                print(f"c1 = {c1}")
                print(f"r1 = {r1}")
                print(f"local_best = {self.local_best}")
                print(f"position value for cognitive = {self.positions[velocity_number]}")
                print(f"c2 = {c2}")
                print(f"r2 = {r2}")
                print(f"global_best = {global_best_positions}")
                print(f"position value for social = {self.positions[velocity_number]}")
                print(f"new_velocity = {new_velocity}")
                print()

            self.only_one = True


class PSO:
    def __init__(self, coefficients_changed_over_iterations, population_number, function_number, dimensions,
                 max_iterations=None, accuracy=None):
        self.coefficients_changed_over_iterations = coefficients_changed_over_iterations
        self.population_number = population_number
        self.function_number = function_number
        self.dimensions = dimensions
        self.max_iterations = max_iterations
        self.accuracy = accuracy

        self.current_iteration = 0
        self.w, self.c1, self.c2 = 0.72984, 3.5, 0.5
        if function_number == 1:
            self.function_range = [-100, 100]
        elif function_number in [2, 3, 4]:
            self.function_range = [-10, 10]

        self.particles = [Particle(self.function_number, self.function_range, self.dimensions) for e in
                          range(self.population_number)]

        # Updating global best
        local_bests = {}
        for particle in self.particles:
            local_bests[particle.local_best] = particle.local_best_position
        self.global_best = min(list(local_bests.keys()))
        self.global_best_positions = min(list(local_bests.values()))
        # Updating global best

        self.start_algorithm()

    def update_parameters_values(self):
        self.w = ((0.4 * (self.current_iteration - self.max_iterations)) / pow(self.max_iterations, 2)) + 0.4
        if self.w > 1:
            self.w = 0.5
        self.c1 = (-3 * (self.current_iteration / self.max_iterations)) + 3.5
        self.c2 = (3 * (self.current_iteration / self.max_iterations)) + 0.5

    def update_velocities(self):
        r1 = random.uniform(0, 2)
        r2 = random.uniform(0, 2)

        for particle in self.particles:
            particle.update_velocities(self.w, self.c1, r1, self.c2, r2, self.global_best)

    def update_particles_positions(self):
        for particle in self.particles:
            particle.update_positions()

    def update_particles_local_bests(self):
        for particle in self.particles:
            particle.update_local_best()

    def update_global_best(self):
        local_bests = {}
        for particle in self.particles:
            local_bests[particle.local_best] = particle.local_best_position
        minimal_local_best = min(list(local_bests.keys()))
        if minimal_local_best < self.global_best:
            self.global_best = minimal_local_best
            self.global_best_positions = min(list(local_bests.values()))

    def move_particles(self):
        self.update_velocities()
        if self.coefficients_changed_over_iterations:
            self.update_parameters_values()
        self.update_particles_positions()
        self.update_particles_local_bests()
        self.update_global_best()

    def print_particles_positions(self):
        print()
        print("Particles Positions:")
        for particle in self.particles:
            print(particle.positions)
        print()

    def print_particles_velocities(self):
        print()
        print("Particles Velocities:")
        for particle in self.particles:
            print(particle.velocities)
        print()

    def start_algorithm(self):
        if self.max_iterations is not None:
            while self.current_iteration <= self.max_iterations:
                print()
                print(f"Current iteration: {self.current_iteration}")
                self.print_particles_velocities()
                self.print_particles_positions()

                self.move_particles()

                self.print_particles_velocities()
                self.print_particles_positions()

                # print(f"w = {self.w}")
                # print(f"c1 = {self.c1}")
                # print(f"c2 = {self.c2}")
                # print(f"Global best before moving particles: {self.global_best}")
                # print(f"Global best after moving particles: {self.global_best}")
                self.current_iteration += 1
        else:
            while self.global_best >= self.accuracy:
                self.move_particles()
                # self.print_particles()
                self.current_iteration += 1

        return self.global_best
