import socket
target_host="www.google.com"
target_port=80
#CREATE A SOCKET OBJECT
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# CONNECT THE CLIENT
client.connect((target_host,target_port))
#SEND IN SOME BYTES
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#RECIEVE SOME DATA
response=client.recv(4096)

#PRINT OUT THE RESPONS
print("the response obtaines is: ",response.decode())
client.close()