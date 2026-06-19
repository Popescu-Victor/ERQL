$action = New-ScheduledTaskAction `
    -Execute "C:\Users\popescu.victor\AppData\Local\Microsoft\WindowsApps\python.exe" `
    -Argument "C:\Users\popescu.victor\Desktop\github\ERQL\cli\cli.py" `
    -WorkingDirectory "C:\Users\popescu.victor\Desktop\github\ERQL\cli"


Register-ScheduledTask -TaskName "DailyScraper" -Action $action