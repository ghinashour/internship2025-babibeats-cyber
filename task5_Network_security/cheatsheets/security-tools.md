````markdown
# Security Tools Cheat Sheet

## Network Scanning Tools

### Nmap

```bash
# Basic network discovery
nmap -sn 192.168.1.0/24

# Comprehensive scan
nmap -A -T4 target.com

# UDP scan
nmap -sU -p 1-1000 target.com
```
````

### Netcat

# Port listening

nc -lvnp 4444

# Port scanning

nc -zv target.com 1-1000

# File transfer

nc -lvnp 4444 > received_file.txt # Receiver
nc -w 3 target.com 4444 < file.txt # Sender

### ping & traceroute

# Basic ping

ping target.com

# Continuous ping

ping -t target.com

# Traceroute

traceroute target.com

# On Windows:

tracert target.com

### Nikto (web scanner)

# Basic web scan

nikto -h http://target.com

# Scan with specific port

nikto -h http://target.com -p 443

# Save output

nikto -h http://target.com -o results.txt

### openVAS

# Start OpenVAS

sudo gvm-start

# Access web interface: https://localhost:9392

# Update vulnerability databases

sudo greenbone-feed-sync --type SCAP
sudo greenbone-feed-sync --type CERT
sudo greenbone-feed-sync --type GVMD_DATA

### packet analysis

## wireshark

# Capture packets

tshark -i eth0 -w capture.pcap

# Read capture file

tshark -r capture.pcap

# Filter HTTP traffic

tshark -r capture.pcap -Y "http"

# Extract files from pcap

tshark -r capture.pcap --export-objects http,./exported_files/

## tcp dump

# Capture all traffic

tcpdump -i any -w capture.pcap

# Capture specific host

tcpdump -i eth0 host target.com -w capture.pcap

# Capture specific port

tcpdump -i eth0 port 80 -w capture.pcap

# Read capture file

tcpdump -r capture.pcap

### password tools

## John the Ripper

# Crack password hashes

john hashes.txt

# Show cracked passwords

john --show hashes.txt

# Use wordlist

john --wordlist=wordlist.txt hashes.txt

## hashcat

# Basic hash cracking

hashcat -m 0 hashes.txt wordlist.txt

# Brute force attack

hashcat -m 0 -a 3 hashes.txt ?l?l?l?l?l

# Show results

hashcat --show hashes.txt

### web application tools

## SQL map

# Basic SQL injection test

sqlmap -u "http://target.com/page.php?id=1"

# Test with cookies

sqlmap -u "http://target.com/page.php?id=1" --cookie="PHPSESSID=abc123"

# Dump database

sqlmap -u "http://target.com/page.php?id=1" --dump

## dirbuster

# Directory brute force

dirb http://target.com

# Use custom wordlist

dirb http://target.com /usr/share/wordlists/dirb/common.txt

# Specific extensions

dirb http://target.com -X .php,.html,.txt
