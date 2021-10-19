import socket

target_host="www.google.com"
target_port=80

# create a socket object
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

#recieve some data
data,addr=client.recvfrom(4096)

print('*****output recievd ****:', data.decode())
client.close