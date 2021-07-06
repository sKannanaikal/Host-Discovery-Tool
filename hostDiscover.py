import socket
import sys

MESSAGE = b'Hello You There?'
DEFAULT_PORT = 9406

class hostScanner:

	def __init__(self, network_headers='192.168.1.0', network_type='C'):
		self.network_headers = network_headers
		self.network_type = network_type

	def analyzeANetwork(network_headers):
		for host_header1 in range(256):
			host_ip = network_headers + "." + host_header1 + "."
			for host_header2 in range(256):
				host_ip += host_header2 + "."
				for host_header3 in range(256):
					host_ip += host_header3
					scanHost(host_ip)
	
	def analyzeBNetwork(network_headers):
		for host_header1 in range(256):
			host_ip = network_headers + "." + host_header1 + "."
			for host_header2 in range(256):
				host_ip += host_header2
				scanHost(host_ip)
	
	def analyzeCNetwork(network_headers):
		for host_header in range(256):
			host_ip = network_headers + "." + host_header
			scanHost(host_ip)
		
	def scanHost(target_addr):
		try:
			probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			for _ in range(10):
				probe.sendto(MESSAGE, (target_addr, DEFAULT_PORT))
				data, addr = probe.recvfrom(1024)
				if data != None:
					print('[+] Host: {host} is Alive'.format(host=target_addr))
					break
				else:
					continue
		except socket.error:
			print('[-] Error occured in constructing UDP communication')

	def run():
		if self.network_type == 'A':
			analyzeANetwork(self.network_headers)
		elif self.network_type == 'B':
			analyzeBNetwork(self.network_headers)
		elif self.network_type == 'C':
			analyzeCNetwork(self.network_headers)
		else:
			print('[-] Incorrect Network Type passed try again!')
			sys.exit()

def main():
	command = optparse.OptionParser()
	command.add_option('-h', action='store', dest='network_headers', help='identify the network headers of the network')
	command.add_optioin('-t', action='store', dest='network_type', help='identify the network type (A, B, or C)')
	options, args = command.parse_args()
	network_headers = options.network_headers
	network_type = options.network_type
	scanner = hostScanner(network_headers, network_type)
	scanner.run()

if __name__ == '__main__':
	main()
