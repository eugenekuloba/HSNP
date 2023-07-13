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



print('continue coding \N{winking face}')
