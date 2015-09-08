#/usr/bin/python
# Complete el codigo, busque "TU CODIGO AQUI"
import socket
import sys

# Se esta creando un socket que es del tipo IPv4 (socket.AF_INET) y es orientado
# a conexion (socket.SOCK_STREAM a.k.a. TCP)
#
try: # esta estructura permite capturar comportamientos anomalos
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg: # si es del tipo socket.error
	print "Failed to create socket. Error code: " + str(msg[0]) + ", error message: " + msg[1] 
	sys.exit()

print "Socket created"

host = "www.google.com"

try:
	# TU CODIGO AQUI
	# Encuentre el IP dado el nombre de servidor en la variable 'host'
	# y almacenelo en una variable llamada 'remote_ip'
	
except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

# TU CODIGO AQUI
# Imprima por pantalla un mensaje que diga
# La direccion IP de www.google.com es 216.58.192.100
# el numero IP puede variar y debe ser leido de la variable remote_ip
