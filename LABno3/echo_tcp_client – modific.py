#klijent se spoji na server, posalje serveru podatke
#prihvati bilo kakve podatke koje primi natrag od servera 
#ispise podatke 

import socket
import datetime
from local_machine_info.py import print_machine_info

print datetime.datetime.now()

host= socket.gethostname()
port = 12345
client_socket=socket.socket()   #TCP socket

client_socket.connect((host,port))

poruka = raw_input("Unesite tekst : ")

client_socket.sendall(poruka)

data= client_socket.recv(1024)     #tekst primljen od servera


print data  #ispis podataka
client_socket.close()  #close the connection

