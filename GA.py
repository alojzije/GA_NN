from Population import Population
from fitness import Fitness
from selection import chooseParents
from crossover import crossover
from mutation import Mutation
from setParser import parseLearningSet, parseLearningDict
from neural_network import HiddenNeuron, OutputNeuron, calcError


VEL_POP = 100
MAX_ITER = 100
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


test_set = parseLearningSet("learningSet/test-set.txt")
test_dict = parseLearningDict("learningSet/test-set.txt")
print "Avg Error na test-setu je ", calcError(fitnessOp.bestIndividual,test_set )
while(True):
    x = ''
    while x not in test_dict.keys():
        x = raw_input("Unesi broj: ")
        try:
            x = float(x)
        except ValueError:
            "Nije broj, probajte ponovo"


    individual = fitnessOp.bestIndividual
    n = individual.n
    hiddenLayerOutput = []
    for i in range(0,2*n,2):
        w0 = individual.getWeight(i+1)
        w1 = individual.getWeight(i)
        hiddenLayerOutput.append(HiddenNeuron.getOutput(w1, w0, x))

    o = OutputNeuron.getOutput( individual.weights[2*n:], hiddenLayerOutput )
    print "Pokusaj neuronske mreze f(x) = ",o
    print "Prava  vrijednost   f(x) = ",test_dict.get(x)