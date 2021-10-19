import socket
#client socket
from pickle import dumps,loads
x=socket.socket()
port,host=5000,'127.0.0.1'
x.connect((host,port))

ch='1'
data=None
connected=True

# while(ch!='#'):
#     data=input("enter the data please:")
#     x.sendall(dumps(data))

    
def wait_on_host():
    global x
    while(connected):
        data=x.recv(1024)
        data=loads(data)
        if data=='1':
            send_msg()

def send_msg():
    global x
    x.sendall(dumps("I am new"))

wait_on_host()