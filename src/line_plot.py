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



# VISUALIZATION OF DATA USING MATPLOTLIB

#  Line Plotting
Haiti = df_canada.loc['Haiti', years]

# Convert the Series to a DataFrame
haiti_df = Haiti.reset_index()
haiti_df.columns = ['Year', 'Number of Immigrants']
haiti_df['Year'] = haiti_df['Year'].astype(int)

# Create folder for saving plots if it doesn't exist
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True) 

# Plot Using Seabon
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,6))
sns.lineplot(data=haiti_df, x='Year', y='Number of Immigrants',markers='o', color='blue',)

# Add titles amd lables
plt.title('Immigration from Haiti to Canada (1980-2013)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Immigrants', fontsize=12)

# Save the plot
output_path = os.path.join(output_folder, "haiti_immigration_plot.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # Save with high resolution
plt.close()  # Close the plot to free memory

print(f"Plot saved at: {output_path}")

