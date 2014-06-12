from neural_network import calcError
# train set = [(x, f(x)), (x, f(x)), ...]
class Fitness:
    def __init__(self, train_set):
        self.fitness_sum = 0.0
        self.bestIndividual = None
        self.train_set = train_set
        self.minError = None
        
    def evaluate(self, population):
        self.minError = None
        self.fitness_sum = 0.0
        self.bestIndividual = None
        for i in range(population.populationSize):
            self.evaluateIndividual(population.getIndividual(i))

    def evaluateIndividual(self, individual):
        Error = calcError(individual, self.train_set)
        if self.minError is None or Error < self.minError:
            self.minError = Error
            self.bestIndividual = individual
        
        ## calculate fitness
        fitness = 1/Error if Error>0  else 0
        self.fitness_sum += fitness
        individual.setFitness(fitness)



