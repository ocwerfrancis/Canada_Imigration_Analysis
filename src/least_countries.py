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

# Sort by 'Total' column and get the top 5 countries
df_canada.sort_values(by='Total', ascending=False, axis=0, inplace=True)
least_5_countries = df_canada.tail(5)

# Transpose to make years rows and countries columns
least_5_countries = least_5_countries[years].transpose()

# Convert the index to integers for clarity
least_5_countries.index = least_5_countries.index.astype(int)

# Reset index and rename columns for plotting
least_5_countries.reset_index(inplace=True)
least_5_countries.rename(columns={'index': 'Year'}, inplace=True)

# Plotting the Area Plot
plt.figure(figsize=(20, 10))
sns.set_theme(style="whitegrid")

# Fill the area under each country's line
for country in least_5_countries.columns[1:]:  # Exclude the 'Year' column
    plt.fill_between(
        least_5_countries['Year'],
        least_5_countries[country],
        alpha=0.8,
        label=country,
     
    )

# Add titles and labels
plt.title('Immigration Trend of 5 Countries with Least Contribution to Immigration', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Immigrants', fontsize=12)
plt.legend(title='Country', fontsize=12,)

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "Least_Immigration_plot.png")
plt.savefig(output_path, dpi=310, bbox_inches='tight')
plt.close()

print(f"Plot saved at: {output_path}")