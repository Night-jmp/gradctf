from scapy.all import *
import time

flag = "fitsec{p!ng_as_4_c0v3rt_ch4nn3l}"

for byte in flag:
    pkt = ICMP(type=8, id=ord(byte))
    sendp(pkt)
    time.sleep(1)
