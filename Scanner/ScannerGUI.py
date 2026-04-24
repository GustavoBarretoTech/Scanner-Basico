import customtkinter as ctk
import socket
import threading

# Configuração do tema (opcional)
ctk.set_appearance_mode("dark")  # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (padrão), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.title("Minha Interface CTK")
        self.geometry("900x840")

        # Criando a Entry (campo de entrada)
        # O placeholder_text é o texto que aparece quando o campo está vazio
        self.entry = ctk.CTkEntry(self, placeholder_text="Digite o IP aqui...", width=300)
        
        # Posicionando no topo
        # O 'pady' adiciona um espaçamento vertical no topo e embaixo
        self.entry.pack(pady=(20, 0), padx=20)

        # Exemplo de botão apenas para compor a tela
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
            
            #checar se o valor é um ip
            # try:
            #     float(self.entry.get())
            # except: #caso nao seja ip, reescreve a url pra seu respectivo ip 
            #     self.entry.delete(0 , 'end')
            #     self.entry.insert(0 , sock.getsockname()[0])
            # finally:
            #     varredor = sock.connect_ex((self.entry.get() , porta))
            #     if varredor == 0:
            #         print(f"Porta {porta} aberta")
            #     else:
            #         print(f"porta {porta} fechada")
            #     sock.close()
            
            #==========================================================
            
            # varredor = sock.connect_ex((self.entry.get() , porta))
            # if varredor == 0:
            #     print(f"Porta {porta} aberta")
            # else:
            #     print(f"porta {porta} fechada")
            #     sock.close()
            
            #============Jeito certo================
            #============Concertar o erro em loop tambem=====================
            
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
        # print(f"Texto digitado: {self.entry.get()}")
        # print(f"seu IP: {self.pegarIP()}")
        threading.Thread(target= self.scannerPortas , daemon=True).start()
        

if __name__ == "__main__":
    app = App()
    app.mainloop() # Inicia o loop da interface
