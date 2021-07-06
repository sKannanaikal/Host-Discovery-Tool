from scapy.all import *
import optparse

def main():
	network_headers = '192.168.1'
	for host_header in range(256):
		host_ip = network_headers + "." + str(host_header)
		packet = IP(dst = host_ip, ttl=10)/ICMP()
		reply = sr1(packet, timeout=2)
		if not (reply is None):
			print('[+] Host: {hostname} is alive!'.format(hostname=host_ip))
	
if __name__ == '__main__':
	main()