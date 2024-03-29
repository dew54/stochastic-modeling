import pandas as pd
from sympy import symbols, Eq, solve
import numpy as np
import population
#import weather
# import json
def getStats():


    df = pd.read_csv('dati-cividale.csv')
    # daily_df = pd.read_csv('orari-Tarvisio-2021.csv')
    df_wet = (df[df['rain'] > 0] ) 
    df_dry = (df[df['rain'] == 0] ) 


    # for mese in range(1, 13):
    #     for giorno in daily_df[daily_df['mese'] == mese]

    #     daily_df[daily_df['mese'] == mese]

    E = np.array([df['rain'] > 0 ]).mean()
    Var = np.array([df['rain'] > 0 ]).var()
    T = len(df['rain'])
    pi = E/T
    g = Var/(E - E**2)
    r1 = (g*T - 1)/(g*T +1)
    p01, p11 = symbols('p01 p11')

    eq1 = Eq(((p01)/(1 + p01 - p11)), pi)
    eq2 = Eq(r1 ,  p11 - p01)

    sol = solve((eq1,eq2), (p01, p11))

    print(sol)


    desc = {                                        # no rain stats
        "E_tmin_0" : int(df_dry['t_min'].mean()),        # means
        "E_tave_0" : int(df_dry['t_ave'].mean()),
        "E_tmax_0" : int(df_dry['t_max'].mean()),
        "E_r_0"    : int(df_dry['radiaz'].mean()),
        "VAR_tmin_0" : int(df_dry['t_min'].std()),       #STDs
        "VAR_tave_0" : int(df_dry['t_ave'].std()),
        "VAR_tmax_0" : int(df_dry['t_max'].std()),
        "VAR_r_0"    : int(df_dry['radiaz'].std()),
                                                    # Rain stats
        "E_tmin_1" : int(df_wet['t_min'].mean()),           
        "E_tave_1" : int(df_wet['t_ave'].mean()),
        "E_tmax_1" : int(df_wet['t_max'].mean()),
        "E_r_1"    : int(df_wet['radiaz'].mean()),
        "VAR_tmin_1" : int(df_wet['t_min'].std()),
        "VAR_tave_1" : int(df_wet['t_ave'].std()),
        "VAR_tmax_1" : int(df_wet['t_max'].std()),
        "VAR_r_1"    : int(df_wet['radiaz'].std()),

        "E_rain"     : int(df_wet['rain'].mean()),
        "VAR_rain"     : int(df_wet['rain'].std()),

        "min_rad_wet"   : int(df_wet['radiaz'].min()),
        'min_rad_dry'   : int(df_dry['radiaz'].min()),
        "min_rad"       : int(df['radiaz'].min()),

        "C_r0"          : -2000,
        "C_r1"          : -900,
        "C_tmin0"       : -4,
        "C_tmax0"       : -4,
        "C_tmin1"       : -3,
        "C_tmax1"       : -4,

        "p01"           : 0.25,#sol[p01],
        "p11"           : 0.8#sol[p11]
        
    }
    
    # with open('stats.txt', 'w') as convert_file:
    #     convert_file.write(json.dumps(desc))
    
    return desc, df


def runSimulation(period):
    weather = Weather(period)
    simulation = []
    dailyRain, t_min, t_max, radiaz = weather.weatherGame()
    dailyStats = []
    
    stats = []
    for d in range(360):
        for t in range(period):        
            oneDayRain.append(dailyRain[d + 360*t])
            oneDayt_min.append(t_min[d + 360*t])
            oneDayt_max.append(t_max[d + 360*t])
            oneDayradiaz.append(radiaz[d + 360*t])
        rainDesc = np.mean(oneDayRain), np.var(oneDayRain)
        t_minDesc = np.mean(oneDayt_min), np.var(oneDayt_min)
        t_maxDesc = np.mean(oneDayt_max), np.var(oneDayt_max)
        radiationDesc =  np.mean(oneDayradiaz), np.var(oneDayradiaz)
        dailyStats.append(rainDesc, t_minDesc, t_maxDesc, radiationDesc)

    return dailyStats
