# -----------------------------------------------------------------------------------------------------------------------------------------------
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
import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from shapely.geometry import Point
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename,askopenfilenames

# ---------------------------------------------------------------------------------------------------------------------------------
# Get the current time
current_time = datetime.datetime.now().time()

# Determine the appropriate greeting based on the current time
greeting = ""
if current_time < datetime.time(12):
    greeting = "Good Morning"
    emoji = "\u2615"  # Coffee emoji
elif current_time < datetime.time(18):
    greeting = "Good Afternoon"
    emoji = "\U0001F44D"  # Thumbs up emoji
else:
    greeting = "Good Evening"
    emoji = "\U0001F44D"  # Thumbs up emoji

# Print the  message
print("The script is now beginning.")
print(f"{greeting}!")
print(f'{emoji}')

# Open file selection dialog
Tk().withdraw()
filename = askopenfilename(title='Select Excel file', filetypes=[('Excel Files', '*.xlsx')])

# Read the selected Excel file
df = pd.read_excel(filename)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------------


# Data Cleaning
print('-------------------Data Cleaning-------------------')


# Convert all object data to title case
df = df.apply(lambda x: x.str.lower() if x.dtype == 'object' else x)

# Remove spacing before the object
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

# Convert all column names to lower case
df.columns = df.columns.str.lower()

# convert column datatype
columns_to_convert = ['household_id', 'village_id','sublocation_id','location_id','constituency_id','county_id']
for column in columns_to_convert:
    df[column] = df[column].astype('object')    
   
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

# def correct_coord():
def correct_coord(df):
    # If latitude is greater than longitude, interchange them
    mask = df['latitude'] > df['longitude']
    df.loc[mask, ['latitude', 'longitude']] = df.loc[mask, ['longitude', 'latitude']].values
    
    # Calculate the correction factor for latitude
    factors_lat = df['latitude'].apply(lambda x: 10 ** -(len(str(int(x))) - 1))
    
    # Divide each latitude value by its correction factor
    df['latitude'] = df['latitude'] * factors_lat
    
    # Calculate the correction factor for longitude
    factors_lon = df['longitude'].apply(lambda x: 10 ** -(len(str(int(x))) - 2))
    
    # Divide each longitude value by its correction factor
    df['longitude'] = df['longitude'] * factors_lon
    
    return df

correct_coord(df)


# filter by county name
print('-------------------------start cleaning coordinates county by county----------------------------')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define the cleaning function
def clean_coordinates(df):
    # Filter by county name
    start_time = time.time()  # Record the start time
    county_options = df['county_name'].unique()

    # Print the available unique counties to allow the user to pick
    print("Available county options:")
    for i, county in enumerate(county_options, start=1):
        print(f"{i}. {county}")

    county_choice = input("Enter the number or name corresponding to the county (or 'q' to quit): ")

    if county_choice.lower() == 'q':
        print("Exiting the program...")
        return False

    # Filter selected county from the dataset to work with
    if county_choice.isdigit():
        county_choice = int(county_choice)
        if county_choice < 1 or county_choice > len(county_options):
            print("Invalid selection.")
            return True
        selected_county = county_options[county_choice - 1]
    else:
        if county_choice not in county_options:
            print("Invalid county name.")
            return True
        selected_county = county_choice

    filtered_county = df[df['county_name'] == selected_county]

    print('--------------------- Info on selected county -------------------')
    print(f"County: {selected_county}")
    print(filtered_county.info())

    # Create a figure with a single subplot
    fig, ax = plt.subplots(figsize=(8, 5))

    # Create a boxplot for the latitude and longitude columns
    sns.boxplot(data=filtered_county[['latitude', 'longitude']], orient='h', ax=ax, palette='pastel')

    # Set the chart title and axis labels
    ax.set_title('Latitude and Longitude Boxplot', fontsize=14)
    ax.set_xlabel('Coordinate Value', fontsize=12)
    ax.set_ylabel('Coordinate Type', fontsize=12)
    ax.tick_params(labelsize=10)

    # Save the plot
    plot_file = os.path.join(plot_dir, f'{selected_county}_coord_before_cleaning.png')
    plt.savefig(plot_file)

    # Show the chart
    plt.show()

    # Perform coordinate cleaning
    filtered_county = correct_coord(filtered_county)

    # Prompt user to open file
    # Open file selection dialog
    Tk().withdraw()
    filename = askopenfilename(title='Select Shapefile (Pick for the county you filtered)', filetypes=[('Shapefile', '*.shp')])

    # Read the selected shapefile into a GeoDataFrame
    selected_boundary = gpd.read_file(filename)

    # Function to check if a coordinate is in the selected boundary
    def is_coordinate_in_selected_boundary(latitude, longitude):
        point = Point(longitude, latitude)
        return selected_boundary.contains(point).any()

    # Iterate through the DataFrame rows and update coordinates if necessary
    for index, row in filtered_county.iterrows():
        latitude = row['latitude']
        longitude = row['longitude']

        if not is_coordinate_in_selected_boundary(latitude, longitude):
            # Assign random coordinates within the county boundary
            while True:
                # Set the latitude range to cover the approximate area of the selected county
                random_latitude = random.uniform(selected_boundary.bounds['miny'], selected_boundary.bounds['maxy'])
                # Set the longitude range to cover the approximate area of the selected county
                random_longitude = random.uniform(selected_boundary.bounds['minx'], selected_boundary.bounds['maxx'])

                if is_coordinate_in_selected_boundary(random_latitude, random_longitude):
                    # Found a random coordinate within the selected boundaries and update the DataFrame
                    filtered_county.at[index, 'latitude'] = random_latitude
                    filtered_county.at[index, 'longitude'] = random_longitude
                    break

    # Create a figure with a single subplot
    fig, ax = plt.subplots(figsize=(8, 5))

    # Create a boxplot for the latitude and longitude columns
    sns.boxplot(data=filtered_county[['latitude', 'longitude']], orient='h', ax=ax, palette='pastel')

    # Set the chart title and axis labels
    ax.set_title('Latitude and Longitude Boxplot', fontsize=14)
    ax.set_xlabel('Coordinate Value', fontsize=12)
    ax.set_ylabel('Coordinate Type', fontsize=12)
    ax.tick_params(labelsize=10)

    # Save the plot
    plot_file = os.path.join(plot_dir, f'{selected_county}_coord_after_cleaning.png')
    plt.savefig(plot_file)

    # Show the chart
    plt.show()

    # save new file as xlsx
    output_dir = "cleaned_xlsx_data"
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
    output_file = os.path.join(output_dir, f"{selected_county}_cleaned.xlsx")
    filtered_county.to_excel(output_file, index=False)
    print(f"Cleaned data saved as {output_file}")


    # save new file as csv (for GIS)
    output_dir = "cleaned_csv_data"
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)  
    output_file = os.path.join(output_dir, f"{selected_county}_cleaned.csv")
    filtered_county.to_csv(output_file, index=False)
    print(f"Cleaned data saved as {output_file}")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    # Print the estimated waiting time
    print(f"Estimated waiting time: {elapsed_time:.2f} seconds")

    return True

    
# Main loop
while True:
    if not clean_coordinates(df):
        break


#  Provide user with option to concantenate xlxs file to have one large dataset
# Ask the user if they want to concatenate multiple files
concat_option = input("Do you want to concatenate multiple XLSX files? (Y/N): ")

if concat_option.upper() == "Y":
    # Prompt the user to select the XLSX files
    Tk().withdraw()
    xlsx_files = askopenfilenames(title="Select XLSX files to concatenate", filetypes=[("XLSX Files", "*.xlsx")])

    if xlsx_files:
        # Read the selected XLSX files and append them to a list of DataFrames
        dfs = []
        for file in xlsx_files:
            df = pd.read_excel(file)
            dfs.append(df)

        if dfs:
            # Concatenate the DataFrames
            concatenated_df = pd.concat(dfs)

            # Prompt the user to select the output file location and name
            Tk().withdraw()
            output_concatenated_file = asksaveasfilename(
                title="Save Concatenated XLSX File As",
                filetypes=[("XLSX File", "*.xlsx")],
                defaultextension=".xlsx"
            )

            if output_concatenated_file:
                # Save the concatenated DataFrame as an Excel file
                concatenated_df.to_excel(output_concatenated_file, index=False)
                print(f"Concatenated data saved as {output_concatenated_file}")
# ------------------------------------------------------------------------------------------------------------------------------------



# Print the farewell message
print("The script is finally over.")
print(f"{greeting}!")
print(f'{emoji}')


print('continue coding \N{winking face}')
