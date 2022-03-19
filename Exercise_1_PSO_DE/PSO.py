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
import copy
import sys


class PSO:
    def __init__(self, static_coefficients, population_number, function_number, dimensions, particles,
                 max_iterations=None, accuracy=None):
        self.static_coefficients = static_coefficients
        self.population_number = population_number
        self.function_number = function_number
        self.dimensions = dimensions
        self.particles = particles
        self.max_iterations = max_iterations
        self.accuracy = accuracy

        self.current_iteration = 0
        self.w, self.c1, self.c2 = 0.72984, 0.1, 0.9

        self.update_particles_adaptations()
        self.best_global = sys.float_info.max
        self.best_global_positions = [0 for e in range(dimensions)]
        self.best_globals = [self.best_global]
        self.best_globals_iterations = [0]

        self.start_algorithm()

    def update_parameters_values(self):
        self.w = ((0.4 * (self.current_iteration - self.max_iterations)) / pow(self.max_iterations, 2)) + 0.4
        if self.w > 1:
            self.w = 0.5
        self.c1 = (-3 * (self.current_iteration / self.max_iterations)) + 0.1
        self.c2 = (3 * (self.current_iteration / self.max_iterations)) + 0.9

    def update_velocities(self):
        for index, particle in enumerate(self.particles):
            particle.update_velocities(self.w, self.c1, self.c2,
                                       self.best_global_positions)

    def update_particles_positions(self):
        for index, particle in enumerate(self.particles):
            particle.update_positions()

    def update_particles_adaptations(self):
        for particle in self.particles:
            particle.update_adaptation()

    def update_global_best(self):
        for particle in self.particles:
            if particle.adaptation < self.best_global:
                self.best_global = particle.adaptation
                self.best_global_positions = copy.copy(particle.positions)
                self.best_globals.append(self.best_global)
                self.best_globals_iterations.append(self.current_iteration)

    def move_particles(self):
        self.update_velocities()
        if not self.static_coefficients:
            self.update_parameters_values()
        self.update_particles_positions()
        self.update_particles_adaptations()
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
            while self.current_iteration < self.max_iterations:
                self.move_particles()
                self.current_iteration += 1
        else:
            while abs(self.best_global) >= self.accuracy:
                self.move_particles()
                self.current_iteration += 1

        return round(self.best_global, 4), self.best_global_positions, self.best_globals, self.best_globals_iterations, \
               self.current_iteration
