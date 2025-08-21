#!/bin/bash
# Ping Sweep Script
# Usage: ./ping-sweep.sh <network> [timeout]

NETWORK=$1
TIMEOUT=${2:-1}

if [ -z "$NETWORK" ]; then
    echo "Usage: ./ping-sweep.sh <network> [timeout]"
    echo "Example: ./ping-sweep.sh 192.168.1.0 1"
    exit 1
fi

echo "Starting ping sweep for network: $NETWORK"
echo "========================================="

# Extract network prefix
PREFIX=$(echo $NETWORK | cut -d'.' -f1-3)

for host in {1..254}; do
    ip="$PREFIX.$host"
    # Ping with timeout and check if successful
    ping -c 1 -W $TIMEOUT $ip > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        # Try to get hostname
        hostname=$(nslookup $ip | grep 'name =' | awk '{print $4}' | cut -d'.' -f1)
        if [ -z "$hostname" ]; then
            hostname="Unknown"
        fi
        echo "Host found: $ip ($hostname)"
    fi
done

echo "Ping sweep completed."