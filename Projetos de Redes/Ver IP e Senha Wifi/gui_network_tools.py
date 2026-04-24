import subprocess
import platform
import re
import customtkinter as ctk
from tkinter import scrolledtext
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class NetworkTools:
    def __init__(self):
        self.os = platform.system().lower()
    
    def _run_command(self, cmd):
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=10)
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            return None, f"Erro: {e.returncode}. Stderr: {e.stderr}"
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return None, f"Comando não encontrado ou timeout."
    
    def get_wifi_password(self):
        if self.os == 'linux':
            stdout, stderr = self._run_command(['nmcli', 'device', 'wifi', 'show-password'])
            return stderr or stdout or "Sem conexão WiFi."
        elif self.os == 'windows':
            stdout, _ = self._run_command(['netsh', 'wlan', 'show', 'profiles'])
            if not stdout: return "Sem perfis WiFi."
            profiles = re.findall(r'All User Profile\s*:\s*(.+)', stdout)
            output = "Perfis WiFi:\n"
            for profile in profiles:
                profile = profile.strip()
                pass_out, _ = self._run_command(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
                key = re.search(r'Key Content\s*:\s*(.+)', pass_out or '')
                pw = key.group(1) if key else '***'
                output += f"- {profile}: {pw}\n"
            return output
        return f"SO: {self.os}"
    
    def get_ip_address(self):
        if self.os == 'linux':
            stdout, stderr = self._run_command(['ip', 'addr', 'show'])
            ips = re.findall(r'inet (\d+\.\d+\.\d+\.\d+)/', stdout or '')
            return "IPs:\n" + "\n".join(ips) if ips else stderr or "Sem IP."
        elif self.os == 'windows':
            stdout, stderr = self._run_command(['ipconfig'])
            ips = re.findall(r'IPv4 Address\. .*: (\d+\.\d+\.\d+\.\d+)', stdout or '')
            return "IPs:\n" + "\n".join(ips) if ips else stderr or "Sem IP."
        return f"SO: {self.os}"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Network Tools - CustomTkinter")
        self.geometry("700x600")
        self.tools = NetworkTools()
        
        # Title
        self.title_label = ctk.CTkLabel(self, text="🛜 Ferramentas de Rede", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=20)
        
        # Buttons
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.pack(pady=10, padx=20, fill="x")
        
        self.wifi_btn = ctk.CTkButton(self.btn_frame, text="🔑 Senha WiFi", command=self.wifi_click, width=150, height=50, fg_color="green")
        self.wifi_btn.pack(side="left", padx=10, pady=10)
        
        self.ip_btn = ctk.CTkButton(self.btn_frame, text="🌐 Meu IP", command=self.ip_click, width=150, height=50, fg_color="blue")
        self.ip_btn.pack(side="left", padx=10, pady=10)
        
        self.clear_btn = ctk.CTkButton(self.btn_frame, text="🗑️ Limpar", command=self.clear, width=150, height=50, fg_color="orange")
        self.clear_btn.pack(side="right", padx=10, pady=10)
        
        # Output
        self.output = scrolledtext.ScrolledText(self, height=25, font=("Consolas", 11), bg="#2b2b2b", fg="white", insertbackground="white")
        self.output.pack(pady=20, padx=20, fill="both", expand=True)
    
    def log(self, msg):
        self.output.insert("end", msg + "\n\n")
        self.output.see("end")
    
    def clear(self):
        self.output.delete(1.0, "end")
    
    def wifi_click(self):
        self.log("🔍 Buscando senha WiFi...")
        threading.Thread(target=self._run_wifi, daemon=True).start()
    
    def _run_wifi(self):
        result = self.tools.get_wifi_password()
        self.after(0, lambda: self.log(result))
    
    def ip_click(self):
        self.log("🔍 Buscando IPs...")
        threading.Thread(target=self._run_ip, daemon=True).start()
    
    def _run_ip(self):
        result = self.tools.get_ip_address()
        self.after(0, lambda: self.log(result))

if __name__ == "__main__":
    app = App()
    app.mainloop()

