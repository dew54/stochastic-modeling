import pandas as pd

def getStats():


    df = pd.read_csv('tarvisio-2021.csv')
    # daily_df = pd.read_csv('orari-Tarvisio-2021.csv')
    df_wet = (df[df['rain'] > 0] ) 
    df_dry = (df[df['rain'] == 0] ) 
    # for mese in range(1, 13):
    #     for giorno in daily_df[daily_df['mese'] == mese]

    #     daily_df[daily_df['mese'] == mese]



    desc = {
        "E_tmin_0" : df_dry['t_min'].mean(),           # no rain stats
        "E_tave_0" : df_dry['t_ave'].mean(),
        "E_tmax_0" : df_dry['t_max'].mean(),
        "E_r_0"    : df_dry['radiaz'].mean(),
        "VAR_tmin_0" : df_dry['t_min'].std(),
        "VAR_tave_0" : df_dry['t_ave'].std(),
        "VAR_tmax_0" : df_dry['t_max'].std(),
        "VAR_r_0"    : df_dry['radiaz'].std(),

        "E_tmin_1" : df_wet['t_min'].mean(),           # Rain stats
        "E_tave_1" : df_wet['t_ave'].mean(),
        "E_tmax_1" : df_wet['t_max'].mean(),
        "E_r_1"    : df_wet['radiaz'].mean(),

        "VAR_tmin_1" : df_wet['t_min'].std(),
        "VAR_tave_1" : df_wet['t_ave'].std(),
        "VAR_tmax_1" : df_wet['t_max'].std(),
        "VAR_r_1"    : df_wet['radiaz'].std(),

        "E_rain"     : df_wet['rain'].mean(),
        "VAR_rain"     : df_wet['rain'].std(),

        "min_rad_wet"   : df_wet['radiaz'].min(),
        'min_rad_dry'   : df_dry['radiaz'].min(),
        "min_rad"       : df['radiaz'].min()
        
    }
    print(df_dry['t_max'].mean(), "||", df_dry['t_min'].mean())
    # print(df_wet['t_max'].std(), "||", df_dry['t_max'].std())
    print(df_wet['radiaz'].mean(), "||", df_dry['radiaz'].mean())
    print(df_wet['radiaz'].std(), "||", df_dry['radiaz'].std())
    return desc, df
