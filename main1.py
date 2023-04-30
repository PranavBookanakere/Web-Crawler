import socket

import re



list1 = []

def my_socket():



	a1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 Header and TCP Header

	a1.connect((socket.gethostbyname('www.google.com'),80))

	a2 = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'

	a2 = a2.encode()

	a1.send(a2)

	a3 = a1.recv(1024)

	#a3 = str(a3)

	print("Data indexed from the website: ",a3)

	print("\nThe length of the data: ",len(a3))

	print("\n")

	while (len(a3)>0):

		#r1 = re.findall('?:href=['"])([:/.A-z?<_&\s=>0-9;-]+',a3)

		#r1 = re.search(r'href=[\'"]?([^\'" >]+)', a3)

		#r1 = re.findall(b'(?:href=")(.*?)"',a3)

		#r1 = re.findall(b'@.*.com',a3)

		#code = '(?:href=")(.*?)"'

		

		code = 'https://\w*.\w*.\w*'

		#code = 'https://\w*.*'

		

		code = code.encode()

		r1 = re.findall(code, a3)

		#r1 = re.findall(rb'@gmail.com',a3)

		

		print("r1: ",r1)

		

		list1.append(r1)

		a3 = a1.recv(1024)

		if len(a3) == 0:

			break

			

		#print(a1.recv(1024))



	print("\nList of the required data:")

	print(list1)

	a1.close()



my_socket()

















