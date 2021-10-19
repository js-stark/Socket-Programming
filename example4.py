import socket

from pickle import loads,dumps

x=socket.socket()
host,port='127.0.0.1',5000
x.connect((host,port))
data= dumps('hello i am doing geat bro')
x.sendall(data)





