from socket import *

serverName = 'localhost'
serverPort = 12000
# SOCK_STREAM represents a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# socket.getsockname returns address and port of this client
print clientSocket.getsockname()
sentence = raw_input('Input lowercase sentence: ')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From server: ', modifiedSentence
clientSocket.close()
