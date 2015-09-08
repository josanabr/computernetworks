#!/usr/bin/python
#
# En este script se presenta como a traves de la clase socket se puede obtener
# el nombre de la maquina donde se corre este programa
#
# Desde vim ejecute el comando ":!python basic-01.py"
#
import socket
host_name = socket.gethostname()
print "Host name [%s] and ip [%s]" % (host_name, socket.gethostbyname(host_name))
