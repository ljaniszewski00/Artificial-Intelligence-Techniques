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
                v = wv + (c1 * r1) * (Pbest - Pi) + (c2 * r2) * (Gbest - Pi)
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


class PSO:
    def __init__(self, function, dimension, range, accuracy, extremum, variables_number, max_iterations):
        self.function = function
        self.dimension = dimension
        self.range = range
        self.accuracy = accuracy
        self.extremum = extremum
        self.variables_number = variables_number
        self.max_iterations = max_iterations

        self.current_iteration = 0
        self.particles = [[]]
        self.velocities = [[]]
        self.w = 0.72984
        self.c1, self.c2 = 2.05, 2.05

        self.local_best = []
        self.global_best = None
        self.assign_initial_values()

    def assign_initial_values(self):
        for particle in self.particles:
            for value in particle:
                value.append
        self.local_best = max(self.particle)
        self.global_best = max(self.particle)


    def update_parameters_values(self):
        self.w = ((0.4 * (self.current_iteration - self.max_iterations)) / pow(self.max_iterations, 2)) + 0.4
        self.c1 = (-3 * (self.current_iteration / self.max_iterations)) + 3.5
        self.c2 = (3 * (self.current_iteration / self.max_iterations)) + 0.5


    def move_particles(self):
        new_velocities = []
        for velocity in self.velocities:
            new_velocities.append(velocity * self.w)
        r1 = random.uniform(0, 2)
        r2 = random.uniform(0, 2)
        for index, velocity in enumerate(new_velocities):
            velocity += (self.c1 * r1 * (self.local_best[index] - self.particles[index])) + \
                        (self.c2 * r2 * (self.global_best - self.particles[index]))

        self.particles += self.velocities
        self.current_iteration += 1


