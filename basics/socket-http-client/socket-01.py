#/usr/bin/python
import socket
import sys

# Se esta creando un socket que es del tipo IPv4 (socket.AF_INET) y es orientado
# a conexion (socket.SOCKET_STREAM a.k.a. TCP)
#
try: # esta estructura permite capturar comportamientos anomalos
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg: # si es del tipo socket.error
	print "Failed to create socket. Error code: " + str(msg[0]) + ", error message: " + msg[1] 
	sys.exit()

print "Socket created"
