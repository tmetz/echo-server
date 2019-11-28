from client import Client
import time

def show_menu(c1):
	menu_selection = 0
	while (menu_selection != 4):
		print("Welcome To Echo Server (Project 4)")
		print("Please make a selection:")
		print("\n")
		print("1. Scan attached disk for files based on search criteria")
		print("2. Request and download file based on name")
		print("3. Query server's host for OS and supported Python version")
		print("4. Exit")
		menu_selection = int(input("What is your selection?"))
		if menu_selection == 1:
			search_term = input("What is your search term?  Enter ALL for full directory listing ")
			c1.send("SCAN_DIR:.:{}".format(search_term))
		elif menu_selection == 2:
			filename = input("What file do you want to download?")
			message_string = "DOWNLOAD_FILE:%s" % (filename)
			c1.client.send(bytearray(message_string, 'utf-8'))
			with open(filename, 'wb') as f:
				while True:
					data = c1.client.recv(1024)
					f.write(data)
			f.close()
		elif menu_selection == 3:
			c1.send("GET_ENVIRONMENT")
		elif menu_selection == 4:
			print ("Exiting")
		else:
			print("Sorry, that command is not recognized.")

def main():
	c1 = Client("127.0.0.1", 5000)
	show_menu(c1)
	#c1.send("LIST_DEVICES")
	c1.close()


if __name__ == "__main__":
	main()