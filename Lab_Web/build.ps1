$exclude = @("venv", "Lab_Web.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_Web.zip" -Force