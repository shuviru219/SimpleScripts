
#Import and deploy the deployment resources--


$errorActionPreference = "stop"
 
# creates object that lets SQL Release connect to the production database
$production = New-DlmDatabaseConnection -ServerInstance your-server\sql2012 -Database WidgetProduction -Username sa -Password p@ssw0rd
 
# imports the deployment resources you reviewed, and runs the deployment
Import-DlmDatabaseRelease C:\Work\Export | Use-DlmDatabaseRelease -DeployTo $production