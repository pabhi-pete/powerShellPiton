$MQTTKey = '-----BEGIN PRIVATE KEY-----
***KEY START TO STOP***
-----END PRIVATE KEY-----
'
$CAPem = '-----BEGIN CERTIFICATE-----
***UR CA CERT HERE***
-----END CERTIFICATE-----
'
$MQTTPem = '-----BEGIN CERTIFICATE-----
***CERT START TO STOP***
-----END CERTIFICATE-----
'

Write-Output $MQTTKey | Out-File -FilePath C:\opt\fluent\etc\fluent\ssl\MQTTKey.key -Encoding utf8
Write-Output $CAPem | Out-File -FilePath C:\opt\fluent\etc\fluent\ssl\CAPem.pem -Encoding utf8
Write-Output $MQTTPem | Out-File -FilePath C:\opt\fluent\etc\fluent\ssl\MQTTPem.pem -Encoding utf8