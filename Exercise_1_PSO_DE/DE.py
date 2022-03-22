"""
The scheme of DE algorithm
1. Create particles for swarm on the basis of data given by the user (dimensions number, function range, parameters)
2. If end condition has not been fulfilled (max iteration number or given accuracy):
    2.1. Apply reproduction step:
        Create basic vector by making it random or by choosing the best particle from swarm
    2.2. Apply mutation step:
        Modify random vector by difference between two other vectors with F parameter:
            𝑣𝑖 = 𝑥𝑟1 + 𝐹 ∙ (𝑥𝑟2 – 𝑥𝑟3),
            where:
                - 𝑣𝑖 is called the mutant
                - 𝐹 is Mu factor, which is static parameter with values from range (0, 1), typically 0.5
                - 𝑟1, 𝑟2, 𝑟3 are three randomly generated particle's numbers from set of {1, 2, ..., N}
                - indexes of particles meet the condition: 𝑖≠𝑟1≠𝑟2≠𝑟3
    2.3. Apply crossing step:
        Randomly shuffle parent xi and mutant vi elements, which will cause creation of new test particle oi.
        If rand[0, 1) < Cr or j = d, then oij = vij. Else, oij = xij,
        where:
            - rand[0, 1) is random number of given range, selected regardless of each j
            - Cr is crossing coefficient - static parameter fulfilling condition 0 <= Cr <= 1
            - d is random number of vector's element randomly chose from set {1, 2, ..., D}
    2.4. Apply selection step:
        If test particle oi has better adaptation than parent xi, then oi replaces parent in population.
        If test particle oi has worse adaptation than parent xi, then oi is rejected.
"""
import random
import numpy


class DE:
    def __init__(self,
                 particles, #List of vectors for input that are base population
                 functionNumber,  #Number of function to evaluate
                 static_coefficients, #Boolean value to determine if coefficient will have static values
                 max_iterations=None,  # 1st of 2 variants of stopping alg
                 accuracy=None  # 2nd of 2 variants of stopping alg
                 ):
        self.max_iterations = max_iterations
        self.accuracy = accuracy
        self.populations = list()
        self.populations.append(particles)
        self.population_count = len(particles)
        self.current = particles
        if static_coefficients:
            self.Cr = 0.7
            self.F = 0.5
        else:
            self.Cr = random.uniform(0, 0.9)
            self.F = random.uniform(0, 1)
        self.max_iterations = max_iterations
        self.accuracy = accuracy
        self.global_bests = list()
        match functionNumber:
            case 1:
                self.function = self.Sphere
            case 2:
                self.function = self.Schwefel
            case 3:
                self.function = self.Rosenbrock
            case _:
                self.function = self.Sphere
        self.global_best = self.function(self.current[0])

    def doDE(self, best=False):
        counter = 0
        while True:
            appender = list()
            if best:
                iIndex = self.reproduction(best=True)
            for i in range(self.population_count):
                temp = numpy.zeros([len(self.current[0])])
                if not best:
                    iIndex = self.reproduction(best=False)
                xi = self.current[iIndex]
                ui = self.Mutation(iIndex)
                oj = self.Crossing(ui, xi)
                temp = self.Selection(oj, xi, counter)
                appender.append(temp)
            self.populations.append(appender)
            self.current = appender
            counter += 1
            if (self.max_iterations is not None and counter >= self.max_iterations) \
             or (self.accuracy is not None and self.accuracy >= self.global_best): break
        # print(self.global_bests)
        # print(counter)
        return round(self.global_best, 4), self.global_bests, counter

    def reproduction(self, best=False):
        index = 0
        if best:
            for i in range(self.population_count):
                if self.function(self.current[i]) < self.function(self.current[index]):
                    index = i
            return index
        return random.randint(0, self.population_count - 1)

    def Mutation(self, iIndex, best=False):
       while True:
           nums = random.sample(range(0, self.population_count), 2) # get indexes
           if iIndex not in nums:
             break
       ui = self.current[iIndex] + self.F * (self.current[nums[0]] - self.current[nums[1]])
       return ui

    def Crossing(self, ui,xi):
        oj = numpy.zeros([self.current[0].size])
        for i in range(ui.size):
            oj[i] = ui[i] if random.uniform(0, 1) <= self.Cr else xi[i]
        return oj

    def Selection(self, oi, xi, iteration):
        newXi = oi if self.function(oi) < self.function(xi) else xi
        fxi = self.function(newXi)
        if self.global_best >  fxi:
            self.global_best = fxi
            # print(iteration, ":", fxi)
            self.global_bests.append({
                "iteration" : iteration,
                "global_best" : self.global_best
            })
        return newXi

    def Sphere(self, xi):
        sum = 0
        for i in range(xi.size):
            sum += xi[i] * xi[i]
        return sum

    def Schwefel(self, xi):
        sum = 0
        for i in range(xi.size):
            sum += abs(xi[i] * xi[i])
        mult = 1
        for i in range(xi.size):
            mult *= abs(xi[i])
        return sum + mult

    def Rosenbrock(self, xi):
        sum = 0
        for i in range(xi.size - 1):
            sum += 100 * pow((xi[i + 1] - pow(xi[i], 2)), 2) + pow((xi[i] - 1),2)
        return sum

    def getGlobalBests(self):
        return self.global_bests
