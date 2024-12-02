<<<<<<< HEAD
# Canada_imigration_analysis
=======
# Canada Immigration Analysis

This project analyzes immigration trends to Canada, focusing on various source countries and demographics. The data spans multiple years and provides valuable insights for researchers and policymakers From 1980 - 2013.

# Acquire the Data from Kaggle 

Let's download and import our primary Canadian Immigration dataset using pandas's ```read_excel()``` method. Normally, before we can do that, we would need to download a module which pandas requires reading in Excel files. This module was ```openpyxl``` (formerlly xlrd). For your convenience, we have pre-installed this module, so you would not have to worry about that. Otherwise, you would need to run the following line of code to install the openpyxl module:

```pip install openpyxl```

## Now we hav the data 
```import pandas as pd```
```import os```
## Define the path to the data folder
```data_folder = os.path.join(os.getcwd(), 'data')```
```file_path = os.path.join(data_folder, 'Canada.xlsx')```

## Check if the file exists
```if os.path.exists(file_path):```
    ### Read the Excel file
    ```df_canada =pd.read_excel('/home/francis/Projects/Canada_Immigration_Analysis/data/Canada.xlsx',sheet_name='Canada by Citizenship', skiprows=20, skipfooter=2)```
    ### ```print("Data Loaded Successfully!")```
```else:```
    ```print(f"File not found at {file_path}")```

The main types stored in pandas objects are ```float, int, bool, datetime64[ns], datetime64[ns, tz], timedelta[ns], category```, and ```object (string)```. In addition, these dtypes have item sizes, e.g. ```int64``` and ```int32```.

Let's clean the data set to remove a few unnecessary columns. We can use pandas ```drop()``` method as follows:
>>>>>>> 14263b9 (First Commit)
