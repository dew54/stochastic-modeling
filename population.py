import numpy as np
from utils import Utils
class Population:
    def __init__(self, totalPop, T):
        self.wave = []
        for x in range(T):
            gauss = np.random.normal(0,1,1)[0]
            self.wave.append(totalPop*((3 + ((1/3)*np.cos(0.0172*x) + np.cos(0.0172*x*2 - 0.6) ))) + 550*gauss)
    
    def samplePopulation(self, t):
        return(self.wave[t])

    def getPopWave(self):
        return self.smooth(self.wave, 7)

    def smooth(self, y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode="same")
        return y_smooth
    
    def getProbability(self, tresh):
        for t in range(self.T):
            count = self.wave if self.wave <= tresh else 0
        