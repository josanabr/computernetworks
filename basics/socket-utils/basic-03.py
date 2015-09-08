#!/usr/bin/python
#
# This program returns the name of a service given its port number
#
import socket

port = 25 # port identifier 
protocolname = "tcp" # protocol
print "Protocol %s, port %i => name [%s]"%(protocolname,port,socket.getservbyport(port, protocolname))
port = 53 # another por identifier
protocolname = "udp" # another transport protocol
print "Protocol %s, port %i => name [%s]"%(protocolname,port,socket.getservbyport(port, protocolname))
