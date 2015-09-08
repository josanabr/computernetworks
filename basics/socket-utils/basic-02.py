#!/usr/bin/python
#
# Este programa muestra como a traves de la clase socket se puede obtener el
# IP de una maquina dado su nombre
#
import socket

host_name = "www.google.com"
print "IP address [%s] of [%s]"%(socket.gethostbyname(host_name),host_name)
