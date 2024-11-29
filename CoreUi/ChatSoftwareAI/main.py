########################################################################
## IMPORTS Libs
import sys
import os
import subprocess
from typing import Dict, Any
import time
import psutil
import GPUtil
import math
import json
import ast

from typing import Dict, Any
import os
import subprocess
import platform
from firebase_admin import credentials, initialize_app, storage, db, delete_app
import concurrent.futures
########################################################################


# Caminho absoluto para o diretório onde SoftwareAI está localizado (raiz do projeto)
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI'))
sys.path.append(caminho_raiz)

########################################################################
# IMPORT CoreApp
from CoreUi.ChatSoftwareAI.Chat.AIQthread import AI_thread
########################################################################


########################################################################
# IMPORT FirebaseKeys
try:
    from CoreApp.KeysFirebase.keys import keys_app_2
except ModuleNotFoundError as e:
    print(f"Erro ao importar: {e}")
app2 = keys_app_2()
########################################################################

########################################################################
# IMPORT .qrc
from src_ import icons_interpreter
########################################################################

########################################################################
# IMPORT GUI 
from src_.ui_cliente_and_chat import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomModals import QCustomModals
########################################################################

########################################################################
# IMPORT Pyside2
from PySide2extn.RoundProgressBar import roundProgressBar #IMPORT THE EXTENSION LIBRARY
from PySide2.QtCore import QTimer, Signal, QThread

########################################################################


########################################################################
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    message_signal = Signal(str)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style.json"}
                      )
        ########################################################################



        VoiceEnginetts1 = self.ui.checkBox



        Menu = self.ui.pushButton_16
        Menu.setObjectCustomTheme("#FFFAFA", "#7FFFD4")
        Menu.setObjectAnimateOn("hover")

        Settings = self.ui.settings_agent
        Settings.setObjectCustomTheme("#FFFAFA", "#B0E0E6")
        Settings.setObjectAnimateOn("hover") 
        #Settings.clicked.connect(self.save_config)

        View_threads = self.ui.view_threads
        View_threads.setObjectCustomTheme("#FFFAFA", "#B0E0E6")
        View_threads.setObjectAnimateOn("hover")

        Upload_file = self.ui.atach_file
        Upload_file.setObjectCustomTheme("#FFFAFA", "#F0F8FF")
        Upload_file.setObjectAnimateOn("hover")
        #Upload_file.clicked.connect(self.open_file_dialog)

        Send_mensage = self.ui.send_mensage
        Send_mensage.setObjectCustomTheme("#FFFAFA", "#F0F8FF")
        Send_mensage.setObjectAnimateOn("hover")
        Send_mensage.clicked.connect(self.send_message)


        self.Instruction = self.ui.instruct_agent
        self.Key = self.ui.key_firebase_agent
        self.Nameassistant = self.ui.name_agent
        self.Modelselect = self.ui.model_agent
        self.Aditionalinstructions = self.ui.addition_instruct
        self.tools = self.ui.tools_agent
        self.Vectorstoreinassistant = self.ui.vectorstore_in_agent
        self.VectorstoreinThread = self.ui.vectorstore_in_thread
        self.Upload1fileinthread = self.ui.Upload_1file_in_thread
        self.Upload1fileinmessage = self.ui.Upload_1file_in_message
        self.Upload1imageforvisioninthread = self.ui.Upload_1image_for_vision_in_thread




        self.chat_area = self.ui.html_chat
        if not isinstance(self.chat_area, QTextEdit):
            print("Erro: html_chat não é um QTextEdit")

        # Conectando o sinal ao método de exibição
        self.message_signal.connect(self.display_user_message)  

        # Emite uma mensagem de teste para verificar se está funcionando
                
        #self.message_signal.emit("Mensagem de teste")

        self.chat_area.setReadOnly(True)

        self.message_input = self.ui.mensage_input
        self.message_input.textChanged.connect(lambda: self.adjust_height(increase=True))
 
        #self.message_input.returnPressed.connect(self.send_message)
        #self.message_input.keyPressEvent = self.handle_key_press

        self.load_config()
    

        
        Instruction = self.Instruction.toPlainText()
        Key = self.Key.text()
        Nameassistant = self.Nameassistant.text()
        Modelselect = self.Modelselect.text()
        Aditionalinstructions = self.Aditionalinstructions.text()
        tools = self.tools.toPlainText()
        Vectorstoreinassistant = self.Vectorstoreinassistant.toPlainText()
        VectorstoreinThread = self.VectorstoreinThread.toPlainText()
        Upload1fileinthread = self.Upload1fileinthread.text()
        Upload1fileinmessage = self.Upload1fileinmessage.text()
        Upload1imageforvisioninthread = self.Upload1imageforvisioninthread.text()

        if Vectorstoreinassistant == "None":
            Vectorstoreinassistant = None
        else:    
            try:
                Vectorstoreinassistant = ast.literal_eval(Vectorstoreinassistant)
            except json.JSONDecodeError:
                print("Erro: 'Vectorstoreinassistant' não está em formato JSON válido.")
                Vectorstoreinassistant = None
        
        if VectorstoreinThread == "None":
            VectorstoreinThread = None
        else: 
            try:
                VectorstoreinThread = ast.literal_eval(VectorstoreinThread)
            except json.JSONDecodeError:
                print("Erro: 'VectorstoreinThread' não está em formato JSON válido.")
                VectorstoreinThread = None

        if Upload1fileinthread == "None":
            Upload1fileinthread = None

        if Upload1fileinmessage == "None":
            Upload1fileinmessage = None

        if Upload1imageforvisioninthread == "None":
            Upload1imageforvisioninthread = None

        if Aditionalinstructions == "None":
            Aditionalinstructions = None

        if tools == "None":
            tools = None
        else:
            try:
                tools = json.loads(tools)
            except json.JSONDecodeError:
                print("Erro: 'tools' não está em formato JSON válido.")
                tools = None






        self.AI_ByteManager_thread = AI_thread("", 
                                                    Instruction, Key,
                                                    Nameassistant, Modelselect,
                                                    Aditionalinstructions, tools,
                                                    Vectorstoreinassistant, VectorstoreinThread,
                                                    Upload1fileinthread, Upload1fileinmessage,
                                                    Upload1imageforvisioninthread
                                                    
                                                    )
        self.AI_ByteManager_thread.chat_and_thoughts.connect(self.message_signal.emit)
        self.AI_ByteManager_thread.start()


        ########################################################################

        self.show()

    def adjust_height(self, increase=True):
        # Define uma altura base e uma altura máxima
        base_height = 50
        max_height = 150  # Altura máxima desejada

        # Obtém o comprimento do texto atual
        current_text_length = len(self.message_input.toPlainText())

        print(f"Comprimento do texto: {current_text_length}")

        # Se o texto for nulo, retorna à altura base
        if current_text_length == 0:
            self.message_input.setMinimumHeight(base_height)
            print(f"Altura ajustada para base: {base_height}")
            self.message_input.setMinimumHeight(base_height)
            self.message_input.setMaximumHeight(base_height)
            return

        if increase:
            # Lógica para aumentar a altura
            extra_lines = (current_text_length // 40) * 15  # Aumenta a altura a cada 40 caracteres
            new_height = base_height + extra_lines
            if new_height > max_height:
                new_height = max_height
        else:
            # Lógica para diminuir a altura
            new_height = max(base_height, max_height - (current_text_length // 40) * 15)

        print(f"Nova altura: {new_height}")
        # Ajusta a altura do QTextEdit existente
        self.message_input.setMinimumHeight(new_height)
        self.message_input.setMaximumHeight(new_height)

        
    def display_user_message(self, message):
        # Adiciona a mensagem ao QTextEdit
        if self.chat_area:  # Verifique se o QTextEdit foi inicializado corretamente
            self.chat_area.append(message)  # Adiciona a mensagem ao campo de texto
        else:
            print("Erro: chat_area não está inicializado.")


    def send_message(self):
        message = self.message_input.toPlainText()
        
        myModal = QCustomModals.InformationModal(
            title="Mensagem Enviada", 
            parent=self,
            position='top-left',
            closeIcon=":/feather/icons/feather/window_close.png",
            modalIcon=":/feather/icons/feather/info.png",
            description="Sua mensagem foi enviada",
            isClosable=False,
            duration=3000
        )
        myModal.show()

        self.AI_ByteManager_thread.new_message.emit(message)  
        self.message_input.clear()
        self.Upload1fileinthread.setText("None")
        self.Upload1fileinmessage.setText("None")
        self.Upload1imageforvisioninthread.setText("None")
        self.save_config()



    # def display_matrix_message(self, message):
    #     """Exibe a mensagem do MatrixAI alinhada à esquerda, sem duplicar o prefixo."""
    #     # Força a remoção de qualquer ocorrência do prefixo no início da mensagem
    #     if message.startswith("MatrixAI: "):
    #         message = message.replace("MatrixAI: ", "", 1)  # Remove só a primeira ocorrência
    #     # Exibe a mensagem sem duplicar o prefixo
    #     self.chat_area.append(f'<p style="color: black; background-color: #E8E8E8; padding: 8px; border-radius: 8px; margin: 5px auto 5px 0px; text-align: left;"><b>MatrixAI:</b> {message}</p>')
                        
    # def open_file_dialog(self):
    #     options = QFileDialog.Options()
    #     file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)
    #     if file_name:
    #         print(f"Selected file: {file_name}")
    #         if self.is_image_file(file_name):
    #             if "visao" in self.message_input.text().lower() or "vision" in self.message_input.text().lower() or "imagem" in self.message_input.text().lower():
    #                 self.Upload1imageforvisioninthread.setText(file_name)
    #             else:
    #                 self.Upload1fileinmessage.setText(file_name)
    #         else:
    #             self.Upload1fileinthread.setText(file_name)



    def is_image_file(self, file_name):
        # Verifica a extensão do arquivo
        image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
        return file_name.lower().endswith(image_extensions)
    


    
    # def closeEvent(self, event):
    #     self.receiver_thread.stop()
    #     self.sock.close()
    #     event.accept()

    def get_machine_info(self):
        system_info = platform.uname()
        machine = system_info.node
        return machine

    def save_config(self):
        def sanitize_key(key):
            return re.sub(r'[$#\[\]/.]', '_', key)
        
        respostaname_machine = self.get_machine_info()
        ref1 = db.reference(f'save_settings_users', app=app2)
        data1 = ref1.get()
        controle_das_funcao2 = sanitize_key(f"DESKTOP-5L1VA7L")
        controle_das_funcao_info_2 = {
            #"chat_area": f"{self.chat_area.toPlainText()}",
            "Instruction": f"{self.Instruction.toPlainText()}",
            "Key": f"{self.Key.text()}",
            "Nameassistant": f"{self.Nameassistant.text()}",
            "Modelselect": f"{self.Modelselect.text()}",
            "Aditionalinstructions": f"{self.Aditionalinstructions.text()}",
            "tools": f"{self.tools.toPlainText()}",
            "Vectorstoreinassistant": f"{self.Vectorstoreinassistant.toPlainText()}",
            "VectorstoreinThread": f"{self.VectorstoreinThread.toPlainText()}",
            "Upload1fileinthread": f"{self.Upload1fileinthread.text()}",
            "Upload1fileinmessage": f"{self.Upload1fileinmessage.text()}",
            "Upload1imageforvisioninthread": f"{self.Upload1imageforvisioninthread.text()}",
        }
        ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)

    def load_config(self):
        def sanitize_key(key):
            return re.sub(r'[$#\[\]/.]', '_', key)
        try:
            
            respostaname_machine = self.get_machine_info()
            ref1 = db.reference(f'save_settings_users/DESKTOP-5L1VA7L', app=app2)
            data1 = ref1.get()                         

            #chat_area = data1["chat_area"]
            Instruction = data1["Instruction"]
            Key = data1["Key"]
            Nameassistant = data1["Nameassistant"]
            Modelselect = data1["Modelselect"]
            Aditionalinstructions = data1["Aditionalinstructions"]
            tools = data1["tools"]
            Vectorstoreinassistant = data1["Vectorstoreinassistant"]
            VectorstoreinThread = data1["VectorstoreinThread"]
            Upload1fileinthread = data1["Upload1fileinthread"]
            Upload1fileinmessage = data1["Upload1fileinmessage"]
            Upload1imageforvisioninthread = data1["Upload1imageforvisioninthread"]


            def str_to_bool(s):
                return s.lower() in ['true', '1', 't', 'y', 'yes']
            

            #self.chat_area.setPlainText(str(chat_area))
            self.Instruction.setPlainText(str(Instruction))
            self.Key.setText(str(Key))
            self.Nameassistant.setText(str(Nameassistant))
            self.Modelselect.setText(str(Modelselect))
            self.Aditionalinstructions.setText(str(Aditionalinstructions))
            self.tools.setPlainText(str(tools))
            self.Vectorstoreinassistant.setPlainText(str(Vectorstoreinassistant))
            self.VectorstoreinThread.setPlainText(str(VectorstoreinThread))
            self.Upload1fileinthread.setText(str(Upload1fileinthread))
            self.Upload1fileinmessage.setText(str(Upload1fileinmessage))
            self.Upload1imageforvisioninthread.setText(str(Upload1imageforvisioninthread))



        except Exception as e:
            print(e)
            #self.save_config()





########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
######################################################################## 
