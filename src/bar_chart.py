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

'''Question: Let's compare the number of Icelandic immigrants (country = 'Iceland') to Canada from year 1980 to 2013.'''

# Get the data
df_iceland = df_canada.loc['Iceland', years]

# Convert the data to dataframe
df_iceland = pd.DataFrame(df_iceland)
df_iceland.reset_index(inplace=True)
df_iceland.columns = ['Year', 'Number of Immigrants']
df_iceland['Year'] = df_iceland['Year'].astype(int)

# Plotting the barchart
plt.figure(figsize=(20,10))
sns.set_theme(style="whitegrid")
sns.barplot(data=df_iceland, x='Year', y='Number of Immigrants', color='blue',palette='viridis')

# Add titles and labels
plt.title('Icelandic Immigrants to Canada (1980-2013)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Immigrants', fontsize=12)

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "iceland_immigration_plot.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # Save with high resolution
plt.close()  # Close the plot to free memory

print(f"Plot saved at: {output_path}")