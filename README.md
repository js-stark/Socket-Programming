# Socket-Programming
<h1>Socket Programming Essentials</h1>

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server. 
They are the real backbones behind web browsing. In simpler terms, there is a server and a client. 
Socket programming is started by importing the socket library and making a simple socket. 

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol. 
