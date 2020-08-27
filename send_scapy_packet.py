from scapy.all import *
import os
os.sys.path.append('/usr/local/bin/')

# SYN
def pkt1():
   eth = Ether(dst='11:ff:ff:ff:ff:ff', src='01:02:03:04:05:06')
   ip=IP(src='10.0.0.12', dst='10.0.0.10')
   SYN=TCP(dport=8000,flags='S',seq=100004)
   pkt1 = eth/ip/SYN/("AAAA"*20)
   sendp(pkt1, iface='eth2')

def pkt2():
   eth = Ether(dst='22:ff:ff:ff:ff:ff', src='01:02:03:04:05:06')
   ip = IP(src='10.0.0.12', dst='10.0.0.10')
   ACK = TCP(dport=8000,flags='A',seq=100004)
   pkt2 = eth/ip/ACK/("AAAA"*20)
   sendp(pkt2, iface='eth2')

def pkt3():
   eth = Ether(dst='33:ff:ff:ff:ff:ff', src='01:02:03:04:05:06')
   ip=IP(src='10.0.0.12', dst='10.0.0.10')
   PUSH_ACK=TCP(dport=8000,flags='PA',seq=100004)
   pkt3 = eth/ip/PUSH_ACK/Raw(load="GET /test HTTP/1.1\r\nHost: www.testtest.com\r\n\r\n")
   sendp(pkt3, iface='eth2')

def pkt4():
   pkt=IP(src='127.0.0.1', dst='88.88.88.88')/TCP(sport=88, dport=888)/Raw(load="GET /test HTTP/1.1\r\nHost: www.testtest.com\r\n\r\n")
   send(pkt)

def pkt5():
	pkt=Ether()/IP(src='10.0.0.12', dst='10.0.0.10')/UDP(sport=8192, dport=4096)
	sendp(pkt, iface='eth2')

if __name__ == "__main__":
	pkt1()
	pkt2()	
	#pkt3()
