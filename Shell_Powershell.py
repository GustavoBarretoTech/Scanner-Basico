import platform
import subprocess
# from pprint import pprint

sistema = platform.system()

if sistema == "Linux":
    print("Executando comando Shell no Linux...")
    # O 'shell=True' permite que você escreva o comando como uma frase comum
    subprocess.run("nmcli device wifi show-password", shell=True) 

elif sistema == "Windows":
    print("Executando comando PowerShell no Windows...")
    # No Windows, você precisa chamar o powershell.exe e passar o comando
    comando_ps = "Get-Process | select -first 10"
    subprocess.run(["powershell", "-Command", comando_ps], shell=True)

else:
    print(f"Sistema {sistema} não mapeado.")
