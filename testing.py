import pandas as pd


df = pd.read_csv('tarvisio-2021.csv')
daily_df = pd.read_csv('orari-Tarvisio-2021.csv')
daily_df.fillna(0)
df_wet = (df[df['rain'] > 0] ) 
df_dry = (df[df['rain'] == 0] ) 
for m in range(1, 13):
    mese = daily_df[daily_df['mese'] == m]
    print(int(mese['index'].size/24))
    for g in range(int(mese['index'].size/24)):
        print(mese[mese['giorno'] == g]['radiaz'].mean() )
        

    