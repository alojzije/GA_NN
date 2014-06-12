from Individual import Individual
from copy import deepcopy


class Population:
    def __init__(self, n=5, populationSize=100):
        self.n = n if (n > 0) else 5;
        self.populationSize = populationSize
        self.individuals = [Individual(n) for i in range(populationSize)]

    def addIndividual(self,individual):
        self.individuals.append(individual)
        self.populationSize += 1
    
    def getIndividual(self, index):
        if index >= len(self.individuals): raise "In Population.getIndividual(): index %d out of range" %index
        return self.individuals[index]
     
    def getIndividualCopy(self, index):
        if index >= len(self.individuals): raise "In Population.getIndividualCopy(): index %d out of range" %index
        return deepcopy(self.individuals[index])