import socket
import threading
from commands import Commands

class Server:
	
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.commands = Commands()
		self._listen(self.ip, self.port)
		self._accept_connections()

	def _listen(self, ip, port):
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind((ip, port))
			self.server.listen(5)
			print("Listening on %s:%d" % (ip, port))
		except Exception as e:
			print(e)

	def _process_client_requests(self, client):
		try:
			with client:
				while True:
					order = client.recv(1024)
					if not order: break
					command = (order.decode("utf-8")).split(':')
					print("Received %s" % command)

					''' Command Processing Section '''

					response = ""

					# if command[0] == "LIST_DEVICES":
					# 	response = self.commands.list_devices()
					# 	client.sendall(bytearray(response, "utf-8"))
					if command[0] == "GET_ENVIRONMENT":
						response = self.commands.get_environment()
						client.sendall(bytearray(response, "utf-8"))
					elif command[0] == "SCAN_DIR":
						response = self.commands.scan_dir(command[1], command[2])
						client.sendall(bytearray(response, "utf-8"))
					elif command[0] == "DOWNLOAD_FILE":
						#response = self.commands.download_file(command[1])
						#client.send(response)
						filename = command[1]
						#self.server.connect((self.ip, self.port))
						with open(filename, mode='rb') as f:
							file_content = f.read()
							client.send(file_content)
						#self.server.close()
						f.close()
						print("Done sending {}".format(filename))



		except Exception as e:
			print(e)

	def _accept_connections(self):
		try:
			with self.server:
				while True:
					print("Waiting for incoming client connection...")
					client, address = self.server.accept()
					print("Accepted connection from %s:%d" % (address[0], address[1]))
					client_handler = threading.Thread(target=self._process_client_requests, args=(client,))
					client_handler.start()
		except Exception as e:
			print(e)