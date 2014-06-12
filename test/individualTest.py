'''
Created on Jun 12, 2014

@author: madame
'''
import unittest
from Individual import Individual


class Test(unittest.TestCase):


    def setUp(self):
        self.iDefault = Individual();
        self.i10 = Individual(10);
        pass


    def tearDown(self):
        pass


    def testInit(self):
        self.assertEqual(self.iDefault.getNumberOfWeights(), 3*5+1, "iDefault.getNumberOfWeights() should be %d but is %d" % (3*5+1, self.iDefault.getNumberOfWeights()))
        self.assertEqual(self.i10.getNumberOfWeights(), 3*10+1, "i10.getNumberOfWeights() should be %d but is %d" % (3*10+1, self.i10.getNumberOfWeights()))
        self.assertEqual(self.iDefault.getNumberOfWeights(), len(self.iDefault.weights), "len(iDefault.weights) should be %d but is %d" % (self.iDefault.getNumberOfWeights(), len(self.iDefault.weights)))
        self.assertEqual(self.i10.getNumberOfWeights(), len(self.i10.weights), "len(i10.weights) should be %d but is %d" % (self.i10.getNumberOfWeights(), len(self.i10.weights)))
        self.assertEqual(self.i10.fitness, 0.0, "i10.fitness should be %f but is %f" % (0.0, self.i10.fitness))
        self.i10.setFitness(4.5)
        self.assertEqual(self.i10.fitness, 4.5, "i10.fitness should be %f but is %f" % (4.5, self.i10.fitness))
        self.i10.setWeight(0, 22)
        self.assertEqual(self.i10.getWeight(0), 22, "i10.weight[%d] should be %f but is %f" % (0, 22, self.i10.getWeight(0)))

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()