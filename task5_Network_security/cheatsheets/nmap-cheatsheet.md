````markdown
# Nmap Cheat Sheet

## Basic Scans

```bash
# Basic scan
nmap target.com

# Scan specific ports
nmap -p 80,443,22 target.com

# Scan port range
nmap -p 1-1000 target.com

# Scan all ports (slow)
nmap -p- target.com

# Scan most common ports (fast)
nmap -F target.com
```
````

# Ping sweep only (no port scan)

nmap -sn 192.168.1.0/24

# Skip host discovery (assume hosts are up)

nmap -Pn target.com

# DNS resolution

nmap -R target.com # Always resolve
nmap -n target.com # Never resolve

# script scanning

# Use default scripts

nmap -sC target.com

# Use specific script category

nmap --script vuln target.com
nmap --script discovery target.com
nmap --script auth target.com

# Use specific script

nmap --script http-title target.com
nmap --script ssl-enum-ciphers target.com

# Update script database

nmap --script-updatedb

# Timing templates (0-5)

nmap -T0 target.com # Paranoid (very slow)
nmap -T1 target.com # Sneaky
nmap -T2 target.com # Polite
nmap -T3 target.com # Normal (default)
nmap -T4 target.com # Aggressive
nmap -T5 target.com # Insane

# Host timeout

nmap --host-timeout 30m target.com

# Min/max parallel hosts

nmap --min-hostgroup 64 --max-hostgroup 1024 target.com

# Normal output to file

nmap -oN results.txt target.com

# XML output

nmap -oX results.xml target.com

# Grepable output

nmap -oG results.grep target.com

# All formats

nmap -oA results target.com

# Append to file

nmap -oN results.txt --append-output target.com

# HTTP information

nmap --script http-headers,http-title -p 80,443 target.com

# SSL/TLS information

nmap --script ssl-cert,ssl-enum-ciphers -p 443 target.com

# Vulnerability scan

nmap --script vuln target.com

# SMB information

nmap --script smb-os-discovery,smb-enum-shares -p 445 target.com

# FTP anonymous check

nmap --script ftp-anon -p 21 target.com
