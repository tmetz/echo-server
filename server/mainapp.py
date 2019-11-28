# server main app
# Resources used:
# 1. https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
# 2. https://stackoverflow.com/questions/8710456/reading-a-binary-file-with-python/8711061

from server import Server

def main():
	s1 = Server("0.0.0.0", 5000)


if __name__ == "__main__":
	main()