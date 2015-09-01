#!/usr/bin/python
#
# This program returns an IP given a hostname 
#
import socket

host_name = "www.google.com"
print "IP address [%s] of [%s]"%(socket.gethostbyname(host_name),host_name)
