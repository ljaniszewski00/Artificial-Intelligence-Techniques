import random
import copy
from Exercise_1_PSO_DE.utils import calculate_function_value


class Particle:
    def __init__(self, function_number, function_range, dimensions):
        self.function_number = function_number
        self.function_range = function_range
        self.dimensions = dimensions
        self.positions = [random.uniform(function_range[0], function_range[1]) for e in range(dimensions)]
        self.velocities = [0 for e in range(dimensions)]
        self.adaptation = calculate_function_value(self.function_number, self)
        self.best_adaptation = self.adaptation
        self.best_adaptation_positions = copy.copy(self.positions)

    def update_adaptation(self):
        self.adaptation = calculate_function_value(self.function_number, self)
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_adaptation_positions = copy.copy(self.positions)

    def update_positions(self):
        for dimension in range(self.dimensions):
            self.positions[dimension] += self.velocities[dimension]

    def update_velocities(self, w, c1, c2, global_best_positions):
        for dimension in range(self.dimensions):
            r1 = random.uniform(0, 2)
            r2 = random.uniform(0, 2)
            interia = w * self.velocities[dimension]
            cognitive = (c1 * r1) * (
                    self.best_adaptation_positions[dimension] - self.positions[dimension])
            social = (c2 * r2) * (global_best_positions[dimension] - self.positions[dimension])

            new_velocity = interia + cognitive + social

            if new_velocity < self.function_range[0]:
                new_velocity = self.function_range[0]
            elif new_velocity > self.function_range[1]:
                new_velocity = self.function_range[1]

            self.velocities[dimension] = new_velocity