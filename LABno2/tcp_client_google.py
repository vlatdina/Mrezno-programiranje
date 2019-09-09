
#tcp client.py 

import socket 

client_socket=socket.socket()
host=socket.gethostbyname(www.google.com)
print "IP for hostname www.google.com is %s " , host

port =80

client_socket.connect((host,port))       ##ovo je prikljucnica 
print client_socket.recv(1024)


print "The client has succsesfully connected to www.google.com on port %d", port

client_socket.close()