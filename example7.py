import socket
import threading
import sys
from pickle import dumps,loads

#server socket
def recv_from_client():
    global con,Connected
    while(connected):
        data=con.recv(1024)
        print('Recieved from client',con.loads(data))

x=socket.socket()
port,host=5000,'127.0.0.1'
x.bind((host,port))
x.listen(5)
clients=[]
i=0
while i<2:
    con,addr=x.accept()
    clients.append((con,addr))
    print("client_connected",addr)
    i+=1

connected=True

i=0
while True:
    i+=1
    con,addr=clients[i%2]
    con.sendall(dumps('1'))
    data=con.recv(1024)
    data=loads(data)
    print("recieved from client",(i%2),data)

    if i==10:
        sys.exit()








