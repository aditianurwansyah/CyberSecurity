import socket 

def scan_port(host, port):
    try : 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        print(f"port {port} terbuka")
        s.close()
    except:
        pass  
host = input("Masukan host : ")
for port in range(1, 1028):
    scan_port(host, port) 