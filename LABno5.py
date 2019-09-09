import socket
import datetime
from local_machine_info import print_machine_info        #ona funkcija koju smo tamo napravili

datum=datetime.datetime.now() 
print(datum)
print_machine_info()

host=raw_input("Unesi adresu hosta kojeg zelis provjeriti: ")
host_ip=socket.gethostbyname(host)
print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje ")
start= raw_input("Pocetni port : ")
end= raw_input("Zavrsni port :" )
def check_ping(hostname):
    response=os.system("ping  -c 1" +hostname)
    #sad provjeravamo odgovor
    if response ==0:
        pingstatus="Ping OK"
    else:
        pingstatus="Ping failed"
    return pingstatus
    
    
def scanPort(int, Port):
    print("Skeniram port %d") % (port)
    
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #svojstva definirana
    
    result=s.connect_ex((host,port))
    if result==0:
        print "Port is open"
    else:
        print "Port is not open"
    s.close()