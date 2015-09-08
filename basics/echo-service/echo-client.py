#!/usr/bin/python
# -*- coding: latin-1 -*-
# 

import socket 
import sys
import argparse

host = 'localhost'

def echo_client(port): 
	# Cree un socket IPv4 y de tipo TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print "Connecting to %s port %s"%server_address
	# Conectese con el servidor
	s.connect(server_address)
	try:
		# El usuario digite la frase a enviar al servidor y lo guarda
		# en una variable llamada message
		message = "Mensaje de prueba. Este sera enviado"
		print "Sending %s"%message
		# Envie datos
		s.sendall(message)
		# Esperando por respuesta
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			# Reciba datos, no mas de 16 bytes
			data = s.recv(16)
			amount_received += len(data)
			print "Received: %s"%data
	except socket.errno, e:
		print "Socket error: %s"%str(e)
	except Exception, e:
		print "Other exception: %s"%str(e)
	finally:
		print "Closing connection to the server"
		s.close()
			

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Socket Server Example')
	parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)
