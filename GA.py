from Population import Population
from fitness import Fitness
from selection import chooseParents
from crossover import crossover
from mutation import Mutation
from setParser import parseLearningSet

VEL_POP = 100;
MAX_ITER = 100;
N = 10;
K = 0.2
fitnessOp = Fitness(parseLearningSet("learningSet/train-set.txt"))
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
        
        
