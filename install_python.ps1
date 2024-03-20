$python_url = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
$python_output_file = "C:\Users\artanim\Downloads\python-3.12.0-amd64.exe"

if (Test-Path $python_output_file) {
    Write-Host "$python_output_file exists - skipping installation"
    return;
}

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $python_url -OutFile $python_output_file
& $python_output_file /passive InstallAllUsers=1 PrependPath=1 Include_test=0


