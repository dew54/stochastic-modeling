from utils import Utils
import random
import numpy as np
from weather import Weather
class Flood:
    def __init__(self, period, Ia, S, Qmax):
        self.Ia = Ia
        self.S = S
        self.Qmax = Qmax

        
        self.probVector = []
        self.prob =  1 - (1 - (self.computeOHY()))**period

        

    def getProb(self):
        return 1, self.prob
        
    def sampleFlood(self):
        Utils.discrete_inverse_trans(self.probVector)

    def sampleNumFloods(self):
        numOfFloods = random.sample(range(1, 9), k=1)
        return numOfFloods[0], self.probVector[numOfFloods[0]]

    def getRainOff(self):
        period = 100
        weather = Weather(period)
        dailyRain, t_min, t_max, radiaz = weather.weatherGame()
        return [(((p - self.Ia)**2)/(p - self.Ia + self.S))for p in dailyRain]

    def computeOHY(self):
        Q = self.getRainOff()
        print(Q)
        count = sum(q >= self.Qmax for q in Q)
        return count/len(Q)



    

    
