import random
import copy
import numpy as np
from Utils.utils import calculate_function_value


class ButterflyParticle:
    def __init__(self, function_number, function_range, dimensions):
        self.function_number = function_number
        self.function_range = function_range
        self.dimensions = dimensions
        self.positions = [random.uniform(function_range[0], function_range[1]) for e in range(dimensions)]

        self.f = 0
        self.I = 0

        self.adaptation = calculate_function_value(self.function_number, self)
        self.best_adaptation = self.adaptation
        self.best_adaptation_positions = copy.copy(self.positions)

    def update_adaptation(self):
        self.adaptation = calculate_function_value(self.function_number, self)
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_adaptation_positions = copy.copy(self.positions)

    def update_fragrance(self, c, a):
        self.f = c * pow(self.I, a)

    def update_positions(self, p, global_best_positions, first_random_butterfly_positions,
                         second_random_butterfly_positions):
        r = random.uniform(0, 1)
        if p < r:
            for dimension in range(self.dimensions):
                self.positions[dimension] += (pow(r, 2) * global_best_positions[dimension] - self.positions[dimension]) \
                                             * self.f

                if self.positions[dimension] < self.function_range[0]:
                    self.positions[dimension] = self.function_range[0]
                elif self.positions[dimension] > self.function_range[1]:
                    self.positions[dimension] = self.function_range[1]
        else:
            for dimension in range(self.dimensions):
                self.positions[dimension] += (pow(r, 2) * first_random_butterfly_positions[dimension] -
                                              second_random_butterfly_positions[dimension]) * self.f

                if self.positions[dimension] < self.function_range[0]:
                    self.positions[dimension] = self.function_range[0]
                elif self.positions[dimension] > self.function_range[1]:
                    self.positions[dimension] = self.function_range[1]
