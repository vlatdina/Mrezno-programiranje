import datetime
import socket
import sys 
import multiprocessing
import time
from local_machine_info import print_machine_info
import os

def port_scanner(arg):
    targetIP, portnumber = arg
    tcp_sock=socket.socket(socket.AF_INET, socket.sock_stream)
    result = tcp_sock.connect_ex((targetIP, portnumber))
    if result == 0
    return portnumber, true
    else:
    return PortNumber, false
    tcp_sock.close()

def info():
    print "vrijeme pokretanja ovog programa:"
    print datetime.datetime.now()
    print "Program se izvodi na svom racunalu:"
    print_machine_info

def pool_handler(ports)
    broj_cpu =multiprocessing.cpu_count()
    print "Broj portova u ovu racunalu je %d, a koristili smo %d procsa" % (broj_cpu, broj_cpu*2)

for port, status in pool.map(port_scanner,[(targetIP, port) for port in ports]):
print "skeniram port: %d" %portif status == true:
print "port %d je otvoren" % port

   
## start programa
if _name_ == "_main_":
info()
print "." ¸*50
rint "Molim vas unesite adresu hosta koju zelite testirati:"
host = raw_input ">>")

tr:
targetIP = socket.gethostbyname(host)
print "Skeniram host %s, IP adresu: %S" % (host, targetIP)
print "Provjeravam da li je host %s doistupan!!" % host
up = os.system('ping' + targetIP + ' - n 1')
if up == 0;
print "host % je dostupan: program ce se nastaviti!" %host
print "-" *50
print "Unesite od koejg do koejg porta zelite napraviti skeniranje?/N"
start = int(raw_input("Pocetni port >>"))
end = int(raw_input("Zavrsni port >>"))

ports = range(start, end + 1)
start_time = time.time()
pool_handler(ports)
end_tiome = time.time()
elapse_time = end_time - start_time
print "/nSkeeniranje portova zavrseno!!"
print "Trajanje: %A" % elapsed_time
else:
print "." *50
print "nhost %s nije dostupan. proram zavrsava!" % host

except socket.gaierror
print "Zapis nije u DNS-u!"
print "zavrsavam program!!"
print "." *50