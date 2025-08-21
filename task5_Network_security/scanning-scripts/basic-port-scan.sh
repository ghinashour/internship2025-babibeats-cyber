#!/bin/bash
# Basic Port Scanner Script
# Author: [Your Name]
# Date: $(date +%Y-%m-%d)
# Description: Simple TCP port scanner using /dev/tcp
# Usage: ./basic-port-scan.sh <target> [start-port] [end-port]

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to display usage
usage() {
    echo -e "${BLUE}Usage:${NC} $0 <target> [start-port] [end-port]"
    echo -e "${BLUE}Examples:${NC}"
    echo "  $0 example.com"
    echo "  $0 192.168.1.1 1 100"
    echo "  $0 localhost 20 443"
    exit 1
}

# Function to check if a port is open
check_port() {
    local target=$1
    local port=$2
    
    # Try to connect to the port with timeout
    timeout 1 bash -c "echo >/dev/tcp/$target/$port" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Port $port: OPEN${NC}"
        return 0
    else
        echo -e "${RED}Port $port: CLOSED${NC}"
        return 1
    fi
}

# Function to get service name from port number
get_service_name() {
    local port=$1
    case $port in
        20) echo "FTP Data" ;;
        21) echo "FTP Control" ;;
        22) echo "SSH" ;;
        23) echo "Telnet" ;;
        25) echo "SMTP" ;;
        53) echo "DNS" ;;
        80) echo "HTTP" ;;
        110) echo "POP3" ;;
        143) echo "IMAP" ;;
        443) echo "HTTPS" ;;
        445) echo "SMB" ;;
        993) echo "IMAPS" ;;
        995) echo "POP3S" ;;
        1433) echo "MSSQL" ;;
        3306) echo "MySQL" ;;
        3389) echo "RDP" ;;
        5432) echo "PostgreSQL" ;;
        5900) echo "VNC" ;;
        27017) echo "MongoDB" ;;
        *) echo "Unknown" ;;
    esac
}

# Main script execution
main() {
    # Check if target is provided
    if [ $# -lt 1 ]; then
        usage
    fi

    TARGET=$1
    START_PORT=${2:-1}
    END_PORT=${3:-1000}

    # Validate ports
    if [ $START_PORT -lt 1 ] || [ $START_PORT -gt 65535 ]; then
        echo -e "${RED}Error: Start port must be between 1 and 65535${NC}"
        exit 1
    fi

    if [ $END_PORT -lt 1 ] || [ $END_PORT -gt 65535 ]; then
        echo -e "${RED}Error: End port must be between 1 and 65535${NC}"
        exit 1
    fi

    if [ $START_PORT -gt $END_PORT ]; then
        echo -e "${RED}Error: Start port cannot be greater than end port${NC}"
        exit 1
    fi

    echo -e "${BLUE}==================================================${NC}"
    echo -e "${YELLOW}Starting port scan on: $TARGET${NC}"
    echo -e "${YELLOW}Port range: $START_PORT - $END_PORT${NC}"
    echo -e "${YELLOW}Start time: $(date)${NC}"
    echo -e "${BLUE}==================================================${NC}"
    echo

    OPEN_PORTS=()
    TOTAL_PORTS=$((END_PORT - START_PORT + 1))
    CURRENT=0

    for ((port=START_PORT; port<=END_PORT; port++)); do
        CURRENT=$((CURRENT + 1))
        PERCENT=$((CURRENT * 100 / TOTAL_PORTS))
        
        # Show progress every 10 ports or for small ranges
        if [ $TOTAL_PORTS -le 50 ] || [ $((port % 10)) -eq 0 ]; then
            echo -ne "${BLUE}Scanning: $CURRENT/$TOTAL_PORTS ($PERCENT%) - Port: $port\r${NC}"
        fi
        
        if check_port "$TARGET" "$port"; then
            SERVICE=$(get_service_name $port)
            OPEN_PORTS+=("$port ($SERVICE)")
        fi
    done

    echo
    echo -e "${BLUE}==================================================${NC}"
    echo -e "${YELLOW}Scan completed at: $(date)${NC}"
    echo -e "${YELLOW}Total ports scanned: $TOTAL_PORTS${NC}"
    echo -e "${YELLOW}Open ports found: ${#OPEN_PORTS[@]}${NC}"
    echo -e "${BLUE}==================================================${NC}"

    if [ ${#OPEN_PORTS[@]} -gt 0 ]; then
        echo -e "${GREEN}Open ports:${NC}"
        for port_info in "${OPEN_PORTS[@]}"; do
            echo -e "  ${GREEN}• $port_info${NC}"
        done
    else
        echo -e "${RED}No open ports found in the specified range.${NC}"
    fi

    echo -e "${BLUE}==================================================${NC}"
}

# Handle script interruption
trap 'echo -e "\n${RED}Scan interrupted by user. Exiting...${NC}"; exit 1' INT

# Run main function with all arguments
main "$@"