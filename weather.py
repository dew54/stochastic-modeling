import numpy as np
import math
from getStats import getStats
from utils import Utils
import random
import pandas as pd

class Weather:
    def __init__(self, T):
        self.T = T
        self.p01 = 0.4 # wet day after dry day
        self.p00 = 1 - self.p01 # (dry day following a dry day
        self.p11 = 0.6 # wet day after a wet day  
        p10 = 1 - self.p11  
        self.rainyDays = []
        self.processParams(T)


        self.zed =np.array([0, 0, 0])

        

    def processParams(self, T):

        self.A = np.array([[0.567, 0.086, -0.002], [0.253, 0.504, -0.050], [-0.006, 0.039, 0.244]])
        self.B = np.array([[0.718, 0, 0], [0.328, 0.637, 0], [0.238, -0.314, 0.873]])

        stats, df = getStats()

        E_tmin0 = stats['E_tmin_0']
        E_tmax0 = stats['E_tmax_0']
        E_r0 = stats['E_r_0']

        self.S_tmin0 = stats['VAR_tmin_0']
        self.S_tmax0 = stats['VAR_tmax_0']
        self.S_r0 = stats['VAR_r_0']

        #Override
        # S_r0 = S_r0/10

        E_tmin1 = stats['E_tmin_1']
        E_tmax1 = stats['E_tmax_1']
        E_r1 = stats['E_r_1']

        self.S_tmin1 = stats['VAR_tmin_1']
        self.S_tmax1 = stats['VAR_tmax_1']
        self.S_r1 = stats['VAR_r_1']
        # S_r1 = S_r1/10

        initialValue = np.array([0, 0, 0])

        C_r0 = stats['C_r0']  #-20000
        C_r1 = stats['C_r1'] # -900
        C_tmin0 = stats['C_tmin0'] #-5
        C_tmax0 = stats['C_tmax0'] #-6
        C_tmin1 = stats['C_tmin1'] #-3
        C_tmax1 = stats['C_tmax1'] #-4
        self.wave_tmin0 = []
        self.wave_tmax0 = []
        self.wave_r0 = []
        self.wave_tmin1 = []
        self.wave_tmax1 = []
        self.wave_r1 = []
        self.mu = []


        EQ_prob_vec = []

        eq_cdf = []
        EQ_samples = []
        EQ_p = 0.01
        EQ_mu = 3



        for i in range(T):

            self.wave_tmin0.append(E_tmin0 + C_tmin0 * (np.cos(0.0172*(i - T - 30))))
            self.wave_tmax0.append(E_tmax0 + C_tmax0 * (np.cos(0.0172*(i - T -30))))
            self.wave_r0.append(E_r0 + C_r0 * (np.cos(0.0172*(i - T -30))))

            self.wave_tmin1.append(E_tmin1 + C_tmin1 * (np.cos(0.0172*(i - T -30))))
            self.wave_tmax1.append(E_tmax1 + C_tmax1 * (np.cos(0.0172*(i - T-30))))
            self.wave_r1.append(E_r1 + C_r1 * (np.cos(0.0172*(i - T-30))))
            self.mu.append(80 + 20*np.cos(0.0172*(i - 2*T -30)))

        self.T = T


    def weatherGame(self):
        pc = self.p01
        # 1 - Generate sample from unifrom distribution
        weatherList = ["dry"]
        dailyRain = []
        t_min = []
        t_max =  []
        radiaz =  []
        probs = []
        averageRain = 0
        X = []
        for i in range(0, self.T):
            u = np.random.uniform()
            if u <= pc:
                rainAmount = np.random.exponential(scale=self.mu[i], size=None)
                probability = (1/self.mu[i])* math.exp(rainAmount/self.mu[i])
                pc = self.p11
                weatherList.append("wet: " + str(math.ceil(rainAmount*100)/100))
                
                # while temp_diff >
                tmin, tmax, rad, excursion = self.computeNonPrecip(i, 1)
                dailyRain.append(rainAmount)


            else:
                pc = self.p01
                weatherList.append("dry: " + '0')
                dailyRain.append(0)                                 # Non è un giorno di pioggia -> 0 precipitazioni
                tmin, tmax, rad, excursion = self.computeNonPrecip(i, 0)
                probability = pc

            t_min.append(tmin)
            t_max.append(tmax)
            radiaz.append(rad)
            probs.append(probability)
            i+=1
            X.append(i)

        self.rainyDays = dailyRain
        self.t_min = t_min
        self.t_max = t_max
        self.weatherData =  dailyRain, t_min, t_max, radiaz
        return dailyRain, t_min, t_max, radiaz


    def computeNonPrecip(self, t, isWet):

        excursion = -1
        rad = -1
        # global zed
        
        
        while(excursion<=0 or rad <= 0):           #        Rejection sampling                                     # Settare parametrabile!!!!!
            
            if isWet:
                        
                # zed = zed[-1]
                tmin = self.wave_tmin1[t] + self.S_tmin1 * self.zed[0]
                tmax = self.wave_tmax1[t] + self.S_tmax1 * self.zed[1]
                rad = self.wave_r1[t] + self.S_r1 * self.zed[2]
                
            else:
                tmin = self.wave_tmin0[t] + self.S_tmin0 * self.zed[0]
                tmax = self.wave_tmax0[t] + self.S_tmax0 * self.zed[1]
                rad = self.wave_r0[t] + self.S_r0 * self.zed[2]
                    
            excursion = tmax - tmin
            self.zed = Utils.computeAR1(self.zed, self.A, self.B)
                        
        # if excursion < 0:
        #     print("EXCURSION IS NEGATIVEEEE")

        return tmin, tmax, rad, excursion


    def extractDescriptors(self, t):
        period = 20        
        oneWeek = []
        oneWtmin = []
        oneWtmax = []
        pc = random.sample([self.p11, self.p01], 1)[0]
        for p in range(period):
            for i in range(7):
                u = np.random.uniform()
                if u <= pc:
                    rainAmount = np.random.exponential(scale=self.mu[t-i], size=None)
                    pc = self.p11
                    tmin, tmax, rad, excursion = self.computeNonPrecip(t-i, 1)
                    oneWeek.append(rainAmount)
                    oneWtmin.append(tmin)
                    oneWtmax.append(tmax)

                else:
                    pc = self.p01
                    oneWeek.append(0)                                 # Non è un giorno di pioggia -> 0 precipitazioni
                    tmin, tmax, rad, excursion = self.computeNonPrecip(t-i, 0)
                    oneWtmin.append(tmin)
                    oneWtmax.append(tmax)
                    # oneWeek.append(rainAmount)
        mean = np.mean(oneWeek)
        std = np.std(oneWeek)
        tminMean = np.mean(oneWtmin)
        tminStd = np.std(oneWtmin)
        tmaxMean = np.mean(oneWtmax)
        tmaxStd = np.std(oneWtmax)
        return mean, std, tminMean, tminStd, tmaxMean, tmaxStd

                
    def getRainProbability(self, t, rainAmount):
        mean, std, a, b, c, d = self.extractDescriptors(t)
        prb = Utils.cebychevDis(rainAmount, mean, std)
        return prb
    
    def getTProbability(self, t, tmin):
        a, b, mean, std, Mean, Std = self.extractDescriptors(t)
        prb = Utils.cebychevDis(tmin, mean, std)
        Prb = Utils.cebychevDis(tmin, Mean, Std)
        return prb, Prb
    
    def setMostRainyWeeks(self, rainyDays, ns):
        mostRainy = []
        timeIstant = []
        for t in range(self.T):
            mostRainy.append(sum(rainyDays[t:t+7]))
        mr = pd.Series(mostRainy)
        i = mr.nlargest(ns)
        # mostRainy.sort(reverse = True)

        # print(i)
        self.rainyWeeks =  (i.index.array)


    def sampleFromRainyWeeks(self):
        rainyWeeks = np.array(self.rainyWeeks)
        index = random.sample(range(len(rainyWeeks)), 1)[0]
        sample = rainyWeeks[index]
        a = [1]#list(rainyWeeks[0:index-1])
        b = [2]#list(rainyWeeks[index+1:-1])
        self.rainyWeeks = np.concatenate((a, b))
        # self.rainyWeeks.delete(index)
        # self.rainyWeeks  = a.concatenate(b)
        return sample

    

        
    




        
        

        
    def sampleRain(self, t):
        return self.rainyDays[t], self.getRainProbability(t, self.rainyDays[t])
        