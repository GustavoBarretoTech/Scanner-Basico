import platform
import subprocess
# from pprint import pprint

sistema = platform.system()

if sistema == "Linux":
    print("Executando comando Shell no Linux...")
    #disparando o Shell script
    subprocess.run("nmcli device wifi show-password", shell=True) 

elif sistema == "Windows":
    print("Executando comando PowerShell no Windows...")
    # disparando o Powershell
    comando_ps = "Get-Process | select -first 10"
    subprocess.run(["powershell", "-Command", comando_ps], shell=True)

else:
    print(f"Sistema {sistema} não mapeado.")
