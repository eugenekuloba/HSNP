# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import folium
import math
import os
import time
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
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

# Group the DataFrame by county and count the number of households in each county
county_counts = df.groupby('county_name')['household_id'].count()

# Sort the county counts in ascending order
county_counts = county_counts.sort_values()

# Set the figure size
plt.figure(figsize=(10, 6)) 

# Plot a bar chart of the county counts
county_counts.plot(kind='bar')

# Set the chart title and axis labels
plt.title('Household Counts by County')
plt.xlabel('County')
plt.ylabel('Household Count')

# Rotate the x-axis labels
plt.xticks(rotation=0)  # Adjust the rotation angle as desired

# Create the "plots" directory if it doesn't exist
plot_dir = 'Images'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)

# Save the plot in the "plots" directory
plot_file = os.path.join(plot_dir, 'county_counts.png')
plt.savefig(plot_file)

# Show the chart
plt.show()


# Group the DataFrame by county and count the unique values of Village_Name, Sublocation_Name, Location_Name, and Constituency_Name
county_counts = df.groupby('county_name').nunique()[['village_name', 'sublocation_name', 'location_name', 'constituency_name']]

# Plot four bar graphs, one for each column
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, col in enumerate(county_counts.columns):
    ax = axes[i]
    ax.bar(county_counts.index, county_counts[col])
    ax.set_title(col)
    ax.tick_params(axis='x', rotation=0)

# Save the plot in the "plots" directory
plot_file = os.path.join(plot_dir, 'administration_counts.png')
plt.savefig(plot_file)

plt.tight_layout()
plt.show()

# start cleaning coordinates county by county
# filter by county name
# check the unique counties in the dataframe
county_options = df['county_name'].unique()

# print the available unique counties to allow user to pick
print("Available county options:")
for i, county in enumerate(county_options, start=1):
    print(f"{i}. {county}")

county_choice = input("Enter the number or name corresponding to the county: ")

# Filter selected county from dataset to work with
if county_choice.isdigit():
    county_choice = int(county_choice)
    if county_choice < 1 or county_choice > len(county_options):
        print("Invalid selection.")
        exit()
    selected_county = county_options[county_choice - 1]
else:
    if county_choice not in county_options:
        print("Invalid county name.")
        exit()
    selected_county = county_choice


filtered_county = df[df['county_name'] == selected_county]





print('continue coding \N{winking face}')
