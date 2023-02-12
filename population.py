import numpy as np
from utils import Utils
class Population:
    def __init__(self, totalPop, T):
        self.wave = []
        self.totalPop = totalPop
        self.T = 3*T
        # self.stats = self.extractDescriptors()
        for x in range(-3, 0):
            gauss = np.random.normal(0,1,1)[0]
            self.wave.append(totalPop*((3 + ((1/3)*np.cos(0.0172*x) + np.cos(0.0172*x*2 - 0.6) ))) + 550*gauss)     

        for x in range(T):
            gauss = np.random.normal(0,1,1)[0]
            self.wave.append(totalPop*((3 + ((1/3)*np.cos(0.0172*x) + np.cos(0.0172*x*2 - 0.6) ))) + 550*gauss)
        for x in range(self.T, self.T + 3):
            gauss = np.random.normal(0,1,1)[0]
            self.wave.append(totalPop*((3 + ((1/3)*np.cos(0.0172*x) + np.cos(0.0172*x*2 - 0.6) ))) + 550*gauss)
    
    def samplePopulation(self, t):
        wave= self.getPopWave()
        return(wave[t]), self.getProbability(wave[t], t)

    def extractDescriptors(self, t):
        period = 20        
        oneWeek = []
        oneYearDescriptors = []                    
        # for x in range(self.T):
        for p in range(period):
            for x in range(7):
                gauss = np.random.normal(0,1,1)[0]
                oneWeek.append(self.totalPop*((3 + ((1/3)*np.cos(0.0172*(t-x)) + np.cos(0.0172*(t-x)*2 - 0.6) ))) + 550*gauss)
        mean = np.mean(oneWeek)
        std = np.std(oneWeek)
        arr = mean, std
       
        return arr


    def getPopWave(self):
        return self.smooth(self.wave, 7)
        # self.wave[0] = self.totalPop

    def smooth(self, y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode="valid")
        return y_smooth
    
    def getProbability(self, sample, t):
        mean, std = self.extractDescriptors(t)
        
        prb = Utils.cantelliDis(sample, mean, std)

        return prb
    


    def getMax(self):
        return np.max(self.wave)
    
    def getMin(self):
        return np.min(self.wave)