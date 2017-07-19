Set-ExecutionPolicy -ExecutionPolicy Unrestricted
$errorActionPreference = "stop"
 
#Create and export the deployment resources--

# creates objects that let SQL Release connect to the databases
$stagingState = New-DlmDatabaseConnection -ServerInstance your-server\sql2012 -Database WidgetStaging -Username sa -Password p@ssw0rd
$productionState = New-DlmDatabaseConnection -ServerInstance your-server\sql2012 -Database WidgetProduction -Username sa -Password p@ssw0rd
 
# sets up the deployment resources and exports them to disk
New-DlmDatabaseRelease -Source $stagingState -Target $productionState | Export-DlmDatabaseRelease -Path C:\Work\Export
