import socket
import sys

MESSAGE = b'Hello You There?'

class scanner:

	def __init__(self, target_addr='255.255.255.255'):
		self.target = target_addr

	def scan():
		probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		probe.sendto(MESSAGE, ())

	def results():
		pass

	def run():
		scan()
		results()

def main():
	print('hello world')

if __name__ == '__main__':
	main()
