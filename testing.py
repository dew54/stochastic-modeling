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



# df = pd.DataFrame(columns=['idx', 'day', 'population' 'rainAmount', 't_min', 't_max', 'radiation', 'flood', 'earthqwake'])

# df['population'] = [1,2]

vector = (1, 5, 10)
print(Utils.normalizeProbs(vector))