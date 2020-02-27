#!/usr/bin/python
# Complete el codigo, en la seccion que dice COMPLETE de acuerdo al enunciado
# dado en este enlace https://goo.gl/1uQqiB, item 'socket-http-client'
# https://goo.gl/1uQqiB -> https://github.com/josanabr/computernetworks/tree/master/basics
#
import socket
import sys

try: # esta estructura permite capturar comportamientos anomalos
     # COMPLETE (1) 
except socket.error, msg: # si es del tipo socket.error
	print "Failed to create socket. Error code: " + str(msg[0]) + ", error message: " + msg[1] 
	sys.exit()

print "Socket created"

host = "www.google.com"
# defina una variable port y almacene alli el numero 80
# COMPLETE (2) 


try:
	# COMPLETE (3)
except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

# COMPLETE (4)

# COMPLETE (5)

# COMPLETE (6)

print "Socket connected to " + host + " on ip " + remote_ip

# Datos a enviarse
message = "GET / HTTP/1.1\r\n\r\n"

try:
	# COMPLETE (7)
except socket.error:
	print "Send failed"
	sys.exit()

print "Message send successfullly"

# Recibiendo datos
# COMPLETE (8)
print reply
s.close()
