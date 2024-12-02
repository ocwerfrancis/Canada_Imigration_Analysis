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

# A plot of China and India Migrants with years

# Extract data for China and India
china_india = df_canada.loc[['India', 'China'], years]

# Transpose the data to have years as rows and countries as columns
china_india = china_india.transpose()
china_india.index = china_india.index.astype(int)  # Convert index (years) to integers for plotting

# # Reset the index for Seaborn compatibility
china_india.reset_index(inplace=True)
china_india.rename(columns={'index': 'Year'}, inplace=True)

# Plotting with Seaborn
plt.figure(figsize=(12, 8))
sns.lineplot(data=china_india, x='Year', y='India', marker='o', label='India', color='blue')
sns.lineplot(data=china_india, x='Year', y='China', marker='o', label='China', color='red')

# Add titles and labels
plt.title('Immigration from India and China to Canada (1980-2013)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Immigrants', fontsize=12)
plt.legend(title='Country', fontsize=12)

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "china_india_immigration_plot.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # Save with high resolution
plt.close()

print(f"Plot saved at: {output_path}")
