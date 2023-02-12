import random
import pandas as pd
from utils import Utils
from weather import Weather
from flood import Flood
from earthQuake import EarthQuake
from population import Population
from flood import Flood
import math
import numpy as np 

class Scenario:
    def __init__(self, pop , weather, numScenarios, t, typ):
        
        self.timeIstant = t
        self.disasterType = typ
        self.T = pop.T
        self.ns = numScenarios
        self.weather = weather
        self.pop = pop
        self.dailyRain, self.t_min, self.t_max, self.radiaz = weather.weatherData
        # self.probability = 0
        self.rainAmount = []
        self.population = []
        self.earthqwake = []
        


    def sampleScenario(self):
        Ia, S, Qmax = 10, 5, 200

        self.tempMin = self.t_min[self.timeIstant]
        self.tempMax = self.t_max[self.timeIstant]
        self.radiation = self.radiaz[self.timeIstant]
          
        if self.disasterType == 1:
            self.eq = EarthQuake(3, 0.8)

            self.earthqwake = self.eq.sampleEQ(5)
            self.flooding = (0, 0)
            disProb = self.earthqwake[1]

        elif self.disasterType == 2:
            period = math.ceil(self.timeIstant/365)
            self.flood = Flood(period, Ia, S, Qmax)   # number of years
            
            self.flooding = self.flood.getProb()
            self.earthqwake = (0, 0)
            disProb = self.flooding[1]

        self.rainAmount, rainProb = self.dailyRain[self.timeIstant], self.weather.getRainProbability(self.timeIstant,self.dailyRain[self.timeIstant] )
        self.population, popProb = self.pop.samplePopulation(self.timeIstant)  

        rainProb = self.weather.getRainProbability(self.timeIstant, self.rainAmount)
        tminProb, tmaxProb = self.weather.getTProbability(self.timeIstant, self.tempMin, self.tempMax)
        self.probability = rainProb * popProb * disProb * tminProb * tmaxProb 
        # print("Probabilities: ", rainProb, popProb, disProb, tminProb, tmaxProb)
        

        return self


  