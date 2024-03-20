$scriptList = @("install_fluentd.ps1", "config_fluentd.ps1", "load_tls_cert.ps1")


foreach ($script in $scriptList) {
    $flagPath = "C:\Users\...\FLAG_FILE_$($script -replace '\.ps1$').txt"
    if (Test-Path $flagPath) {
        Write-Output "[job-name]: $script is still working ..."
    }
    else {
        Write-Output "[job-name]: Starts $script "
        Start-Process powershell.exe -ArgumentList "-File $script" -Wait
    }
}
