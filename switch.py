
class KangTaiSwitch:
	def __init__(self, ipaddr):
		import socket
		self.ipaddr = ipaddr
		self.port = 28536
		self.message_size = 34
		self.preamble = b'\x02\x02\x00\x01\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\x00\x10'
		self.state_command = self.preamble + b'\x29\x5a\x7d\x99\x7a\x4d\x1a\xb5\x7b\x25\x4f\xf9\x0e\x3b\xcb\x33'
		self.on_command = self.preamble + b'\xb5\xcb\x50\x7e\x1d\x53\x50\xf4\xd2\xa0\x8c\x9d\xfc\xd1\x3f\x64'
		self.off_command = self.preamble + b'\x91\x1f\x6d\xaf\xb9\xc5\x6b\x81\x55\x37\x75\x30\x29\xd6\x90\x99'
		self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conn.connect((self.ipaddr, self.port))

	def switch_on(self):
		self.conn.sendall(self.on_command)
	def switch_off(self):
		self.conn.sendall(self.off_command)
	def query(self):
		self.conn.sendall(self.state_command)
		self.retval = self.conn.recv(self.message_size)
		
		if self.retval.endswith(b'\x01'):
			return('OFF')
		elif self.retval.endswith(b'\xb6'):
			return('ON')
		else:

			return(self.retval)
