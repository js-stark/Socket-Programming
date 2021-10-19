import socket
from pickle import dumps,loads
#client socket

x=socket.socket()
port,host=5000,'127.0.0.1'
x.connect((host,port))
#data=dumps([x for x in "Jayasoruban"])

#x.sendall(data)

ch='1'
while(ch!='#'):
    print('enter data to send')
    data=input("enter the data")
    x.sendall(dumps(data))
