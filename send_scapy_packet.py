#!/usr/bin/env python3
from scapy.all import *
import os
os.sys.path.append('/usr/local/bin/')

def pkt1():
   # SYN
   ip=IP(src='127.0.0.1', dst='8.8.8.8')
   SYN=TCP(dport=443,flags='SP',seq=100004)
   send(ip/SYN)

def pkt2():
   pkt=IP(src='127.0.0.1', dst='88.88.88.88')/TCP(sport=88, dport=888)/Raw(load="GET /test HTTP/1.1\r\nHost: www.testtest.com\r\n\r\n")
   send(pkt)

if __name__ == "__main__":
	pkt1()
	pkt2()