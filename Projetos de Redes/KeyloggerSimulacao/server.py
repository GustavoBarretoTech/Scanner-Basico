import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

sock.bind(("localhost" , 12345))

sock.listen(1)
print("esperando conexão")

conn , addr = sock.accept()
print(f"ip conectado: {addr}")

#receber dados

while True:
    dados = conn.recv(1024)
    print(dados.decode())