from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "The server is ready to receive"
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print "Message received from %s port %s"%(clientAddress[0],clientAddress[1])
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)
