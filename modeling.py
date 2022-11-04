import numpy as np
import random as rm
import math
import pandas as pd
from matplotlib import pyplot as plt
from getStats import getStats
from statsmodels.distributions.empirical_distribution import ECDF


def weatherGame(T):
    
    pc = p01
    # 1 - Generate sample from unifrom distribution
    i = 0
    weatherList = ["dry"]
    totalRain = []
    averageRain = 0
    X = []
    for i in range(1, T):
        u = np.random.uniform()
        if u <= pc:
            rainAmount = np.random.exponential(scale=mu[i], size=None)
            pc = p11
            weatherList.append("wet: " + str(math.ceil(rainAmount*100)/100))
            totalRain.append(rainAmount)
            # while temp_diff >
            computeNonPrecip(i, 1)
        else:
            pc = p01
            weatherList.append("dry: " + '0')
            totalRain.append(0)                                 # Non è un giorno di pioggia -> 0 precipitazioni
            computeNonPrecip(i, 0)

        i+=1
        X.append(i)

    for rain in totalRain:
        averageRain += rain/T
    # print("Possible states: " + str(weatherList))
    # print("average rain: " +  str(averageRain))

def computeAR1(previousVal):
    epsilon = np.array([np.random.normal(0,1,1)[0], np.random.normal(0,1,1)[0], np.random.normal(0,1,1)[0]] )
    Aprime = A.dot(previousVal)
    Bprime = B.dot(epsilon)
    zed = Aprime + Bprime
    return zed





def computeAR():
    zeta = np.array([[0, 0, 0], ]*T)
    for t in range(1, T):
        epsilon = np.array([np.random.normal(0,1,1)[0], np.random.normal(0,1,1)[0], np.random.normal(0,1,1)[0]] )
        Aprime = A.dot(zeta[t-1])
        Bprime = B.dot(epsilon)
        zed = Aprime + Bprime
        zeta = np.append(zeta, [zed], axis=0)
    return zeta


def computeNonPrecip(t, isWet):

    excursion = -1
    rad = -1
    
    initTmin = 0
    initTmax = 10
    initRad = 400

    global zed
    
    while(excursion<=0 or rad <= 0):           #        Rejection sampling                                     # Settare parametrabile!!!!!
    
    
        if isWet:
                    
            # zed = zed[-1]
            tmin = wave_tmin1[t] + S_tmin1 * zed[0]
            tmax = wave_tmax1[t] + S_tmax1 * zed[1]
            rad = wave_r1[t] + S_r1 * zed[2]
            
        else:
            # while(excursion<=0 and rad < stats['min_rad_dry']): 
            # zed = zed[-1]                                                                                 # Settare parametrabile!!!!!
            tmin = wave_tmin0[t] + S_tmin0 * zed[0]
            tmax = wave_tmax0[t] + S_tmax0 * zed[1]
            rad = wave_r0[t] + S_r0 * zed[2]
                
        excursion = tmax - tmin
        zed = computeAR1(zed)                   # 
        

    if excursion < 0:
        print("EXCURSION IS NEGATIVEEEE")
            
            

    t_min.append(tmin)
    t_max.append(tmax)
    r.append(rad)
    temp_diff.append(excursion)
    z.append(zed)
    zed = computeAR1(zed)
    

def earthQwakeGame():
    a = -100
    b = 1


    for m in range(0, 1300):
        print(m)
        print(10 **((a-b)*(m/100)))
        y.append(10 **((a-b)*(m/100)))
    EQ_cdf = ECDF(y)

    # print(EQ_cdf.y)
    print(y)

    for i in range(0, T):
        EQ_samples.append(sampleGivenCDF(EQ_cdf.y)/100)




def hydroGame():
    pass
def stormGame():
    pass
def popGame():
    pass



def sampleGivenCDF(y):
    u = np.random.uniform()
    if u < y[1]:
        return 1
    else :    
        for idx in range(y.size):
            if(y[idx] < u and y [idx+1] > u):
                return idx
            
            



if __name__ == "__main__":
# The statespace
    global zed

    states = ["dry","wet"]
    T = 365 # 1 month 
    # Possible sequences of events
    transitionName = [["DD","DW"],["WD","WW"]]
    
    p01 = 0.4 # wet day after dry day
    p00 = 1 - p01 # (dry day following a dry day
    p11 = 0.6 # wet day after a wet day  
    p10 = 1 - p11       
    
    transitionMatrix = [[p00,p01],[p10,p11]]

    pi = p01/(1 + p01 - p11)
    r = p11 - p01
    average = pi * T                            # average number of wet days
    variance = pi * (1-pi) * T * (1 + r)/(1-r)  # Variance of the number of wet days from average


    # if sum(transitionMatrix[0])+sum(transitionMatrix[1]) != 2:
    #     print("Somewhere, something went wrong. Transition matrix, perhaps?")
    # else: print("All is gonna be okay, you should move on!! ;)")
    
    
    stats, df = getStats()

    #mu = 120#stats['E_rain']                                      #  mm per day 
    A = np.array([[0.567, 0.086, -0.002], [0.253, 0.504, -0.050], [-0.006, 0.039, 0.244]])
    B = np.array([[0.718, 0, 0], [0.328, 0.637, 0], [0.238, -0.314, 0.873]])


    E_tmin0 = 2#stats['E_tmin_0']
    E_tmax0 = 15#stats['E_tmax_0']
    E_r0 = stats['E_r_0']

    S_tmin0 = 7#stats['VAR_tmin_0']
    S_tmax0 = 5#stats['VAR_tmax_0']
    S_r0 = stats['VAR_r_0']

    #Override
    # S_r0 = S_r0/10

    E_tmin1 = 0#stats['E_tmin_1']
    E_tmax1 = 12#stats['E_tmax_1']
    E_r1 = stats['E_r_1']

    S_tmin1 = 6#stats['VAR_tmin_1']
    S_tmax1 = 5#stats['VAR_tmax_1']
    S_r1 = stats['VAR_r_1']
    # S_r1 = S_r1/10

    initialValue = np.array([0, 0, 0])
    zed = initialValue
    


    C_r0 = -20000
    C_r1 = -900
    C_tmin0 = -5
    C_tmax0 = -6
    C_tmin1 = -3
    C_tmax1 = -4
    wave_tmin0 = []
    wave_tmax0 = []
    wave_r0 = []
    wave_tmin1 = []
    wave_tmax1 = []
    wave_r1 = []
    mu = []


    y = []
    EQ_cdf = []
    EQ_samples = []
    


    for i in range(T):

        wave_tmin0.append(E_tmin0 + C_tmin0 * (np.cos(0.0172*(i - T - 30))))
        wave_tmax0.append(E_tmax0 + C_tmax0 * (np.cos(0.0172*(i - T -30))))
        wave_r0.append(E_r0 + C_r0 * (np.cos(0.0172*(i - T -30))))

        wave_tmin1.append(E_tmin1 + C_tmin1 * (np.cos(0.0172*(i - T -30))))
        wave_tmax1.append(E_tmax1 + C_tmax1 * (np.cos(0.0172*(i - T-30))))
        wave_r1.append(E_r1 + C_r1 * (np.cos(0.0172*(i - T-30))))
        mu.append(80 + 20*np.cos(0.0172*(i - 2*T -30)))



    # print(stats)

    


    t_min = [0]
    t_max = [10]
    r = [6000]
    temp_diff = [10]

    z = [[0,0,0]]


    weatherGame(T)
    earthQwakeGame()



    # print('Average is: ', average)
    # print('Average percent is: ', average * 100/T)
    # print('Variance is: ', variance)
    # # weatherGame(T)
    X = range(0, T)

    
    fig1, axs1 = plt.subplots(3, 2)

    axs1[0][0].plot(X, df['rain'][0:T] )
    axs1[0][0].set_title('Rainy days')
    #plt.grid()

    axs1[1][0].plot(X, t_min, t_max)
    axs1[1][0].set_title('t min')
    
    # axs1[1][0].plot(X, numNodes)
    # axs1[1][0].set_title('# of nodes')

    axs1[0][1].plot(X,  EQ_samples )
    axs1[0][1].set_title('scosse')

    axs1[1][1].plot(X,  r )
    axs1[1][1].set_title('radiation')


    axs1[2][1].plot([x/100 for x in range(1300)],  y )
    axs1[2][1].set_title('AutoRegressivo')

    plt.show()