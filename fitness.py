# train set = [(x, f(x)), (x, f(x)), ...]
class Fitness:
    def __init__(self, train_set):
        self.fitness_sum = 0.0
        self.bestIndividual = None
        self.train_set = train_set;
        
    def evaluate(self, population):
        pass