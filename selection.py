from random import random

def chooseParents(population, fitnessOp):
    fit_sum = float(fitnessOp.fitness_sum)
    ind_fitness = [ind.fitness/fit_sum for ind in population.individuals]
    probabilities = [sum(ind_fitness[:i+1]) for i in range(len(ind_fitness))]
    parent1 = getParent(population, probabilities)
    parent2 = getParent(population, probabilities)
    
    return parent1, parent2
    
def getParent(population, probabilities):
    p = random()
    for i in range(population.populationSize):
        if p <= probabilities[i]:
            return population.getIndividual(i)
    return population.getIndividual(population.populationSize-1)