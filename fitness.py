from neural_network import HiddenNeuron, OutputNeuron
# train set = [(x, f(x)), (x, f(x)), ...]
class Fitness:
    def __init__(self, train_set):
        self.fitness_sum = 0.0
        self.bestIndividual = None
        self.train_set = train_set
        self.minError = None
        
    def evaluate(self, population):
        self.fitness_sum = 0.0
        for i in range(population.populationSize):
            self.evaluateIndividual(population.getIndividual(i))

    def evaluateIndividual(self, individual):
        Error = 0;
        n = individual.n
        for x,t in self.train_set:
            hiddenLayerOutput= []
            for i in range(0,2*n,2):
                w0 = individual.getWeight(i+1)
                w1 = individual.getWeight(i)
                hiddenLayerOutput.append(HiddenNeuron.getOutput(w1, w0, x))
            
            o = OutputNeuron.getOutput( individual.weights[2*n:], hiddenLayerOutput )
            Error += 0.5*((t-o)**2)
        
        ##calculate error
        Error = Error/float(len(self.train_set))
        if self.minError is None or Error < self.minError:
            self.minError = Error
            self.bestIndividual = individual
        
        ## calculate fitness
        fitness = 1/Error if Error>0  else 0
        self.fitness_sum += fitness
        individual.setFitness(fitness)
        