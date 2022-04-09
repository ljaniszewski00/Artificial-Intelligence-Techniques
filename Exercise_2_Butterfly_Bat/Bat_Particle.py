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

        self.minimum_frequency = 0.0
        self.maximum_frequency = 2.0
        self.frequency = 0
        self.update_frequency()

        self.adaptation = calculate_function_value(self.function_number, self)

        self.pulse_rate = random.uniform(0, 1)
        self.initial_pulse_rate = self.pulse_rate
        self.loudness = random.uniform(1, 2)
        self.initial_loudness = self.loudness

    def update_adaptation(self):
        self.adaptation = calculate_function_value(self.function_number, self)

    def update_frequency(self):
        self.frequency = self.minimum_frequency + (self.maximum_frequency - self.minimum_frequency) * \
                         random.uniform(0, 1)

    def update_velocities(self, best_bat_positions):
        for dimension in range(self.dimensions):
            self.velocities[dimension] = self.velocities[dimension] + \
                           (best_bat_positions[dimension] - self.positions[dimension]) * self.frequency

    def update_positions(self, second_time=False, avg_loudness=None):
        if not second_time:
            for dimension in range(self.dimensions):
                self.positions[dimension] += self.velocities[dimension]

                if self.positions[dimension] < self.function_range[0]:
                    self.positions[dimension] = self.function_range[0]
                elif self.positions[dimension] > self.function_range[1]:
                    self.positions[dimension] = self.function_range[1]
        else:
            rand = random.uniform(0, 1)
            if rand < self.pulse_rate:
                epsilon = random.uniform(-1, 1)
                for dimension in range(self.dimensions):
                    if avg_loudness is not None:
                        self.positions[dimension] += epsilon * avg_loudness
                    else:
                        self.positions[dimension] += epsilon * self.loudness

                    if self.positions[dimension] < self.function_range[0]:
                        self.positions[dimension] = self.function_range[0]
                    elif self.positions[dimension] > self.function_range[1]:
                        self.positions[dimension] = self.function_range[1]

    def update_pulse_rate_and_loudness(self, gamma, alpha, iteration_number):
        self.pulse_rate = self.initial_pulse_rate * (1 - np.exp(-gamma * iteration_number))
        self.loudness = alpha * self.initial_loudness
