import pandas as pd
import matplotlib as mpl

df = pd.read_csv('SMHI_Data.csv')

df_helper = df.copy()
df_helper['Datum'] = pd.to_datetime(df_helper['Datum'])
df_helper['Month'] = df_helper['Datum'].dt.month
df_helper['Day'] = df_helper['Datum'].dt.day

seasonal_means = df_helper.groupby(['Month', 'Day', 'Tid (UTC)'])['Lufttemperatur'].transform('mean')

df_filled = df.copy()

df_filled['Lufttemperatur'] = df_filled['Lufttemperatur'].fillna(seasonal_means).round(1)

if df_filled['Lufttemperatur'].isna().any():
    daily_means = df_helper.groupby(['Month', 'Day'])['Lufttemperatur'].transform('mean')
    df_filled['Lufttemperatur'] = df_filled['Lufttemperatur'].fillna(daily_means)


print(df_filled.to_string())
