Param(
    [string] $Server = "(local)\SQLEXPRESS",
    [string] $Database = "cc520",
    [string] $Dir = "src"
)


# This script requires the SQL Server module for PowerShell.
# The below commands may be required.

# To check whether the module is installed.
# Get-Module -ListAvailable -Name SqlServer;

# Install the SQL Server Module
# Install-Module -Name SqlServer -Scope CurrentUser

$CurrentDrive = (Get-Location).Drive.Name + ":"

Write-Host ""
Write-Host "Rebuilding database $Database on $Server..."

# Write-Host "Dropping tables..."
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\book_drop\sql\Tables\DropTables.sql"

Write-Host "Creating schema..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\book_drop\sql\Schemas\BookDrop.sql"

Write-Host "Creating tables..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\book_drop\sql\Tables\BookDrop.Person.sql"
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\book_drop\sql\Tables\BookDrop.Review.sql"
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\person\sql\Tables\Person.PersonAddress.sql"

Write-Host "Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\book_drop\sql\Procedures\BookDrop.CreatePerson.sql"
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\book_drop\sql\Procedures\BookDrop.CreateReview.sql"
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\person\sql\Procedures\Person.FetchPerson.sql"
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\person\sql\Procedures\Person.GetPersonByEmail.sql"
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\person\sql\Procedures\Person.SavePersonAddress.sql"
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\person\sql\Procedures\Person.RetrieveAddressesForPerson.sql"
#
# Write-Host "Inserting data..."
# Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\person\sql\Data\Person.AddressType.sql"

Write-Host "Rebuild completed."
Write-Host ""

Set-Location $CurrentDrive
