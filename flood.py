from utils import Utils
import random
import numpy as np

class Flood:
    def __init__(self, period):
        self.probVector = []
        
        self.prob =  (sum(np.random.binomial(period, 0.01, 10000) == 1)/10000)

    def getProb(self):
        return 1, self.prob
        
    def sampleFlood(self):
        Utils.discrete_inverse_trans(self.probVector)

    def sampleNumFloods(self):
        numOfFloods = random.sample(range(1, 9), k=1)
        return numOfFloods[0], self.probVector[numOfFloods[0]]

    
