import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import map_plot as map_plot
import os

from data_processing import df_canada
from analysis import years

'''Question: What is the immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013?'''

# Filter data for Denmark, Norway, and Sweden
df_countries = df_canada.loc[['Denmark', 'Norway', 'Sweden'], years]

# Transpose the data to have years as rows and countries as columns
df_countries = df_countries.transpose()
df_countries.index = df_countries.index.astype(int)  # Convert index (years) to integers for plotting

# Reset the index for Seaborn compatibility
df_countries.reset_index(inplace=True)
df_countries.rename(columns={'index': 'Year'}, inplace=True)

# Plotting the Histogram
plt.figure(figsize=(12,8))
sns.set_theme(style="whitegrid")

# Plot the histogram of each country
sns.histplot(df_countries['Denmark'], kde=True, bins=20, label='Denmark', color='coral', edgecolor='black',alpha=0.6)
sns.histplot(df_countries['Norway'], kde=True, bins=20, label='Norway', color='darkslateblue', edgecolor='black',alpha=0.6)
sns.histplot(df_countries['Sweden'], kde=True, bins=20, label='Sweden', color='mediumseagreen', edgecolor='black',alpha=0.6)

# Add titles and labels
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years',fontsize=12)
plt.xlabel('Number of Immigrants',fontsize=12)
plt.legend(title='Country',fontsize=12)

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "denmark_norway_sweden_histogram.png")
plt.savefig(output_path, dpi=310, bbox_inches='tight')
plt.close()

print(f"Plot saved at: {output_path}")