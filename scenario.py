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
            self.flood = Flood(period)   # number of years
            
            self.flooding = self.flood.getProb()
            self.earthqwake = (0, 0)
            disProb = self.flooding[1]

        self.rainAmount, rainProb = self.dailyRain[self.timeIstant], self.weather.getRainProbability(self.timeIstant,self.dailyRain[self.timeIstant] )
        self.population, popProb = self.pop.samplePopulation(self.timeIstant)  

        rainProb = self.weather.getRainProbability(self.timeIstant, self.rainAmount)
        tminProb, tmaxProb = self.weather.getTProbability(self.timeIstant, self.tempMin)
        self.probability = rainProb * popProb * disProb * tminProb * tmaxProb
        # print("Probabilities: ", rainProb, popProb, disProb, tminProb, tmaxProb)
        

        return self



    # def getRow(self):
    #     row = [self.timeIstant, self.population, self.rainAmount, self.]



    def populate(self, numScenarios, evaAreas, evaDemand):
        self.night = int(1/(random.randint(1,5)))
        self.windLevel = random.randint(0, 4)
        self.rainLevel = random.randint(0, 4)
        self.lightLevel = random.randint(0, 4)
        self.severity = math.ceil((self.windLevel + self.rainLevel + self.lightLevel)/3) 
        distribution = {
            0 : 0.25,
            1 : 0.35,
            2 : 0.25,
            3 : 0.1,
            4 : 0.05
        }

        self.speedCoeff = 1/(1+Utils.computeCoefficient(self, "drive"))**self.severity
        
        self.loadingCoeff = 1 + (1- 1/(1+Utils.computeCoefficient(self, "loadingOps"))**self.severity)
          
        self.probability = distribution[self.severity]
        self.evaAreas = evaAreas
        
        for area in evaAreas:
            area.evaDemand = random.randint(evaDemand[0], evaDemand[1])