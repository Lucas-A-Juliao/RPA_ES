$exclude = @("venv", "Lab_Webscrap.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_Webscrap.zip" -Force