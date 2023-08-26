# load necessary libraries
library(shiny)
library(shinydashboard)
library(shinycssloaders)
# define dashboard
dashboardPage(
    dashboardHeader(title = "HSNP BENEFICIARIES",
                    titleWidth = 650,
                    tags$li(class="dropdown",tags$a(href="https://www.hsnp.or.ke/", icon("building"), "HSNP", target="_blank"))),
    dashboardSidebar(
        # sidebarmenu
        sidebarMenu(
            id = "sidebar",
            #  first menu item
            menuItem("Dataset", tabName = "data", icon=icon("database")),
            menuItem(text = "Visualization", tabName = "viz", icon = icon("chart-line")),
            menuItem(text = "Chloropleth Map", tabName = "map", icon = icon("map"))

        )
    ),
    dashboardBody(
        tabItems(
            # first tab item
            tabItem(tabName = "data",
                    # tab box
                    tabBox(id="t1", width=12,
                    tabPanel("About", icon=icon("address-card"),
fluidRow(
    column(width=8,tags$img(src='images/cash-handover.jpg', width=600, height=400),
            tags$br(),
            tags$a("Photo by Evans Dims on Unsplash"), align = "center"),
                        column(width = 4, tags$br(),
                            tags$p("The Hunger Safety Net Programme (HSNP) is an unconditional Government cash transfer programme implemented by the National Drought Management Authority (NDMA) in eight poorest and arid counties, namely; Turkana, Wajir, Mandera, Marsabit, Garissa, Tana River, Isiolo, and Samburu."))
                    )),
                    tabPanel(title = "Structure", icon = icon("address-card"), withSpinner(dataTableOutput("dataTable"))),
                    tabPanel(title = "Data", icon = icon("address-card"), withSpinner(verbatimTextOutput("structure"))),
                    tabPanel(title = "Summary Stats", icon = icon("address-card"), withSpinner(verbatimTextOutput("summary")))
                    )
            ),
            # second tab item/ landing page
            tabItem(tabName = "viz",
                    tabBox(id = "t2", width = 12,
                    tabPanel(title = "Count Plot Of Total Population",withSpinner(plotlyOutput("boxplot"))),
                    tabPanel(title = "Count Plot Of Total Beneficiaries",withSpinner(plotlyOutput("boxplot2"))),
                    tabPanel(title = "Count Plot of Total Population Against Beneficiaries",withSpinner(plotlyOutput("barplot")))
                    )
                    
                    ),

            # third tabItem
            tabItem(tabName = "map",
                    box(withSpinner(plotlyOutput("chloropleth")),width = 15))
        )
    )
)