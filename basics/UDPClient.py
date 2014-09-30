from socket import *

serverName = 'localhost'
serverPort = 12000
# AF_INET represents a socket by a pair (host, port). Internet
# SOCK_DGRAM represents a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print "Received message from %s port %s"%(serverAddress[0],serverAddress[1])
print modifiedMessage
clientSocket.close()
