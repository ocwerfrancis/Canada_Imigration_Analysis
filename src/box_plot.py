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

# Load the data
df_japan = df_canada.loc[['Japan'], years]

# Transpose the data to have years as rows and countries as columns
df_japan = df_japan.transpose().reset_index()
df_japan.columns = ['Year', 'Number of Immigrants']
df_japan['Year'] = df_japan['Year'].astype(int)


# Plotting the Box Plot
plt.figure(figsize=(12,8))
sns.set_theme(style="whitegrid")
sns.boxplot(x=df_japan['Number of Immigrants'], data=df_japan)

# Add titles and labels
plt.title('Box Plot of Immigrants from Japan from 1980 - 2013', fontsize=16)
plt.xlabel('Year', fontsize=12)


# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "box_plot_japan_immigration.png")
plt.savefig(output_path, dpi=320, bbox_inches='tight')
plt.close()

print(f"Plot saved at: {output_path}")

print(df_japan.describe())