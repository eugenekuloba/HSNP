library(shiny)
library(leaflet)
library(dplyr)
library(ggplot2)

# # Load your summarized data (replace 'summarized_data.csv' with your actual file)
# summarized_data <- read.csv("summarized.csv")

# ui <- fluidPage(
#   titlePanel("County Beneficiaries Map"),
#   leafletOutput("map")
# )

# server <- function(input, output) {
#   output$map <- renderLeaflet({
#     leaflet(summarized_data) %>%
#       addTiles() %>%
#       addMarkers(
#         lng = ~longitude,
#         lat = ~latitude,
#         label = ~paste("County: ", county_name, "<br>Beneficiaries: ", beneficiaries_count)
#       )
#   })
# }

# shinyApp(ui, server)

# plot graphs
df <- read.csv("cleaned_csv_data/turkana_cleaned.csv")

ggplot(df)+
  geom_point(aes(x=longitude,y=latitude,color=isbeneficiaryhh))
     
print("finished")