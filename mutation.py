import random

class Mutation:
    def __init__(self, K, n, populationSize ):
        self.K = K
        self.percentage = n/float(populationSize)
    
    def mutate(self, individual):
        for i in range(individual.getNumberOfWeights()): 
            if random.random() <= self.percentage:
                weight = individual.getWeight(i)
                weight += random.uniform(0, self.K)
                individual.setWeight(i, weight)
                
               
                