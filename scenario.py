import random
import pandas as pd
from utils import Utils
from weather import Weather
from flood import Flood
from earthQuake import EarthQuake
from population import Population
from flood import Flood
import math

class Scenario:
    def __init__(self, totPop,  T ):
        self.timeIstant = 0
        self.weather = Weather(T)
        self.pop = Population(totPop, T)
        self.eq = EarthQuake(3, 0.8)
        self.flood = Flood(T/365)   # number of years
        self.dailyRain, self.t_min, self.t_max, self.radiaz, self.probs = self.weather.weatherGame()
        # self.probability = 0
        self.rainAmount = []
        self.population = []
        self.earthqwake = []
        # self.t_min = []
        # self.t_max = []
        # self.radiaz = []
        self.T = T
        





    def sampleScenario(self):

        self.disaster = {
            1: "earthqwake",
            2: "flood"
        }

        disasterType = random.randint(1, 2)
        self.timeIstant = random.randint(0, self.T)
        # print(self.t_min)
        self.tempMin = self.t_min[self.timeIstant]
        self.tempMax = self.t_max[self.timeIstant]
        self.radiation = self.radiaz[self.timeIstant]
        
        self.rainAmount = [self.weather.sampleRain(self.timeIstant)]
        self.population = [self.pop.samplePopulation(self.timeIstant)]        
        if disasterType == 1:
            self.earthqwake = [self.eq.sampleEQ(5)]
            self.flooding = [0, 0]
        elif disasterType == 2:
            self.flooding = [self.flood.getProb()]
            self.earthqwake = [0, 0]
        

        

        # print(self.timeIstant)
        # print(self.rainAmount)
        # print(self.population)
        # print(self.earthqwake)
        # print(self.floodings)

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