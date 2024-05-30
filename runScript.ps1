# CD into the directory where the script is located and run the script
Set-Location C:\Users\willi\Documents\coding_projects\APOD_Wallpaper_Script
python script.py

$imageFolder = Get-Content ./userDefinedVariables.json -Raw | ConvertFrom-Json | Select-Object -ExpandProperty IMAGE_FOLDER
$regKey = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP'

# Create registry key if it doesn't exist
if (-not (Test-Path $regKey)) {
    New-Item -Path $regKey -Force | Out-Null
}

# Edit the registry to set the lock screen and desktop background to the APOD collage image
New-ItemProperty -Path $regKey -Name "LockScreenImageStatus" -Value "1" -PropertyType DWORD -Force | Out-Null
New-ItemProperty -Path $regKey -Name "LockScreenImagePath" -Value "$imageFolder\collage.jpg" -PropertyType STRING -Force | Out-Null
New-ItemProperty -Path $regKey -Name "LockScreenImageUrl" -Value "$imageFolder\collage.jpg" -PropertyType STRING -Force | Out-Null

New-ItemProperty -Path $regKey -Name "DesktopImageStatus" -Value "1" -PropertyType DWORD -Force | Out-Null
New-ItemProperty -Path $regKey -Name "DesktopImagePath" -Value "$imageFolder\collage.jpg" -PropertyType STRING -Force | Out-Null
New-ItemProperty -Path $regKey -Name "DesktopImageUrl" -Value "$imageFolder\collage.jpg" -PropertyType STRING -Force | Out-Null

# Restart the explorer process to apply the changes immediately rather than on computer restart
taskkill /f /im explorer.exe
start explorer.exe