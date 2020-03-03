import socket, optparse

parser = optparse.OptionParser()
parser.add_option('-i', dest='ip', default='10.0.0.2')
parser.add_option('-p', dest='port', type='int', default=12345)
(options, args) = parser.parse_args()

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.sendto(options.msg.encode(), (options.ip, options.port))

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

'''
ethernet  = b'\x36\x00\x4d\xd6\x76\x4d' # h1 c6:90:f7:ae:a7:8f 
ethernet += b'\x92\x74\x27\xd0\x7b\x55' # h2 ee:1b:f0:f9:c6:6d
ethernet += b'\x08\x00'
'''

ip_header  = b'\x45\x00\x00\x28'  # Version, IHL | DSCP, ECN | Type of Service | Total Length
ip_header += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
ip_header += b'\x40\x06\xbb\x00'  # TTL, Protocol | Header Checksum
ip_header += b'\x0a\x00\x00\x01'  # Source Address
ip_header += b'\x0a\x00\x00\x02'  # Destination Address

tcp_header  = b'\x30\x39\x30\x3a' # Source port | Destination port
tcp_header += b'\x00\x01\x00\x00' # Sequence Number
tcp_header += b'\x00\x00\x00\x00' # Acknowledgement Number
tcp_header += b'\x50\x02\x71\x10' # Data offset, Reserved, NS | ..., SYN, FIN | Window Size
tcp_header += b'\xca\x5b\x00\x00' # Checksum | Urgent pointer

packet_to_send = ip_header + tcp_header
s.sendto(packet_to_send, (options.ip, options.port))


ip_header2  = b'\x45\x00\x00\x28'  # Version, IHL | DSCP, ECN | Type of Service | Total Length
ip_header2 += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
ip_header2 += b'\x40\x06\xbb\x00'  # TTL, Protocol | Header Checksum
ip_header2 += b'\x0a\x00\x00\x01'  # Source Address
ip_header2 += b'\x0a\x00\x00\x02'  # Destination Address

tcp_header2  = b'\x30\x39\x30\x3a' # Source port | Destination port
tcp_header2 += b'\x00\x00\x00\x00' # Sequence Number
tcp_header2 += b'\x00\x00\x00\x01' # Acknowledgement Number
tcp_header2 += b'\x50\x02\x70\x10' # Data offset, Reserved, NS | ..., SYN, FIN | Window Size
tcp_header2 += b'\xca\x5b\x00\x00' # Checksum | Urgent pointer

packet_to_send2 = ip_header2 + tcp_header2
s.sendto(packet_to_send2, (options.ip, options.port))
