import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import map_plot as map_plot
import os

from data_processing import df_canada

# Clean the Dataset
df_canada.drop(['AREA','REG','DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df_canada.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_canada['Total'] = df_canada.iloc[:, 4:].sum(axis=1)
df_canada.set_index('Country', inplace= True)
df_canada.columns = list(map(str, df_canada.columns))
years = list(map(str, range(1980, 2014)))
