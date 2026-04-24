import customtkinter as ctk
import socket
import threading


ctk.set_appearance_mode("dark")  # Modo Dark
ctk.set_default_color_theme("blue")  # Temas Azul

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.title("Minha Interface CTK")
        self.geometry("900x840")

        # Criando a Entry (campo de entrada)
        self.entry = ctk.CTkEntry(self, placeholder_text="Digite o IP aqui...", width=300)
        
        # Posicionando no topo
        self.entry.pack(pady=(20, 0), padx=20)

        # Botao de confirmar
        self.button = ctk.CTkButton(self, text="Confirmar", command=self.botao_clicado)
        self.button.pack(pady=20)
        
    def pegarIP(self):
        try:
            sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8" , 80))
            ip = sock.getsockname()[0]
            sock.close()
            return ip
        except Exception:
            return "falha ao obter IP"
        
    def scannerPortas(self):
        # portas = [porta for porta in range(1 , 101)]
        portas = [22,443,21,53,445,80,8080]
        
        for porta in portas:
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            sock.settimeout(0.1)
            
            try:
                ip_real = socket.gethostbyname(self.entry.get().replace("https://","").replace("http://",""))
            except:
                print("Url inválida")
            else:
                varredor = sock.connect_ex((ip_real , porta))
                if varredor == 0:
                    print(f"Porta {porta} aberta")
                else:
                    print(f"porta {porta} fechada")
                    sock.close()

    def botao_clicado(self):
        threading.Thread(target= self.scannerPortas , daemon=True).start()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
