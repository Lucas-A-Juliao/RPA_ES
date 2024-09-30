$exclude = @("venv", "Lab_PDF_RE.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Lab_PDF_RE.zip" -Force