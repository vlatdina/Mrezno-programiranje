#klijent se spoji na server, posalje serveru podatke
#prihvati bilo kakve podatke koje primi natrag od servera 
#ispise podatke 

import socket

host= socket.gethostname()
port = 12345
client_socket=socket.socket()   #TCP socket

client_socket.connect((host,port))

client_socket.sendall('proizvoljan tekst saljemo serveru')

data= client_socket.recv(1024)     #tekst primljen od servera

print data  #ispis podataka
client_socket.close()  #close the connection

