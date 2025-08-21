# Network Security Basics Guide

A comprehensive guide to fundamental network security concepts, tools, and practices for cybersecurity professionals.

## 📚 Table of Contents

- [Firewalls](#firewalls)
- [VPNs](#vpns)
- [HTTPS](#https)
- [Port Scanning](#port-scanning)
- [Tools](#tools)
- [Practical Examples](#practical-examples)
- [Security Checklist](#security-checklist)

## 🔥 Firewalls

Firewalls act as barriers between trusted internal networks and untrusted external networks, controlling traffic based on security rules.

### Types of Firewalls

- **Packet-filtering firewalls** - Basic filtering based on IP addresses and ports
- **Stateful inspection firewalls** - Track active connections for more intelligent filtering
- **Proxy firewalls** - Act as intermediaries between end-users and requested resources
- **Next-generation firewalls (NGFW)** - Include additional features like intrusion prevention

### Example iptables Rules

```bash
# Allow established connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Default deny policy
iptables -P INPUT DROP
iptables -P FORWARD DROP
```
