import socket
import threading
from pickle import dumps,loads

#server socket function

def recv_from_client():
    global con,Connected
    while(connected):
        data=con.recv(1024)
        print("recieved from client",loads(data))


x=socket.socket()
port,host=5000,'127.0.0.1'
x.bind((host,port))
x.listen(5)#waiting
con,addr=x.accept()
connected=True
#recv_from_client()
print("this is printed")

t=threading.Thread(target=recv_from_client)
t.start()
print("recieving started")









