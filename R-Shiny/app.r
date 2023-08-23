# load necessary libraries
library(dplyr)
library(ggplot2)
library(sf) 
library(plotly)
library(htmlwidgets)
library(shiny)

# load dataset
data <- sf::st_read("file.geojson")

# Define the UI for the Shiny app
ui <- fluidPage(
  titlePanel("Interactive Map with Shiny"),
  # Place your interactive map here
  plotlyOutput("plot")
)

# Define the server logic for the Shiny app
server <- function(input, output) {
  # Load your spatial data
  data <- st_read("file.geojson")
  
  # Create ggplot with hover text
  gg <- ggplot() +
    geom_sf(data = data, aes(fill = beneficiary_count,
                             text = paste("County:", county, "<br>Constituency:", constituency,"<br>Population Count:",population_count))) +
    scale_fill_gradientn(colors = rev(heat.colors(num_colors))) +
    labs(title = "Beneficiary Counts Map")
  
  # Convert to plotly object
  plotly_map <- ggplotly(gg)
  
  # Display interactive map
  output$plot <- renderPlotly({
    plotly_map
  })
}

# Run the Shiny app
shinyApp(ui, server)


