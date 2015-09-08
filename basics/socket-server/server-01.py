#/usr/bin/python
# Para reusar puertos de red 
# Despues de crear un socket, socket.socket(...)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
import socket
import sys

HOST = '' # Este servidor escuchara por todas las interfaces de red
PORT = 8888 # Un identificador de puerto cualquiera

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
	s.bind((HOST, PORT)) # Esta funcion asocia un socket a un IP y un port
except socket.error, msg:
	print 'Bind failed. Error code: ' + str(msg[0]) + ' message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

