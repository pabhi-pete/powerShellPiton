$fluentd_path = "C:\opt\fluent\etc\fluent\fluentd.conf"
$fluentContent = '<source>
 @type tail
 read_from_head true
 tag logs.csv
 path C:/Users/.../log.csv
 pos_file pos_file C:/Users/.../logfiles.pos
 <parse>
   @type csv
   parser_type fast
   keys timestamp,cpu_user_time,physical_disk_time,gpu_memory_usage,gpu_usage,packets_sent,packets_received,packets_received_error,bytes_total,current_bandwidth
   time_format %d/%b/%Y:%H:%M:%S %z
 </parse>
</source>

<match logs.csv>
 @type amqp
 host <IP>
 port 5672
 user <username>
 pass <password>
 vhost /
 key <check ur MQTT keys>
 exchange <exchange names MQTT>
 exchange_type direct
 durable true
 heartbeat 10
 tag_key false
 tls false
 verify_ssl false
 tls_key <.key>
 tls_cert <.pem>
 tls_ca_certificates ["ca.pem"]
 tls_verify_peer false
</match>
'
if (Test-Path $fluentd_path) {
    Write-Host "$fluentd_path file exists - Starting configuration"
    Write-Output "$fluentContent" | Out-File -FilePath $fluentd_path -Encoding utf8
}