#!/usr/bin/python
#
# This program returns the name of a service given its port number
#
import socket

port = 25
protocolname = "tcp"
print "Protocol %s, port %i => name [%s]"%(protocolname,port,socket.getservbyport(port, protocolname))
port = 53
protocolname = "udp"
print "Protocol %s, port %i => name [%s]"%(protocolname,port,socket.getservbyport(port, protocolname))
