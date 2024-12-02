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

'''Create a new dataframe that stores that total number of landed immigrants to Canada per year from 1980 to 2013.'''

# Calculate the total number of landed immigrants per year
df_total_immigrants = pd.DataFrame(df_canada[years].sum(axis=0))

# Change the years to float values
df_total_immigrants.index = df_total_immigrants.index.astype(float)

# Reset the index to the default 
df_total_immigrants.reset_index(inplace=True)

# Rename the columns
df_total_immigrants.columns = ['Year', 'Total']



# Plotting the Regression Plot
plt.figure(figsize=(15,10))
sns.set_theme(style="whitegrid")
sns.regplot(x=df_total_immigrants['Year'], y=df_total_immigrants['Total'], color='blue')

# Add titles and labels
plt.title('Total Landed Immigrants to Canada per Year')
plt.xlabel('Year')
plt.ylabel('Total Immigrants')

# Save the plot
output_folder = "visuals"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "total_immigrants_plot.png")
plt.savefig(output_path, dpi=310, bbox_inches='tight')
plt.close()

print(f"Plot saved at: {output_path}")