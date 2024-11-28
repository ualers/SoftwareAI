
import sys
import os


import struct
import re
import platform
import json
import ast
from firebase_admin import credentials, initialize_app, storage, db, delete_app



# Caminho absoluto para o diretório onde SoftwareAI está localizado (raiz do projeto)
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI'))
sys.path.append(caminho_raiz)

from CoreApp._init_core_ import AutenticateAgent,Agent_files,  ResponseAgent, python_functions 




from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class AI_thread(QThread):
    chat_and_thoughts = Signal(str)
    new_message = Signal(str)

    def __init__(self, message, 
                Instruction, Key,
                Nameassistant, Modelselect,
                Aditionalinstructions, tools,
                Vectorstoreinassistant, VectorstoreinThread,
                Upload1fileinthread, Upload1fileinmessage,
                Upload1imageforvisioninthread
                 
                ):
        super().__init__()
        
        self.message = message

        self.Instruction = Instruction
        self.Key = Key
        self.Nameassistant = Nameassistant
        self.Modelselect = Modelselect
        self.Aditionalinstructions = Aditionalinstructions
        self.tools = tools
        self.Vectorstoreinassistant = Vectorstoreinassistant
        self.VectorstoreinThread = VectorstoreinThread
        self.Upload1fileinthread = Upload1fileinthread
        self.Upload1fileinmessage = Upload1fileinmessage
        self.Upload1imageforvisioninthread = Upload1imageforvisioninthread


        self.running = True
        # Conectar o sinal de nova mensagem ao método que atualiza a mensagem
        self.new_message.connect(self.update_message)

    def run(self):

        instruction = self.Instruction
        key = self.Key
        nameassistant = self.Nameassistant
        model_select = self.Modelselect
        adxitional_instructions = self.Aditionalinstructions
        Upload_1_file_in_thread = self.Upload1fileinthread
        Upload_1_file_in_message = self.Upload1fileinmessage
        Upload_1_image_for_vision_in_thread = self.Upload1imageforvisioninthread
        Upload_list_for_code_interpreter_in_thread = None
        UploadinGoogleDocs = None
        vectorstore_in_Thread = self.VectorstoreinThread
        vectorstore_in_Agent = self.Vectorstoreinassistant
        tools = self.tools

        AI = AutenticateAgent.create_or_auth_AI(
            key, instruction, 
            nameassistant, model_select,
            tools, vectorstore_in_Agent
        )


        while self.running:
            if self.message:
     
                
                self.emit_message("user", self.message)

                mensaxgem = f"""{self.message} \n       
                
                """  
                exemplo = "sempre inclua nas repostas \n para facilitar a legibilidade"

                mensaxgemfinal = mensaxgem + exemplo

                
                response = ResponseAgent.ResponseAgent_message_with_assistants(
                                                                        mensaxgemfinal,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread,
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools,  AI, model_select,
                                                                        adxitional_instructions, key
                                                                        )
                
                
                #self.chat_and_thoughts.emit(f"MatrixAI: {response}  ")  

                self.emit_message("matrix", response)
                
                
                # Limpa a mensagem para esperar uma nova
                self.message = None

    def format_message(self, message):
        # Regex para detectar blocos de código em Python, incluindo comentários e strings
        code_pattern = r'```python(.*?)```'

        # Adiciona <br> após cada linha de código encontrada e envolve em <pre><code>
        formatted_message = re.sub(
            code_pattern,
            lambda m: (
                '<pre><code style="background-color: #2E2E2E; color: #FFFFFF; padding: 8px; border-radius: 5px; border: 1px solid #444;">'
                + m.group(1).replace("\n", "<br>") + '</code></pre>'
            ),
            message,
            flags=re.DOTALL  # Para permitir a captura de múltiplas linhas
        )
        
        # Substitui quebras de linha por <br> para parágrafos normais
        formatted_message = formatted_message.replace("\n", "<br>")
        
        return formatted_message

    def emit_message(self, sender, message):
        """Emite a mensagem formatada com base no remetente, incluindo quebras de linha e formatação de código."""
        # Formata a mensagem com código
        formatted_message = self.format_message(message)

        if sender == "user":
            formatted_message = (
                f'<div style="display: flex; justify-content: flex-end;">'
                f'<div style="background-color: #d4f4dd; color: black; padding: 8px; border-radius: 8px; '
                f'margin: 5px; max-width: 70%;"><b>user:</b> {formatted_message}</div>'
                f'</div>'
            )
        elif sender == "matrix":
            formatted_message = (
                f'<div style="display: flex; justify-content: flex-start;">'
                f'<div style="color: black; padding: 8px; border-radius: 8px; '
                f'margin: 5px; max-width: 70%;"><b>MatrixAI:</b> {formatted_message}</div>'
                f'</div>'
            )

        self.chat_and_thoughts.emit(formatted_message)
    def update_message(self, message):
        """Atualiza a mensagem da thread sem reiniciá-la."""
        self.message = message

    def stop(self):
        """Encerra a thread."""
        self.running = False
        
