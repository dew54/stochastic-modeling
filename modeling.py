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



if __name__ == "__main__":

    numScenarios = 20
    T = 365 * 10
    totPop = 1000
    weather = Weather(T)
    dailyRain, t_min, t_max, radiaz, probs = weather.weatherGame()
    population = Population(totPop, T)
    population.getProbability(5000)

    scenario = Scenario(totPop, T)
    scenarios = []
    tIstants = []
    badDays = []
    for ns in range(numScenarios):
        s = scenario.sampleScenario()
        scenarios.append(s)
        tIstants.append(s.timeIstant)
        print(s.timeIstant)
    print(tIstants)

    # # ics, tmin, tmax = weather.getTemperatureProbability(300, 10, 20)
    # tIstants = [0, 1, 2]
    X = range(0, T)
    # for x in X:
    #     for t in tIstants:
    #         if t == x:
    #             badDays.append(1)
    #         else:
    #             badDays.append(0)
                
    badDays = np.isin(X, tIstants)
    # print(badDays)



    df = pd.DataFrame(columns=['idx', 'day', 'population' 'rainAmount', 't_min', 't_max', 'radiation', 'flood', 'earthqwake'])
    
    df['idx'] = [x for x in range(len(tIstants))]
    df['day'] = tIstants
    for s in scenarios:
        



    df['population'].append(s.population)
    df['rainAmount'].append(s.rainAmount)
        # df['t_min'] = self.tem



    fig1, axs1 = plt.subplots(3, 2)

    axs1[0][0].plot(X, dailyRain[0:T] )
    axs1[0][0].set_title('Rainy days')

    #plt.grid()

    axs1[1][0].plot(X, t_min, t_max)
    axs1[1][0].set_title('t min')

    axs1[0][1].plot(X,  population.getPopWave() )
    axs1[0][1].set_title('pop')

    axs1[1][1].plot(X,  radiaz )
    axs1[1][1].set_title('radiation')

    axs1[2][0].plot(X, badDays)
    axs1[2][0]

    plt.show()