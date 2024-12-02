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

# Filter data for Denmark, Norway, and Sweden

df_countries = df_canada.loc[['Denmark', 'Norway', 'Sweden'],years].transpose()

df_total = pd.DataFrame(df_countries.sum(axis=1))


df_total.reset_index(inplace=True)
df_total.columns = ['Year', 'Total']
df_total['Year'] = df_total['Year'].astype(int)

# Plotting the scatter plot
plt.figure(figsize=(12,8))
sns.set_theme(style="whitegrid")
sns.regplot(x='Year', y='Total', data=df_total,scatter_kws={'s':200})

# Add titles and labels
plt.title('Total Immigrants from Denmark, Norway, and Sweden')
plt.xlabel('Year')
plt.ylabel('Total Immigrants')

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "scatterplot.png")
plt.savefig(output_path, dpi=310, bbox_inches='tight')
plt.close()

print(f"Plot saved at: {output_path}")