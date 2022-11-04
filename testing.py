import pandas as pd
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF


def sampleGivenCDF(y):
    u = np.random.uniform()
    print(u)
    if u < y[1]:
        return 1
    else :    
        for idx in range(y.size):
            if(y[idx] < u and y [idx+1] > u):
                return idx



T = 365
EQ_samples = []

a = -0.9999999
b = 1
y = []
for m in range(0, 1300):
    print(m)
    print(10 **((a-b)*(m/100)))
    y.append(10 **((a-b)*(m/100)))
EQ_cdf = ECDF(y)

for i in range(0, T):
    EQ_samples.append(sampleGivenCDF(EQ_cdf.y)/100)


# print(EQ_samples)