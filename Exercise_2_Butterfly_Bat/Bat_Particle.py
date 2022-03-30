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
        self.velocities = [0 for e in range(dimensions)]

        self.frequency = 0
        self.pulse_rate = 0.5
        self.loudness = 0.5

        self.adaptation = calculate_function_value(self.function_number, self)
        self.local_best = self.adaptation

    def update_adaptation(self):
        self.adaptation = calculate_function_value(self.function_number, self)

    def update_frequency(self, minimum_frequency, maximum_frequency):
        self.frequency = minimum_frequency + (maximum_frequency - minimum_frequency) * random.uniform(0, 1)

    def update_velocities(self, best_bat_positions):
        for dimension in range(self.dimensions):
            new_velocity = self.velocities[dimension] + \
                           (self.positions[dimension] - best_bat_positions[dimension]) * self.frequency

            if new_velocity < self.function_range[0]:
                self.velocities[dimension] = self.function_range[0]
            elif new_velocity > self.function_range[1]:
                self.velocities[dimension] = self.function_range[1]
            else:
                self.velocities[dimension] = new_velocity

    def update_positions(self):
        temp_position = [0 for e in range(self.dimensions)]

        for dimension in range(self.dimensions):
            temp_position[dimension] += self.velocities[dimension]

        for dimension in range(self.dimensions):
            if np.random.random_sample() > self.pulse_rate:
                temp_position[dimension] = self.local_best + 0.001 * random.gauss(0, 1)

        for dimension in range(self.dimensions):
            if temp_position[dimension] < self.function_range[0]:
                temp_position[dimension] = self.function_range[0]
            elif temp_position[dimension] > self.function_range[1]:
                temp_position[dimension] = self.function_range[1]

        adaptation = calculate_function_value(self.function_number, self)
        rnd = np.random.random_sample()

        for dimension in range(self.dimensions):
            if adaptation < self.adaptation and rnd < self.loudness:
                self.positions[dimension] = temp_position[dimension]

        self.update_local_best(adaptation)

    def update_local_best(self, adaptation):
        if adaptation < self.local_best:
            self.local_best = adaptation

    def update_pulse_rate_and_loudness(self, pulse_rate_decay, loudness_decay, loudness_limit, gamma, iteration_number):
        self.pulse_rate = pulse_rate_decay * (1 - np.exp(-gamma * iteration_number))
        if self.loudness > loudness_limit:
            self.loudness *= loudness_decay
        else:
            self.loudness = loudness_limit




