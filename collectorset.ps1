$CounterList = "\Network Interface(vmxnet3 Ethernet Adapter _2)\Current Bandwidth",
		"\Network Interface(vmxnet3 Ethernet Adapter _2)\Bytes Total/sec",
		"\Network Interface(vmxnet3 Ethernet Adapter _2)\Packets Received Errors",
		"\Network Interface(vmxnet3 Ethernet Adapter _2)\Packets Received/sec",
		"\Network Interface(vmxnet3 Ethernet Adapter _2)\Packets Sent/sec",
		"\NVIDIA GPU(#0 NVIDIA RTX A5000 (id=1, NVAPI ID=768))\% GPU Usage",
		"\NVIDIA GPU(#0 NVIDIA RTX A5000 (id=1, NVAPI ID=768))\% GPU Memory Usage",
		"\PhysicalDisk(_Total)\% Disk Time",
		"\Process(_Total)\% User Time"
Get-Counter -Counter $CounterList -SampleInterval 2 -Continuous | Export-Counter -Force -FileFormat CSV -Path C:/Users/artanim/Documents/Utilization/EventsLog/log.csv