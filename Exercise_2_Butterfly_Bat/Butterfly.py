"""
The scheme of Butterfly algorithm
1. Generate initial population of butterflies:
    1.1. Assign random starting position from given range for each dimension
2. Calculate Fitness values / intensity values for each butterfly
3. Define:
    3.1. sensor modality c -
    3.2. power exponent a -
    3.3. switch probability p -
4. Calculate function value from every butterfly positions and determine the best solution
value holds the best solution
5. Until end condition has not been fulfilled (max iteration number or given accuracy):
    5.1. For each butterfly in the population calculate fragrance f with equation:
        f = c(I**a),
        where:
            c - the sensor modality
            I - the stimulus intensity
            a - the power exponent dependent on modality
    5.2. For each butterfly in the population:
        5.2.1. Generate a random number r from 0 to 1
        5.2.2. If r < p,
                then move towards best butterfly / solution with the equation:
                    x = x + (r**2 * gbest - x) * f,
                    where:
                        x - current position
                        r - random value from 0 to 1
                        gbest - currenst best solution's position
                        f - fragrance
                If not,
                then move butterfly randomly with the equation:
                    x = x + (r**2 * xj - xk) * f,
                    where:
                        x - current position
                        r - random value from 0 to 1
                        xj, xk - current positions of two random butterflies from the solution space
                        f - fragrance
        5.2.3. Calculate function value from butterfly positions and determine if it's better than the best solution.
        If yes, save it as the best solution
        5.2.4. Update the value of a

"""
import copy
import sys