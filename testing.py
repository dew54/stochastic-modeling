import numpy as np
import random as rm
import math
import pandas as pd
from scipy.stats import uniform
from matplotlib import pyplot as plt
from getStats import getStats
from statsmodels.distributions.empirical_distribution import ECDF
import random
from utils import Utils
from sympy import symbols, Eq, solve

import json
  

E = 12
Var = 0 
T = 12

pi = E/T
g = Var/(E - E**2)
r1 = (g*T - 1)/(g*T +1)
p01, p11 = symbols('p01 p11')

eq1 = Eq(((p01)/(1 + p01 - p11)), pi)
eq2 = Eq(r1 ,  p11 - p01)

sol = solve((eq1,eq2), (p01, p11))

print(sol[p01])