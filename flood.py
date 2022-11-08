from utils import Utils


class Flood:
    def __init__(self, n, period, y100 = 1):
        self.probVector = []
        for n in range(15):
            self.probVector.append(1 - (1-(1/period))**n)

    def getProb(self):
        return self.probVector
        
    def sampleFlood(self):
        Utils.discrete_inverse_trans(self.probVector)
