import pandas as pd
import os

# Define the path to the data folder
data_folder = os.path.join(os.getcwd(), 'data')
file_path = os.path.join(data_folder, 'Canada.xlsx')

# Check if the file exists
if os.path.exists(file_path):
    # Read the Excel file
    df_canada =pd.read_excel('/home/francis/Projects/Canada_Immigration_Analysis/data/Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=20, skipfooter=2)
    # print("Data Loaded Successfully!")
else:
    print(f"File not found at {file_path}")


