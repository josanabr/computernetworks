#!/usr/bin/python
#
# This python program shows how to get the hostname and IP of the host in which
# this program is running
#
import socket
host_name = socket.gethostname()
print "Host name [%s] and ip [%s]" % (host_name, socket.gethostbyname(host_name))
