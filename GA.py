import argparse
from Population import Population
from fitness import Fitness
from selection import chooseParents
from crossover import crossover
from mutation import Mutation
from parsers import parseLearningSet, parseLearningDict
from neural_network import HiddenNeuron, OutputNeuron, calcError, get_nn_output



def run_GA(P, fitnessOp, mutationOp,VEL_POP, MAX_ITER, ERR_THRESHOLD):
    fitnessOp.evaluate(P)
    gen = 0
    while gen < MAX_ITER and fitnessOp.minError > ERR_THRESHOLD:
        gen += 1
        new_P = Population(P.n,0)
        new_P.addIndividual(fitnessOp.bestIndividual)
        while new_P.populationSize <VEL_POP:
            parent1, parent2 = chooseParents(P, fitnessOp)
            child = crossover(parent1, parent2)
            mutationOp.mutate(child)
            new_P.addIndividual(child)
        P = new_P
        fitnessOp.evaluate(P)
        print "%5d. gen,\t error: %s" %(gen, fitnessOp.minError)
    return fitnessOp.bestIndividual


def writeOut(neural_network, test_set=[], test_dict={}):
    while True:
        print '_'*40
        x = raw_input("Unesite 'u' za ucitavanje seta za testiranje, 'k' za kraj\nInace unesite broj: ")
        if x.startswith('k'):
            break
        if x.startswith('u'):
            testPath = raw_input("Unesite put do datoteke: ")
            try:
                test_set = parseLearningSet(testPath)
                test_dict = parseLearningDict(testPath)
                print "Ukupna greska na ucitanim testnim primjerima je ", calcError(neural_network, test_set)
                continue
            except Exception:
                print "Ucitavanje nije uspjelo\n"
                continue
        else:
            try:
                x = float(x)
            except ValueError:
                print "Nije broj, probajte ponovo\n"
                continue


        nn_out = get_nn_output(x, neural_network)
        print "Neuronska  mreza  f(x) = ", nn_out
        if x in test_dict.keys():
            print "Prava vrijednost  f(x) = ", test_dict.get(x)


def main():
    parser = argparse.ArgumentParser(description='Tweak GA parameters')
    parser.add_argument('-s','--populationSize',    type=int, required=False, default=100,
                        help = 'Desired population size (int)')
    parser.add_argument('-i','--maxIter',           type=int, required=False, default=100,
                        help = "Max number of iterations allowed (int)")
    parser.add_argument('-n','--n',                 type=int, required=False, default=10,
                        help = 'Desired number of neural_networks in the hidden layer')
    parser.add_argument('-k','--K',                 type=float, required=False, default=1.1,
                        help = "Chromosome is mutated by adding a number from the normal_distibution(0,K) to it's weights value")
    parser.add_argument('-err','--errThreshold',    type=float, required=False, default=0.1,
                        help = "Algorithm stops search if it has found a chromosome with error less than errThreshold")
    parser.add_argument('-train','--trainSet',      type=str, required=False, default="learningSet/train-set.txt",
                        help = "Path to training_set")
    #parser.add_argument('-test','--testSet',        type=str, required=False, default="learningSet/test-set.txt",
    #                    help = "Path to test_set")

    args = parser.parse_args()
    ERR_THRESHOLD = args.errThreshold
    VEL_POP  = args.populationSize
    MAX_ITER = args.maxIter
    N = args.n
    K = args.K

    train_set = parseLearningSet(args.trainSet)

    ## initialize needed operators
    fitnessOp  = Fitness(train_set)
    mutationOp = Mutation(K, N, VEL_POP)

    ##initialize population
    P = Population(N, VEL_POP)

    ##returns best neural_network (individual)
    best_nn = run_GA(P, fitnessOp, mutationOp, VEL_POP, MAX_ITER, ERR_THRESHOLD)
    test_set  = [] # parseLearningSet(args.testSet)
    test_dict = {} #parseLearningDict(args.testSet)

    writeOut(best_nn, test_set, test_dict)


if __name__ == '__main__':
    main()