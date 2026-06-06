from scapy.all import sniff, IP

packet_count = 0

def process_packet(packet):
    global packet_count

    if packet.haslayer(IP):
        packet_count += 1

        print("\n" + "=" * 50)
        print(f"Packet Number: {packet_count}")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")

        if packet.payload:
            print(f"Payload: {packet.payload}")

print("Network Sniffer Started...")
print("Press CTRL+C to stop.")

sniff(prn=process_packet, store=False)