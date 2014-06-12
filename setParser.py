import re

def parseLearningSet(fileName):
    f = open(fileName)
    training_set = []
    for line in f.readlines():
        x, y = line.rsplit()
        if re.match(".*[0-9]{1}.*", x) and re.match(".*[0-9]{1}.*", y): 
            training_set.append((float(x), float(y))
    return training_set