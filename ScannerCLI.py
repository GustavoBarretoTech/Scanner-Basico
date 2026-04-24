import socket
# import threading

urlIP = input("Insira o IP ou URL: ").replace("https://" , "").replace("http://" , "")
print()
portas = [porta for porta in range(1 , 50)]

try:
    ip_real = socket.gethostbyname(urlIP)
except:
    print("IP ou URL invalido")
else:
    print(f"escaneando IP: {ip_real}")
    for porta in portas:
        
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.settimeout(1)
        
        varredor = sock.connect_ex((socket.gethostbyname(ip_real) , porta))
        if varredor == 0:
            print(f"Porta {porta} aberta")
        else:
            print(f"Porta {porta} fechada")  
finally:
    print("\nScan encerrado")