########################################################################
## IMPORTS Libs
import sys
import json
import time
import os
import subprocess
import platform
from firebase_admin import credentials, initialize_app, storage, db, delete_app
import concurrent.futures
########################################################################

########################################################################
# IMPORT Pyside2
from PySide2extn.RoundProgressBar import roundProgressBar #IMPORT THE EXTENSION LIBRARY
from PySide2.QtCore import QTimer, Signal, QThread

########################################################################

class QProcessCreateAgent(QThread):
    ModalSucess = Signal(str)
    ModalInfo = Signal(str)

    def __init__(self,
                KeyInFirebase_AgentCreate,
                ModelSelect_AgentCreate,
                Vectorstoreinassistant_AgentCreate,
                VectorstoreinThread_AgentCreate,
                Upload1fileinThread_AgentCreate,
                Upload1fileinmessage_AgentCreate,
                Upload1imageforvisioninThread_AgentCreate,
                Uploadlistfileforcodeinterpreterinthread_AgentCreate,
                Promptmain_AgentCreate,
                PromptRules_AgentCreate,
                PromptExample_AgentCreate,
                NameAgent_AgentCreate,
                AgentCategory_AgentCreate,
                namefunction_agentcreate,
                AgentToolsAgentCreate,
                InstructionAgentCreate,
                FunctionPythonAgentCreate,
                AditionalInstructionsAgentCreate,
                FunctionPythonOutputAgentCreate
            ):
        
        super().__init__()

        self.KeyInFirebase_AgentCreate = KeyInFirebase_AgentCreate
        self.ModelSelect_AgentCreate = ModelSelect_AgentCreate
        self.Vectorstoreinassistant_AgentCreate = Vectorstoreinassistant_AgentCreate
        self.VectorstoreinThread_AgentCreate = VectorstoreinThread_AgentCreate
        self.Upload1fileinThread_AgentCreate = Upload1fileinThread_AgentCreate
        self.Upload1fileinmessage_AgentCreate = Upload1fileinmessage_AgentCreate
        self.Upload1imageforvisioninThread_AgentCreate = Upload1imageforvisioninThread_AgentCreate
        self.Uploadlistfileforcodeinterpreterinthread_AgentCreate = Uploadlistfileforcodeinterpreterinthread_AgentCreate
        self.Promptmain_AgentCreate = Promptmain_AgentCreate
        self.PromptRules_AgentCreate = PromptRules_AgentCreate
        self.PromptExample_AgentCreate = PromptExample_AgentCreate
        self.NameAgent_AgentCreate = NameAgent_AgentCreate
        self.AgentCategory_AgentCreate = AgentCategory_AgentCreate
        self.namefunction_agentcreate = namefunction_agentcreate
        self.AgentToolsAgentCreate = AgentToolsAgentCreate
        self.InstructionAgentCreate = InstructionAgentCreate
        self.FunctionPythonAgentCreate = FunctionPythonAgentCreate
        self.AditionalInstructionsAgentCreate = AditionalInstructionsAgentCreate
        self.FunctionPythonOutputAgentCreate = FunctionPythonOutputAgentCreate

    def run(self):

        KeyInFirebase_AgentCreate = self.KeyInFirebase_AgentCreate
        ModelSelect_AgentCreate = self.ModelSelect_AgentCreate
        if self.Vectorstoreinassistant_AgentCreate.strip():
            Vectorstoreinassistant_AgentCreate = [self.Vectorstoreinassistant_AgentCreate]
        else:
            Vectorstoreinassistant_AgentCreate = None

        if self.VectorstoreinThread_AgentCreate.strip():
            VectorstoreinThread_AgentCreate = [self.VectorstoreinThread_AgentCreate]
        else:
            VectorstoreinThread_AgentCreate = None


        if self.Upload1fileinThread_AgentCreate.strip():
            Upload1fileinThread_AgentCreate = self.Upload1fileinThread_AgentCreate
        else:
            Upload1fileinThread_AgentCreate = None


        if self.Upload1fileinmessage_AgentCreate.strip():
            Upload1fileinmessage_AgentCreate = self.Upload1fileinmessage_AgentCreate
        else:
            Upload1fileinmessage_AgentCreate = None


        if self.Upload1imageforvisioninThread_AgentCreate.strip():
            Upload1imageforvisioninThread_AgentCreate = self.Upload1imageforvisioninThread_AgentCreate
        else:
            Upload1imageforvisioninThread_AgentCreate = None


        if self.Uploadlistfileforcodeinterpreterinthread_AgentCreate.strip():
            Uploadlistfileforcodeinterpreterinthread_AgentCreate = [self.Uploadlistfileforcodeinterpreterinthread_AgentCreate]
        else:
            Uploadlistfileforcodeinterpreterinthread_AgentCreate = None

        Promptmain_AgentCreate = self.Promptmain_AgentCreate
        PromptRules_AgentCreate = self.PromptRules_AgentCreate
        PromptExample_AgentCreate = self.PromptExample_AgentCreate
        NameAgent_AgentCreate = self.NameAgent_AgentCreate
        category_target = self.AgentCategory_AgentCreate


        self.AgentToolsAgentCreate_()

        time.sleep(2)

        self.InstructionAgentCreate_()

        time.sleep(2)

        self.FunctionPythonAgentCreate_()

        time.sleep(2)

        self.FunctionPythonOutputAgentCreate_()


        time.sleep(2)


        PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/Agents/{category_target}'))
        file_path = os.path.join(PATH_caminho, f"{NameAgent_AgentCreate}.py")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(F'''
#########################################
# IMPORT SoftwareAI Core
from ..._init_core_ import *
#########################################
# IMPORT SoftwareAI Libs 
from ..._init_libs_ import *
#########################################
# IMPORT SoftwareAI All Paths 
from ..._init_paths_ import *
#########################################
# IMPORT SoftwareAI Instructions
from ...SoftwareAI.Instructions._init_Instructions_ import *
#########################################
# IMPORT SoftwareAI Tools
from ...SoftwareAI.Tools._init_tools_ import *
#########################################
# IMPORT SoftwareAI Keys 
from ..._init_keys_ import *
#########################################

def {NameAgent_AgentCreate}_{KeyInFirebase_AgentCreate}():
    key = "{KeyInFirebase_AgentCreate}"
    nameassistant = "{NameAgent_AgentCreate}"
    model_select = "{ModelSelect_AgentCreate}"
    
    Upload_1_file_in_thread = {Upload1fileinThread_AgentCreate}
    Upload_1_file_in_message = {Upload1fileinmessage_AgentCreate}
    Upload_1_image_for_vision_in_thread = {Upload1imageforvisioninThread_AgentCreate}
    vectorstore_in_assistant = {Vectorstoreinassistant_AgentCreate}
    vectorstore_in_Thread = {VectorstoreinThread_AgentCreate}
    Upload_list_for_code_interpreter_in_thread = {Uploadlistfileforcodeinterpreterinthread_AgentCreate}

    {NameAgent_AgentCreate} = AutenticateAgent.create_or_auth_AI(key, instruction{NameAgent_AgentCreate}, nameassistant, model_select, tools_{NameAgent_AgentCreate}, vectorstore_in_assistant)
    
    mensagem = f"""
    {Promptmain_AgentCreate}
    """
    
    exemplo = f""" 
    {PromptExample_AgentCreate}
    """
    
    regras = f""" 
    {PromptRules_AgentCreate}
    
    """
    mensage_final = mensagem + exemplo + regras
    
    response = ResponseAgent.ResponseAgent_message_with_assistants(mensage_final,
                                                                    Upload_1_file_in_thread,
                                                                    Upload_1_file_in_message,
                                                                    Upload_1_image_for_vision_in_thread, 
                                                                    Upload_list_for_code_interpreter_in_thread,
                                                                    vectorstore_in_Thread,
                                                                    tools_{NameAgent_AgentCreate}, 
                                                                    {NameAgent_AgentCreate}, 
                                                                    model_select,
                                                                    adxitional_instructions_{NameAgent_AgentCreate}, key)
    return response
            ''')
            file.close()

        self.ModalInfo.emit("Agent Created !!, Configuring launchers")

        time.sleep(2)


        with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Tools')), f"_init_tools_.py"), 'r+', encoding='utf-8') as file:
            content = file.read()
            if f"{self.AgentCategory_AgentCreate}.{self.NameAgent_AgentCreate}_tools" not in content:
                
                file.write(F'''
from .{self.AgentCategory_AgentCreate}.{self.NameAgent_AgentCreate}_tools import *
                ''')
                file.close()

        self.ModalInfo.emit("Launcher Tools Configured !!")


        time.sleep(2)



        with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Instructions')), f"_init_Instructions_.py"), 'r+', encoding='utf-8') as file:
            content = file.read()
            if f"{self.AgentCategory_AgentCreate}.{self.NameAgent_AgentCreate}" not in content:

                file.write(F'''
from .{self.AgentCategory_AgentCreate}.{self.NameAgent_AgentCreate} import *
                ''')
                file.close()

        self.ModalInfo.emit("Launcher Instructions Configured !!")

        time.sleep(2)



        with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Functions')), f"_init_functions_.py"), 'r+', encoding='utf-8') as file:
            content = file.read()
            if f"{self.namefunction_agentcreate}_function" not in content:

                file.write(F'''
from .{self.namefunction_agentcreate}_function import *
                ''')
                file.close()

        self.ModalInfo.emit("Launcher Functions Configured !!")


        time.sleep(2)

        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Functions_Submit_Outputs'))
        init_file_path = os.path.join(base_path, '_init_submit_outputs_.py')

        new_function_name = f"submit_output_{self.namefunction_agentcreate}"
        with open(init_file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            
            # Adicionar função à lista se ainda não estiver presente
            if new_function_name not in content:
                updated_content = content.replace(
                    "functions_to_call = [",
                    f"functions_to_call = [\n        {new_function_name},"
                )
                file.seek(0)
                file.write(updated_content)
                file.truncate()
                print("Função adicionada à lista com sucesso!")
            else:
                print("Função já está na lista.")


        with open(init_file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            new_import = f"from .{self.namefunction_agentcreate}_submit_outputs import submit_output_{self.namefunction_agentcreate}\n"
            if new_import not in content:
                file.seek(0)
                file.write(new_import + content)
                file.truncate()

        self.ModalInfo.emit("Launcher Functions Outputs Configured !!")

        time.sleep(2)


        self.ModalSucess.emit("The agent was created with SoftwareAI, now you can add arguments to this agent if you want !!")






    def FunctionPythonOutputAgentCreate_(self):
        if self.FunctionPythonOutputAgentCreate.strip():

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Functions_Submit_Outputs'))
            file_path = os.path.join(PATH_caminho, f"{self.namefunction_agentcreate}_submit_outputs.py")
            with open(file_path, 'w', encoding='utf-8') as file:
               
                file.write(f'''

#########################################
# IMPORT SoftwareAI Libs 
from CoreApp._init_libs_ import *
#########################################
# IMPORT SoftwareAI Functions
from ..Functions._init_functions_ import *
#########################################
tool_outputs = []
{self.FunctionPythonOutputAgentCreate}

                ''')
                file.close()

                self.ModalInfo.emit("Function Python Output Agent Created !!")


    def AgentToolsAgentCreate_(self):
        if self.AgentToolsAgentCreate.strip():

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Tools/{self.AgentCategory_AgentCreate}'))
            file_path = os.path.join(PATH_caminho, f"{self.NameAgent_AgentCreate}_tools.py")
            with open(file_path, 'w', encoding='utf-8') as file:
                
                file.write(f'''

tools_{self.NameAgent_AgentCreate} = [
{self.AgentToolsAgentCreate}
]

                ''')
                file.close()
                self.ModalInfo.emit("Agent Tools Created !!")



    def InstructionAgentCreate_(self):

        if self.InstructionAgentCreate.strip():
            if self.AditionalInstructionsAgentCreate.strip():
                AditionalInstructionsAgentCreate = f"""{self.AditionalInstructionsAgentCreate}"""
            else:
                AditionalInstructionsAgentCreate = "None"

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/{self.AgentCategory_AgentCreate}'))
            file_path = os.path.join(PATH_caminho, f"{self.NameAgent_AgentCreate}.py")
            with open(file_path, 'w', encoding='utf-8') as file:
                content = self.InstructionAgentCreate
                file.write(F'''
instruction{self.NameAgent_AgentCreate} = """ 
{content}
""" 
adxitional_instructions_{self.NameAgent_AgentCreate} = {AditionalInstructionsAgentCreate}

                ''')
                file.close()
                self.ModalInfo.emit("Instruction Agent Created !!")

    def FunctionPythonAgentCreate_(self):
                
        if self.FunctionPythonAgentCreate.strip():

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Functions'))
            file_path = os.path.join(PATH_caminho, f"{self.namefunction_agentcreate}_function.py")
            with open(file_path, 'w', encoding='utf-8') as file:
                content = self.FunctionPythonAgentCreate
                file.write(f'''

{content}

                ''')
                file.close()
                self.ModalInfo.emit("Function Python Agent Created !!")



