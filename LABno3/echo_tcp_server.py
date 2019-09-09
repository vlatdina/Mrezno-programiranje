#echo_server program koristi socket i prihvaca dolazne konekcije
#primi podatke od klijenta
#vrati mu natrag te iste podatke ? 

import socket

host=socket.gethostname()
port=12345

echo_server=socket.socket()  #TCP socket  -novi socket
echo_server.bind((host,port))
echo_server.listen(5)


print "Cekam klijenta..."
conn, addr = echo_server.accept()

print "Spojen : " , addr

while True: 
    data = conn.recv(1024)      #Prihvacanje podataka od klijenta
    if not data: break           #ako nema podataka izadi
    conn.sendall(data)           #vrati primljene podatke klijentu
    
    conn.close()
    
    