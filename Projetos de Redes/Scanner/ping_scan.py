import subprocess

ip_metasploitable = "192.168.56.101"

try:
    ping = subprocess.run(["ping" , "-c", "1", ip_metasploitable],
                          capture_output=True,
                          text=True)
    
    if "1 received" in ping.stdout:
        print(f"----- ALVO VIVO! Iniciando varredura de portas -----\n")
        
        # -F para ser rápido, -sV para pegar as versões
        nmap = subprocess.run(f"nmap -F -sV {ip_metasploitable}",
                              shell=True,
                              capture_output=True,
                              text=True)
        
        print(nmap.stdout)
    else:
        print("Alvo não respondeu ao ping.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
finally:
    print("\nProcesso Finalizado!")
