import random
import copy
import numpy as np
from Utils.utils import calculate_function_value


class BatParticle:
    def __init__(self, function_number, function_range, dimensions):
        self.function_number = function_number
        self.function_range = function_range
        self.dimensions = dimensions
        self.positions = [random.uniform(function_range[0], function_range[1]) for e in range(dimensions)]
        self.velocities = [random.uniform(function_range[0], function_range[1]) for e in range(dimensions)]

        self.pulse_rate = 0
        self.loudness = 0
        self.rand = random.uniform(0, 1)
        self.frequency = 0

        self.adaptation = calculate_function_value(self.function_number, self)
        self.best_adaptation = self.adaptation
        self.best_adaptation_positions = copy.copy(self.positions)

    def update_adaptation(self):
        self.adaptation = calculate_function_value(self.function_number, self)
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_adaptation_positions = copy.copy(self.positions)

    def update_frequency(self):
        self.frequency = 0 + (1 - 0) * random.uniform(0, 1)

    def update_velocities(self, best_bat_positions):
        for dimension in range(self.dimensions):
            new_velocity = self.velocities[dimension] + \
                           (self.positions[dimension] - best_bat_positions[dimension]) * self.frequency

            self.velocities[dimension] = new_velocity

    def update_positions(self, mean_loudness_value_of_all_bats):
        for dimension in range(self.dimensions):
            self.positions[dimension] += self.velocities[dimension]
            if random.random() < self.loudness:
                self.positions[dimension] += mean_loudness_value_of_all_bats * random.uniform(-1, 1)

            if self.positions[dimension] < self.function_range[0]:
                self.positions[dimension] = self.function_range[0]
            elif self.positions[dimension] > self.function_range[1]:
                self.positions[dimension] = self.function_range[1]

    def update_pulse_rate_and_loudness(self, pulse_rate_decay, loudness_decay, loudness_limit, gamma, iteration_number):
        self.pulse_rate = pulse_rate_decay * (1 - np.exp(-gamma * iteration_number))
        if self.loudness > loudness_limit:
            self.loudness *= loudness_decay
        else:
            self.loudness = loudness_limit




