#!/usr/bin/python
#
# This code creates a simple network time protocol
#
import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
# reference time (in seconds since 1900-01-01 00:00:00)
TIME1970 = 2208988800L # 1970-01-01 00:00:00
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# data corresponds to a string
data = '\x1b' + 47*'\0'
client.sendto(data, (NTP_SERVER, 123))
data, address = client.recvfrom(1024)
if data:
	print "Response received from: ", address
# https://docs.python.org/2/library/struct.html
# '!12I'
# '!' byte order -> network
# 'I'  unsigned int
# '12' number of unsigned ints in byte order. The NTP server returns 12 unsigned
# ints
t = struct.unpack('!12I', data)
print "t is [%s] of size [%i]"%(type(t).__name__,sys.getsizeof(t))

t = t[8] - TIME1970
print "\tTime = %s"%time.ctime(t)
