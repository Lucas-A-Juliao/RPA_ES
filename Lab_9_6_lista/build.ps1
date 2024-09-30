$exclude = @("venv", "Lab_9_6_lista.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_9_6_lista.zip" -Force