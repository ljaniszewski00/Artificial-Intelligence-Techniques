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

        self.c = random.uniform(0, 1)
        self.a = random.uniform(0, 1)
        self.p = random.uniform(0, 1)

        self.adaptation = calculate_function_value(self.function_number, self)
        self.I = self.adaptation

        self.F = self.c * pow(self.I, self.a)

    def update_adaptation(self):
        self.adaptation = calculate_function_value(self.function_number, self)

    def update_fragrance(self):
        self.F = self.c * pow(self.I, self.a)

    def update_power_exponent(self):
        pass

    def update_positions(self, global_best, first_random_butterfly_positions,
                         second_random_butterfly_positions):
        r = random.uniform(0, 1)
        if r < self.p:
            for dimension in range(self.dimensions):
                self.positions[dimension] += (pow(r, 2) * global_best - self.positions[dimension]) \
                                             * self.F

                if self.positions[dimension] < self.function_range[0]:
                    self.positions[dimension] = self.function_range[0]
                elif self.positions[dimension] > self.function_range[1]:
                    self.positions[dimension] = self.function_range[1]
        else:
            for dimension in range(self.dimensions):
                self.positions[dimension] += (pow(r, 2) * first_random_butterfly_positions[dimension] -
                                              second_random_butterfly_positions[dimension]) * self.F

                if self.positions[dimension] < self.function_range[0]:
                    self.positions[dimension] = self.function_range[0]
                elif self.positions[dimension] > self.function_range[1]:
                    self.positions[dimension] = self.function_range[1]
