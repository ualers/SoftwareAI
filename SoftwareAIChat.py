import threading
import subprocess
import os

def executar_automacao():
    # Definindo o diretório correto (onde está o )
    diretório_coreui = os.path.join(os.path.dirname(__file__), 'CoreUi', 'ChatSoftwareAI')
    os.chdir(diretório_coreui)  # Mudando para o diretório 

    comando_terminal = ['python', 'main.py']  # Executando main.py dentro do diretório 
    subprocess.Popen(comando_terminal, shell=True)

threading.Thread(target=executar_automacao).start()
