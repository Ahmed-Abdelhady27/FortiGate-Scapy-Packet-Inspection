 FortiGate Stateful Packet Inspection & Scapy Analysis Lab

This project demonstrates how a stateful firewall processes, inspects, and logs different Layer 4 connection states (TCP & UDP) generated using custom raw packets crafted via Python's **Scapy** library.

Network Topology
 *Kali Linux (`10.0.1.100`):** Traffic Generator on `port2`
 *FortiGate VM (`10.0.1.1` / `10.0.2.1`):** Stateful Firewall
 *Target Node (`10.0.2.100`):** Destination on `port3`

Key Features & Findings
 *Custom Packet Crafting:** Utilized Scapy to inject specific TCP flag combinations (`SYN`, `SYN-ACK`, `FIN-ACK`) and connectionless UDP datagrams.
 *Stateful Session Consolidation:** Verified that FortiGate merges TCP handshake and teardown packets of the same 4-tuple into a single consolidated session log entry.
 *Real-time Diagnostics:** Executed real-time CLI packet captures (`diagnose sniffer packet any 'host 10.0.1.100' 4`) to track ingress (`port2`) and egress (`port3`) interface traversals.
 *Layer 2/3 Adjacency Resolution:** Configured explicit gateway routes and interface subnets to ensure ARP resolution and route table lookup precede policy enforcement.

Execution
`bash
sudo python3 scripts/test_packets.py
