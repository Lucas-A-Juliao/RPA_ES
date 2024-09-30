$exclude = @("venv", "Lab_Sap_Browser_test.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_Sap_Browser_test.zip" -Force