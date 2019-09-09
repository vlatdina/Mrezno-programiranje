#echo_server program koristi socket i prihvaca dolazne konekcije
#primi podatke od klijenta
#vrati mu natrag te iste podatke ? 

import socket
import datetime
from local_machine_info.py import print_machine_info
print datetime.datetime.now()


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
    
    #ukoliko korisnik unese string 'aspira' server vraca klijentu obavjest da uno nije podrzan??   nemaam pojmaa
    #server cijelo vrijeme slusa dolazne konekcije, a ne da izade nakon sto primi konekciju i zatvori konekciju 