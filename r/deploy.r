# install rsconnect
install.packages('rsconnect')

# authorize account
rsconnect::setAccountInfo(name='hsnp',
			  token='FB0D3DCC31A8B9A72B1A8ECA05D2926F',
			  secret='IS8SaR7MbM0sOWcDb3Vhwh1PqmzyI2AQnNGM5PTy')

# deploy 
library(rsconnect)
rsconnect::deployApp('R-Shiny/')
