function getIP{

    (Get-NetIPAddress).ipv4address | Select-String "192*"
    }
Write-Host(getIP)
$IP = getIP

function GetVersion{
    Get-Host | Select-Object Version
    }
Write-Host(GetVersion)
$Version = GetVersion

function GetLocalUser{
    Get-LocalUser
    }

function GetDate{
    Get-Date
    }
Write-Host(GetDate)
$Date = GetDate

Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "lam.martin31@gmail.com" Subject "IT3038c Windows SysInfo" -Body "This is my lab 3 script!  IP Address: $IP, Powershell Version: $Version, Local User: $env:USERNAME, Date: $Date." -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)