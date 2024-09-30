$exclude = @("venv", "Lab_ecxel.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_ecxel.zip" -Force