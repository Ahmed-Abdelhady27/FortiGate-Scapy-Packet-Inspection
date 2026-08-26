from scapy.all import IP, TCP, UDP, DNS, DNSQR, send
import time

target_ip = "10.0.2.100"
src_ip = "10.0.1.100"

# 1. Send TCP SYN
print("[+] Sending TCP SYN Packet...")
send(IP(src=src_ip, dst=target_ip)/TCP(sport=12345, dport=80, flags="S"), count=1)
time.sleep(1)

# 2. Send TCP SYN-ACK
print("[+] Sending TCP SYN-ACK Packet...")
send(IP(src=src_ip, dst=target_ip)/TCP(sport=12345, dport=80, flags="SA"), count=1)
time.sleep(1)

# 3. Send TCP FIN-ACK
print("[+] Sending TCP FIN-ACK Packet...")
send(IP(src=src_ip, dst=target_ip)/TCP(sport=12345, dport=80, flags="FA"), count=1)
time.sleep(1)

# 4. Send UDP Packet (DNS Query)
print("[+] Sending UDP DNS Query Packet...")
send(IP(src=src_ip, dst=target_ip)/UDP(sport=12345, dport=53)/DNS(rd=1, qd=DNSQR(qname="fortinet.com")), count=1)

print("[+] Done!")
