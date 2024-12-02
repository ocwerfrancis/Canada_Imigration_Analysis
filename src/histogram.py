import pandas as pd
import numpy as np
import matplotlib
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import map_plot as map_plot
import os

from data_processing import df_canada
from analysis import years

'''Question: What is the frequency distribution of the number (population)
   of new immigrants from the various countries to Canada in 2013?
'''

immigants_2013 =df_canada['2013']

# Plotting the Histogram
plt.figure(figsize=(10,6))
sns.set_theme(style="whitegrid")
sns.histplot(immigants_2013, kde=False,bins=20, color='blue', edgecolor='black')

# Add titles and labels
plt.title('Histogram of Immigration from 195 Countries in 2013',fontsize = 16)
plt.xlabel('Number of Immigrants', fontsize = 12)
plt.ylabel('Number of Countries', fontsize = 12)

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "Immigrants_2013_histogram.png")
plt.savefig(output_path, dpi=310, bbox_inches='tight')
plt.close()

print(f"Plot saved at: {output_path}")