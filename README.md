# Port Scanning Tool
 
A simple Python-based port scanner with banner grabbing capabilities for penetration testing and network reconnaissance.
 
## Features
 
- **Port Scanning**: Scan target hosts for open ports (starting from port 80)
- **Banner Grabbing**: Retrieves service banners to identify running services
- **Hostname Resolution**: Supports both IP addresses and domain names
- **HTTP-Aware**: Sends proper HTTP requests to web ports (80, 443, 8080, 8081, 8443)
- **Multi-threading Ready**: Lightweight socket-based implementation
 
## Installation
 
1. Clone the repository:
```bash
git clone https://github.com/md-mohe-med/port-scanning-tool.git
cd port-scanning-tool
```
Install dependency:
```bash

pip install IPy
```

Usage
Run the vulnerability scanner:

bash
python vuln_scan.py
Then enter:

Target IP or domain
Number of ports to scan (starts from port 80)
Path to your vulnerabilities file (optional)
