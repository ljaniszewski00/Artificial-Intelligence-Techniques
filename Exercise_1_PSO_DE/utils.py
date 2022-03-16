def calculate_function_value(function_number, particle):
    value = 0
    if function_number == 1:
        # Sphere
        for iteration_number in range(1, particle.dimensions + 1):
            value += pow(particle.positions[iteration_number-1], 2)
        return value
    elif function_number == 2:
        # Schwefel
        for iteration_number in range(1, particle.dimensions + 1):
            value += pow(abs(particle.positions[iteration_number-1]), 2)
        temp_value = 1
        for iteration_number in range(1, particle.dimensions + 1):
            temp_value *= abs(particle.positions[iteration_number-1])
        value += temp_value
        return value
    elif function_number == 3:
        # Rosenbrock
        for iteration_number in range(1, particle.dimensions):
            value += 100 * (pow(particle.positions[iteration_number] -
                            pow(particle.positions[iteration_number-1], 2), 2) +
                            pow(particle.positions[iteration_number-1] - 1, 2))
        return value
