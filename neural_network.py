from math import exp

class HiddenNeuron:
    @staticmethod
    def getOutput( w1, w0, x):
        net = x*w1 + w0
        return 1/(1 + exp(-net))
    
class OutputNeuron:
    @staticmethod
    def getOutput( weights, xVect):
        xVect += [1]
        if len(xVect)!=len(weights): raise BaseException("In OutputNeuron.getOutput(): len(weights) != len(xVect)")
        net = 0.0
        for i in range( len(weights)):
            net += weights[i]* xVect[i]
        return net