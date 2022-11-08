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

    