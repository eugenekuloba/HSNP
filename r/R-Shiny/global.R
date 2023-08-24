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
# Boxplot
ggplotly(
  ggplot(filtered_data) +
    geom_boxplot(mapping = aes(x = county, y = population_count, fill = county))
)


ggplotly(
  ggplot(filtered_data) +
    geom_boxplot(mapping = aes(x = county, y = beneficiary_count, fill = county))
)



ggplotly(
    ggplot(data)+
    geom_bar(mapping = aes(x = county_name,fill=isbeneficiaryhh),position = "dodge")
)

