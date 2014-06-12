import random
# n-length array of doubles

class Individual:
    def __init__(self, n=5):
        self.n = n if n>0 else 5
        self.fitness = 0.0
        self.weights = [random.uniform(-100, 100) for i in range(3 * self.n + 1)]

    def setFitness(self, fitness):
        self.fitness = fitness

    def setWeight(self, index, val):
        if index >= len(self.weights): raise BaseException("In Individual.setWeight(): index %d out of range" % index)
        self.weights[index] = val

    def getWeight(self, index):
        if index >= len(self.weights): raise BaseException("In Individual.getWeight(): index %d out of range" % index)
        return self.weights[index]

    def getNumberOfWeights(self):
        return len(self.weights)
       
           
    