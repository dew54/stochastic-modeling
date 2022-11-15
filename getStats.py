import pandas as pd
import json
def getStats():


    df = pd.read_csv('tarvisio-2021.csv')
    # daily_df = pd.read_csv('orari-Tarvisio-2021.csv')
    df_wet = (df[df['rain'] > 0] ) 
    df_dry = (df[df['rain'] == 0] ) 
    # for mese in range(1, 13):
    #     for giorno in daily_df[daily_df['mese'] == mese]

    #     daily_df[daily_df['mese'] == mese]



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
        "C_tmin0"       : -5,
        "C_tmax0"       : -6,
        "C_tmin1"       : -3,
        "C_tmax1"       : -4
        
    }
    
    with open('stats.txt', 'w') as convert_file:
        convert_file.write(json.dumps(desc))
    
    return desc, df
