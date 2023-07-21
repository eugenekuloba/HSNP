# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import geopandas as gpd
import os
import time

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from shapely.geometry import Point
from tkinter import Tk
from tkinter.filedialog import askopenfilename

