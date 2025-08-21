# Generate keys

wg genkey | tee privatekey | wg pubkey > publickey

# Basic configuration (/etc/wireguard/wg0.conf)

[Interface]
Address = 10.0.0.1/24
PrivateKey = <server-private-key>
ListenPort = 51820

[Peer]
PublicKey = <client-public-key>
AllowedIPs = 10.0.0.2/32
