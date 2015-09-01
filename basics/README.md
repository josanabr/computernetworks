# Basics directory
This directory contains various programs which were extracted from these books

- Computer Networks a Top-down approach
- Python Network Programming Cookbook

As follows is presented the following topics

- A UDP Client/Server program
- A TCP Client/Server program
- Another snippets of code

## A simple UDP client-server program

Client: ``UDPClient.py``

Server: ``UDPServer.py``

To run these programs open two terminals. In one terminal run ``python UDPServer.py``.
Go to the other terminal and run ``python UDPClient.py`` then follow the instructions.

## A simple TCP client-server program

Client: ``TCPClient.py``

Server: ``TCPServer.py``

To run these programs open two terminals. In one terminal run ``python TCPServer.py``.
Go to the other terminal and run ``python TCPClient.py`` then follow the instructions.

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

## Another programs exhibiting the use of `socket` class

The following programs show how to use the `socket` class in different scenarios. The following files are available:

- **basics-01.py** This program shows the basic use of the `socket` class in particular how to get the hostname of a server where this code is run
- **basics-02.py** This program shows how to get the IP of a server given its IP
- **basics-03.py** This program shows how to get the name of a network service given its protocol name and port number
- **basics-04.py** This program runs as an NTP client using the `ntplib` library. It is possible to the ntplib should be installed in your system, here is the command ``sudo pip install ntplib``
- **basics-05.py** This program runs as an NTP client with no third libraries. It is interesting because it shows how a real UDP protocol works

