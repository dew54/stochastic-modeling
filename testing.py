import numpy as np
import random as rm
import math
import pandas as pd
from scipy.stats import uniform
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from getStats import getStats
from earthQuake import EarthQuake
from flood import Flood
from population import Population
from weather import Weather
from scenario import Scenario
from utils import Utils
import random

numScenarios = 25
T = 365 *5
basePop = 1000
weather = Weather(T)