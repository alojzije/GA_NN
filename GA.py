from Population import Population
from fitness import Fitness
from selection import chooseParents
from crossover import crossover
from mutation import Mutation
from setParser import parseLearningSet


VEL_POP = 100
MAX_ITER = 1000
N =10
K = 10
train_set = parseLearningSet("learningSet/train-set.txt")
fitnessOp = Fitness(train_set)
mutationOp = Mutation(K, N, VEL_POP)

P = Population(N, VEL_POP)
fitnessOp.evaluate(P)
while (MAX_ITER ):
    MAX_ITER -=1;
    new_P = Population(P.n,0)
    new_P.addIndividual(fitnessOp.bestIndividual)
    while new_P.populationSize <VEL_POP:
        parent1, parent2 = chooseParents(P, fitnessOp)
        child = crossover(parent1, parent2)
        mutationOp.mutate(child)
        new_P.addIndividual(child)
    P = new_P
    fitnessOp.evaluate(P)
    print "%d. gen Err: %s" %(1000-MAX_ITER, fitnessOp.minError)
        
        
