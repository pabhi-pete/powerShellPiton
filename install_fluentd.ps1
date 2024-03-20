$fluentd_url = "https://s3.amazonaws.com/packages.treasuredata.com/5/windows/fluent-package-5.0.1-x64.msi"
$fluentd_file = "C:\Users\...\Downloads\fluent-package-5.0.1-x64.msi"
$fluentd_installed_log = "C:\Users\...\Documents\Utilization\msilog.log"

if (Test-Path $fluentd_file) {
    Write-Host "$fluentd_file exists - skipping installation"
    return;
}

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $fluentd_url -OutFile $fluentd_file
msiexec.exe /I $fluentd_file /QN /L*V $fluentd_installed_log