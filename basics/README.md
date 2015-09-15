# Basics directory
This directory contains various programs which were extracted from these books

- Computer Networks a Top-down approach
- Python Network Programming Cookbook

As follows is presented the following topics

- A UDP Client/Server program
- A TCP Client/Server program
- Socket utils
- NTP client
- Socket HTTP client
- Socket server
- Echo service

## A simple UDP client-server program

Client: ``UDPClient.py``

Server: ``UDPServer.py``

To run these programs open two terminals. In one terminal run ``python UDPServer.py``.
Go to the other terminal and run ``python UDPClient.py`` then follow the instructions.

### What should learn from here - UDPClient.py
- How to create a socket used to send datagrams
- How read data coming from server
- How to read data from terminal

Resuelva el siguiente [formulario](http://goo.gl/forms/0Pf72fveHq).

### What should learn from here - UDPServer.py
- What is the meaning of `bind` function.
- What is the method used to send data

Resuelva el siguiente [formulario](http://goo.gl/forms/DOHllYi7FB).

## A simple TCP client-server program

Client: ``TCPClient.py``

Server: ``TCPServer.py``

To run these programs open two terminals. In one terminal run ``python TCPServer.py``.
Go to the other terminal and run ``python TCPClient.py`` then follow the instructions.

### What should learn from here - TCPClient.py
- How to create a TCP-based socket
- What parameters recive the `connect()` method
- How to read data from a TCP socket
- How to write data through a TCP socket

Resuelva el siguiente [formulario](http://goo.gl/forms/lN4V38wp8f).

### What should learn from here - TCPServer.py
- How to create a TCP-based socket
- What the listen()'s parameter means
- How to get the identity of a client

Resuelva el siguiente [formulario](http://goo.gl/forms/6RLs4Vqpkh).

## Questions about UDP\* and TCP\* programs?

- What happen if the UDPClient.py is run before UDPServer.py?
- What happen if you run the UDPClient.py program, type a sentence and hit ``ENTER``
- What happen if the TCPClient.py is run before TCPServer.py?
- What happen if TCPServer.py is run then UDPClient.py? 
- What happen if UDPServer.py is run then TCPClient.py?
- What happen if you run two instances of TCPServer.py simultaneously? 
- What happen if you run two instances of UDPServer.py simultaneously? 
- Can you run TCPServer.py and UDPServer.py simultaneously?
- Do you remember this sentence ``serverSocket.bind(('',serverPort))``? What is the meaning of ``''``? 

## Socket utils

The following programs are located at *socket-utils* directory. There you can find some programas to show how to use the `socket` class in different scenarios. The following files are available:

- **basics-01.py** This program shows the basic use of the `socket` class in particular how to get the hostname of a server where this code is run
- **basics-02.py** This program shows how to get the IP of a server given its name
- **basics-03.py** This program shows how to get the name of a network service given its protocol name and port number

## NTP Client
The following programs are located at *ntp-client* directory. There you can find some programas to show how to use the `socket` class in different scenarios. The following files are available:

- **basics-04.py** This program runs as an NTP client using the `ntplib` library. It is possible to the ntplib should be installed in your system, here is the command ``sudo pip install ntplib``
- **basics-05.py** This program runs as an NTP client with no third libraries. It is interesting because it shows how a real UDP protocol works

## HTTP Client
In *socket-http-client* directory you will find five python programs (from python-01.py to python-05.py) to show how you can interact with a real HTTP server like www.google.com.
- **socket-01.py** shows how to create an Internet TCP socket 
- **socket-02.py** needs some help from you. Read the code and complete it
- **socket-03.py** this time the `socket.connect` is used to connect with the www.google.com server
- **socket-04.py** this time the program shows how you can send a HTTP request to the HTTP server
- **socket-05.py** shows how to receive the responde from a HTTP server

It is pretty important that you understand how the different functions allow to interact with a remote server

## Socket server
The previous codes shown how to interact from a client perspective. This time you will learn how to create a server. You can interact with this server using the
`telnet` command. 
All the programs are in the `socket-server` directory and you can access the server running the command `telnet localhost 8888`.

- **server-01.py** shows the `socket.bind()` which is a method to bind a socket with a given host and port.
- **server-02.py** this time the `socket.listen()` and `socket.accept()` are exposed. 
- **server-03.py** this code shows how a server receives a connection then how it replies to the client
- **server-04.py** this time an infinite loop is created in order to run the server forever.
- **server-05.py** this time you need to complete the code in order to create a multithreaded server which accepts connections from several clients and it is able to attend them simultaneously.

## Echo Service
The `echo-service` directory has only two files. At this time you are very familiarized with network communication primitives and it is required to fill the code gaps in order to create a functional echo server and echo client programs.
