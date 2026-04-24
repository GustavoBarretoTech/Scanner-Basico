import subprocess
import platform
# import re


def menu():
    os = platform.system()
    
    opcoes = input("""
                [1] Ver senha da sua rede
                [2] Ver seu IP
                """)
    if opcoes == "1":
        if os == "Linux":
            res = subprocess.run(['nmcli','device','wifi','show-password'],
                                capture_output=True, 
                                text=True
                                )
            print(res.stdout)
        elif os == "Windows":
            res = subprocess.run(['netsh','wlan','show','profiles'],
                                capture_output=True, 
                                text=True
                                )
            print(res.stdout)
    elif opcoes == '2':
        if os == "Linux":
            res = subprocess.run(['ip' , 'a'],
                           capture_output=True,
                           text=True,
                           )
            print(res.stdout)
        elif os == "Windows":
            res = subprocess.run(['ipconfig'],
                           capture_output=True,
                           text=True,
                           )
            print(res.stdout)
menu()
