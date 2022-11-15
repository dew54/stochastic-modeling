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



def runSym():
    numScenarios = 20
    T = 365 *10
    totPop = 1000
    weather = Weather(T)
    weatherData = weather.weatherGame()
    dailyRain, t_min, t_max, radiaz = weatherData
    population = Population(totPop, T)
    scenarios = []
    tIstants = []
    for ns in range(numScenarios):
        scenario = Scenario(population, weatherData, numScenarios)
        s = scenario.sampleScenario()
        scenarios.append(s)
        tIstants.append(s.timeIstant)
    

    X = range(0, T)
    df = pd.DataFrame(columns=['day', 'population', 'rainAmount', 't_min', 't_max', 'radiation', 'flood', 'earthqwake', 'probability', 'normalized'])
    
    df['day'] = tIstants
    df['population'] = [int(s.population) for s in scenarios]
    df['rainAmount'] = [int(s.rainAmount) for s in scenarios]
    df['t_min'] = [int(s.tempMin) for s in scenarios]
    df['t_max'] = [int(s.tempMax) for s in scenarios]
    df['radiation'] = [int(s.radiation) for s in scenarios]
    df['flood'] = [s.flooding[0] for s in scenarios]
    df['earthqwake'] =  [s.earthqwake[0] for s in scenarios]
    df['probability'] = [s.probability for s in scenarios]
    df['normalized'] = Utils.normalizeProbs([s.probability for s in scenarios])

    fig1, axs1 = plt.subplots(3, 2)

    axs1[0][0].plot(X, dailyRain[0:T] )
    axs1[0][0].set_title('Rainy days')

    axs1[1][0].plot(X, t_min, t_max)
    axs1[1][0].set_title('t min')

    axs1[0][1].plot(X,  population.getPopWave() )
    axs1[0][1].set_title('pop')

    axs1[1][1].plot(X,  radiaz )
    axs1[1][1].set_title('radiation')

    axs1[2][0].plot([x for x in range(len(tIstants))], Utils.normalizeProbs([s.probability for s in scenarios]))
    axs1[2][0]

    plt.show()
    return df


if __name__ == "__main__":
    runSym()
