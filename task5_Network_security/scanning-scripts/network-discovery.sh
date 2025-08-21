#!/usr/bin/env python3
"""
Network Discovery Tool
Scans a network range for active hosts
"""

import subprocess
import ipaddress
import threading
import socket

def ping_host(ip):
    """Ping a host to check if it's alive"""
    try:
        result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], 
                              capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(str(ip))[0]
            except socket.herror:
                hostname = "Unknown"
            print(f"Active: {ip} ({hostname})")
    except:
        pass

def network_discovery(network_range):
    """Discover active hosts in a network range"""
    print(f"Scanning network: {network_range}")
    print("=" * 50)
    
    network = ipaddress.ip_network(network_range, strict=False)
    threads = []
    
    for ip in network.hosts():
        thread = threading.Thread(target=ping_host, args=(ip,))
        threads.append(thread)
        thread.start()
        
        # Limit to 50 concurrent threads
        if len(threads) >= 50:
            for t in threads:
                t.join()
            threads = []
    
    # Wait for remaining threads
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python network-discovery.py <network_range>")
        print("Example: python network-discovery.py 192.168.1.0/24")
        sys.exit(1)
    
    network_discovery(sys.argv[1])