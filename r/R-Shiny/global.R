# HSNP BENECIARY DATASET
# load reuired libraries
library(dplyr)
library(readxl)
library(sf)
library(ggplot2)
library(plotly)
# read dataset
data <- read_excel("data/final-data.xlsx")
file <- sf::st_read("data/file.geojson")

# structure of the data
data %>%
    str()

# summary of data
data %>%
    summary()

# head of data
data %>%
    head()

# filter counties
filtered_data <- file %>%
  filter(county %in% c("marsabit", "turkana", "mandera", "wajir"))
# second menu item visualization


# Create an interactive boxplot using plotly
# Boxplot Population Count
ggplotly(
  ggplot(filtered_data) +
    geom_boxplot(mapping = aes(x = county, y = population_count, fill = county))
)

# Boxplot Beneficiary Count
ggplotly(
  ggplot(filtered_data) +
    geom_boxplot(mapping = aes(x = county, y = beneficiary_count, fill = county))
)


# Population Count Against Beneficiary Count
ggplotly(
    ggplot(data)+
    geom_bar(mapping = aes(x = county_name,fill=isbeneficiaryhh),position = "dodge")
)

# chloropleth map
 # Create ggplot with hover text
num_colors = 11

ggplot() +
    geom_sf(data = file, aes(fill = beneficiary_count,
                             text = paste("County:", county, "<br>Constituency:", constituency,"<br>Population Count:",population_count))) +
    scale_fill_gradientn(colors = rev(heat.colors(num_colors))) +
    labs(title = "Beneficiary Counts Map")

