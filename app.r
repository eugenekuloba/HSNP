# load necessary libraries
library(dplyr)
library(sf)
library(readxl)

# read xlsx file
data <- read_excel("cleaned_xlsx_data/cleaned_data.xlsx")
View(data)
 
# Create an sf object with point geometries from lat and long columns
sf_data <- st_as_sf(data, coords = c("longitude", "latitude"), crs = 4326)

# Visualize data
plot(sf_data)
