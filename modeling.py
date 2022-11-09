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

    T = 365*10
    totPop = 1000
    weather = Weather(T)
    dailyRain, t_min, t_max, radiaz, probs = weather.weatherGame()
    population = Population(totPop, T)
    population.getProbability(5000)

    scenario = Scenario(totPop, T)
    scenario.sampleScenario()

    # ics, tmin, tmax = weather.getTemperatureProbability(300, 10, 20)

    X = range(0, T)


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

    # axs1[2][0].plot(ics, tmin, tmax)
    # axs1[2][0]

    plt.show()