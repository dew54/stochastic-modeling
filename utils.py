import numpy as np
from scipy.stats import uniform


class Utils:



    def discrete_inverse_trans(prob_vec):
        U=uniform.rvs(size=1)
        if U<=prob_vec[0]:
            return 0
        else:
            for i in range(1,len(prob_vec)+1):
                if sum(prob_vec[0:i])<U and sum(prob_vec[0:i+1])>U:
                    return i

    def computeAR1(previousVal,A , B):
        epsilon = np.array([np.random.normal(0,1,1)[0], np.random.normal(0,1,1)[0], np.random.normal(0,1,1)[0]] )
        Aprime = A.dot(previousVal)
        Bprime = B.dot(epsilon)
        zed = Aprime + Bprime
        return zed

    def smooth( y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode="same")
        return y_smooth


    def normalizeProbs(probs):
        total = sum(probs)
        normalized = [p/total for p in probs]
        return normalized

    
    def cebychevDis(sample, mean, std):
        lmbda = abs(sample - mean)
        # lmbda = lmbda if lmbda > 1 else 1
        print("lambda is: ", lmbda)

        return  (std**2)/(std**2 + lmbda)       # disuguaglianza di Cantelli
    