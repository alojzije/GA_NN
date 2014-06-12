from Individual import Individual


def crossover(parent1, parent2):
    n = parent1.n
    nb_of_weights = parent1.getNumberOfWeights()
    child = Individual(n)
    for i in range(nb_of_weights):
        avg = 0.5*(parent1.getWeight(i) + parent2.getWeight(i))
        child.setWeight(i, avg)
    return child
