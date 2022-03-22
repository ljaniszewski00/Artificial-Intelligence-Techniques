"""
The scheme of Bat algorithm
1. Create particles (bats) on the basis of data given by the user (dimensions number, function range, parameters) and:
    1.1. Assign random starting position from given range for each dimension
    1.2. Assign velocity v = rand(1, function_range)
    1.3. Assign pulse rate r = rand(N, 1) or rand(0, 1)
    1.4. Assign loudness A = rand(N, 1) * 2 or rand(0, 1) * 2
    1.5. Assign frequency f = 2 * rand(0, 1) -> (save this rand for later)
2. For every bat from set:
    2.1. Calculate the current value of function with bat's positions
    2.2. Save current position of the bat as it's best local solution
    2.3. If bat's position is better than the global solution, assign it as global one
3. Until end condition has not been fulfilled (max iteration number or given accuracy):
    3.1. For every bat from set:
        3.1.1. Update frequency using the equation:
            f = Fmin + (Fmax - Fmin) * B
                where:
                    Fmin - function range minimum
                    Fmax - function range maximum
                    B - random number between 0 and 1
        3.1.2. Update velocity using the equation:
            v = v + (x - xbest) * f
                where:
                    v - bat's velocity
                    x - current bat's position
                    xbest - current global best bat's position
                    f - frequency
        3.1.3. Update positions for every bat with the equation:
            x = x + v
                where:
                    x - bat's position
                    v - bat's velocity
    3.2. For every bat from set:
        3.2.1. If r > rand(0, 1) -> same rand as used in 1.1.5.:
            3.2.1.1. Select a solution among the bats as the best solution (bat with the biggest frequency value)
            3.2.1.2. Generate local solution around best solution with equation:
                x = x + ε * A,
                    where:
                        x - current bat's position
                        ε - random number between -1 and 1
                        A - loudness value
        3.2.2. If rand < A and function value < current best function value, save calculated
        function value as current best solution, reduce loudness and increase pulse rate with equations:
            A = α * A,
                where:
                    A - loudness value
                    α - alpha value - random value between 0 and 1
            r = r * (1 - e ** (-yt)),
                where:
                    r - pulse rate
                    γ - gamma value - random value between 0 and 1
                    t - iteration number
        3.2.3. Calculate bat's function value with it's positions
        3.2.4. If bat's new function value is better than global's best solution, assign it as global's best
"""
import copy
import sys