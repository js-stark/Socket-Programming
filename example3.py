import socket

from pickle import dumps,loads

x=socket.socket()
host,port='127.0.0.1',5000
x.bind((host,port))
x.listen(10)
con,addr=x.accept()

data=con.recv(10000)
data=loads(data)

print("***our client has send data****",data,(con,addr))
x.close()





