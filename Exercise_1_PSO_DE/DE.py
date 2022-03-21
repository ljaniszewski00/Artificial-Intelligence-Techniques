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
        return self.global_best, self.global_bests, counter

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
