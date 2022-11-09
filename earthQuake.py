from utils import Utils

class EarthQuake:
    def __init__(self, a, b):
        p = []
        for m in range(0, 14):
            
            N = 10 **((a-b*(m)))
            p.append(N)

        self.probVector = ([ i/sum(yps for yps in p) for i in p])

    def getProb(self, magnitude):
        if magnitude >= 14:
            return 0
        else:
            return(self.probVector[magnitude])


    def sampleEQ(self, minMag):
        magnitude = 0
        while magnitude < minMag:
            magnitude = Utils.discrete_inverse_trans(self.probVector)
        
        prob = self.getProb(magnitude)
        return magnitude, prob
        
