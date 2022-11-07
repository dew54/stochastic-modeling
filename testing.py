import numpy as np
import random as rm
import math
import pandas as pd
from scipy.stats import uniform
from matplotlib import pyplot as plt
from getStats import getStats
from statsmodels.distributions.empirical_distribution import ECDF



def discrete_inverse_trans(prob_vec):
    U=uniform.rvs(size=1)
    if U<=prob_vec[0]:
        return 1
    else:
        for i in range(1,len(prob_vec)+1):
            if sum(prob_vec[0:i])<U and sum(prob_vec[0:i+1])>U:
                return i+1



a = 20
b = 2
y = []


for m in range(0, 13):
    
    y.append(10 **((a-b*(m))))
cdf = ECDF([i/sum(yps for yps in y) for i in y])
for x in cdf.x:
    print(x) 
