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

print("All imports have been imported")

def data():
    df = pd.read_excel('Data/County Location_ Raw Data.xlsx')
    return df

# df = df.apply(lambda x: x.str.title() if x.dtype == 'object' else x)
# county_counts = df.groupby('county_name')['household_id'].count()
# county_counts = county_counts.sort_values()
# county_counts = df.groupby('county_name').nunique()[['village_name', 'sublocation_name', 'location_name', 'constituency_name']]


