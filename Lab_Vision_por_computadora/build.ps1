$exclude = @("venv", "Lab_Vision_por_computadora.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_Vision_por_computadora.zip" -Force