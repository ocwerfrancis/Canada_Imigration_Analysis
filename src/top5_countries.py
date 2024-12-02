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

inplace =True

# Sort by 'Total' column and get the top 5 countries
df_canada.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top5_countries = df_canada.head(5)

# Transpose to make years rows and countries columns
df_top5_countries = df_top5_countries[years].transpose()

# Convert the index to integers for clarity
df_top5_countries.index = df_top5_countries.index.astype(int)

# Reset index and rename columns for plotting
df_top5_countries.reset_index(inplace=True)
df_top5_countries.rename(columns={'index': 'Year'}, inplace=True)

# Plotting
plt.figure(figsize=(14, 8))
for country in df_top5_countries.columns[1:]:  # Skip the 'Year' column
    sns.lineplot(data=df_top5_countries, x='Year', y=country, label=country, linewidth=2.5, marker='o')

# Add titles, labels, and legend
plt.title('Top 5 Countries Immigration Trends (1980-2013)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Immigrants', fontsize=12)
plt.legend(title='Country', fontsize=12)
plt.grid(True)

# Save the plot to a folder
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist
output_path = os.path.join(output_folder, "top5_countries_immigration_plot.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # Save with high resolution
plt.close()

# Print confirmation
print(f"Plot saved at: {output_path}")


