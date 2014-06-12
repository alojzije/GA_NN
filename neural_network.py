from math import exp


class HiddenNeuron(object):
    @staticmethod
    def getOutput(w1, w0, x):
        net = x*w1 + w0
        return 1/(1 + exp(-net))


class OutputNeuron(object):
    @staticmethod
    def getOutput(weights, xVector):
        net = 0.0
        xVector += [1]
        if len(xVector) != len(weights): raise BaseException("In OutputNeuron.getOutput(): len(weights) != len(xVector)")

        for i in range(len(weights)):
            net += weights[i] * xVector[i]
        return net


def calcError(neural_network, learning_set):
    Error = 0
    n = neural_network.n

    hidden_weights = [(neural_network.getWeight(i), neural_network.getWeight(i+1)) for i in range(0, 2*n, 2)]
    output_weights = neural_network.weights[2*n:]

    for x, t in learning_set:
        hidden_output = []
        for w1, w0 in hidden_weights:
            hidden_output.append(HiddenNeuron.getOutput(w1, w0, x))
        o = OutputNeuron.getOutput(output_weights, hidden_output)
        Error += 0.5*((t-o)**2)

    ##avg error
    Error = Error/float(len(learning_set))
    return Error