# define server
function(input,output,session) {

    # structure
    output$structure <- renderPrint(
        # structure of data
        data %>%
            str()
    )

    # summary
    output$summary <- renderPrint(
        # summary of data
        data %>%
            summary()
    )

    # DataTable
    output$dataTable <- renderDataTable(
        data
    )
    
    # plots
    output$boxplot <- renderPlotly({
        ggplotly(
            ggplot(filtered_data) +
                geom_boxplot(mapping = aes(x = county, y = population_count, fill = county))
            )
    
    })
    
    output$boxplot2 <- renderPlotly({
        ggplotly(
            ggplot(filtered_data) +
                geom_boxplot(mapping = aes(x = county, y = beneficiary_count, fill = county))
            )
    
    })

    output$barplot <- renderPlotly({
        ggplotly(
    ggplot(data)+
    geom_bar(mapping = aes(x = county_name,fill=isbeneficiaryhh),position = "dodge")
)
    
    })

    # chloropleth map
    output$chloropleth <- renderPlotly({
       num_colors <- 11
       ggplotly(
    ggplot() +
    geom_sf(data = file, aes(fill = beneficiary_count,
                             text = paste("County:", county, "<br>Constituency:", constituency,"<br>Population Count:",population_count))) +
    scale_fill_gradientn(colors = rev(heat.colors(num_colors))) +
    labs(title = "HSNP Beneficiary Count Map")) %>%
    layout(height = 600, width = 800) 
    })
}