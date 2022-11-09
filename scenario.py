import random
from utils import Utils
from weather import Weather
from flood import Flood
from earthQuake import EarthQuake
from population import Population
import math

class Scenario:
    def __init__(self, totPop,  T ):
        self.timeIstant = 0
        self.weather = Weather(T)
        self.pop = Population(totPop, T)
        self.eq = EarthQuake(3, 0.8)
        self.dailyRain, self.t_min, self.t_max, self.radiaz, self.probs = self.weather.weatherGame()
        self.probability = 0
        self.rainAmount = []
        self.population = []
        self.earthqwake = []
        self.flood = []
        self.t_min = []
        self.t_max = []
        self.radiaz = []
        self.T = T


    def sampleScenario(self):
        self.timeIstant = random.randint(0, self.T)
        self.rainAmount = [self.weather.sampleRain(self.timeIstant)]
        self.population = [self.pop.samplePopulation(self.timeIstant)]        
        self.earthqwake = [self.eq.sampleEQ(5)]

        print(self.timeIstant)
        print(self.rainAmount)
        print(self.population)
        print(self.earthqwake)

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