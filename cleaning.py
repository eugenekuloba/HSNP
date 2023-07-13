# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import folium
import math
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
import geopandas as gpd
from shapely.geometry import Point
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Open file selection dialog
Tk().withdraw()
filename = askopenfilename(title='Select Excel file', filetypes=[('Excel Files', '*.xlsx')])

# Read the selected Excel file
df = pd.read_excel(filename)

# Data Understanding
print('-------------------Data Understanding-------------------')

# Print dataset head
# Ask the user for the number of rows to view
num_rows = int(input("Enter the number of rows to view: "))

# Print the specified number of rows from the dataset
print(df.head(num_rows))

# Print shape of dataset
print('Columns = ', df.shape)


# Print data info
df.info()

# Check for null values
df.isna().sum()

# Check for duplicates
df.duplicated().any()


# Data Cleaning
print('-------------------Data Cleaning-------------------')

# Convert all object data to title case
df = df.apply(lambda x: x.str.lower() if x.dtype == 'object' else x)

# Remove spacing before the object
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

# Convert all column names to lower case
df.columns = df.columns.str.lower()

# Check the counties in the dataset
print('Counties in the dataset are:')

print(df['county_name'].unique())

# Sort the DataFrame by a specific column in ascending order
df = df.sort_values('village_name', ascending=True)

print('------------------Sorted Dataframe with ascending order with village names-------------------')
# print dataframe head
print('-----------------dataframe head--------------')
print(df.head())

# print dataframe tail
print('-----------------dataframe tail--------------')
print(df.tail())









print('continue coding \N{winking face}')
