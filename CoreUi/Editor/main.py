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


# Caminho absoluto para o diretório onde SoftwareAI está localizado (raiz do projeto)
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI'))
sys.path.append(caminho_raiz)

########################################################################
# IMPORT CoreApp
from CoreUi.ChatSoftwareAI.Chat.AIQthread import AI_thread
from CoreUi.Editor.Process import QProcessCreateAgent
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
from src_.ui_interface import *
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
        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style.json"})
        self.liveCompileQss = True
        self.checkForMissingicons = False # do not generate new icons

        ########################################################################


        self.myStackedWidget = self.ui.myStackedWidget

        self.CurrentInstruction = self.ui.Current_instuction_html_edit
        self.CurrentInstruction.setReadOnly(True)


        self.InstructionSelector = self.ui.comboBox_list_instruction_edit
        self.list_instruction()
        self.InstructionSelector.currentTextChanged.connect(self.on_InstructionSelector_changed)

        
        self.Instructioninput_edit = self.ui.instruction_input_edit
        self.Instructioninput_edit.textChanged.connect(lambda: self.adjust_height(self.Instructioninput_edit, max_height=170))

        self.change_instruction_button_edit = self.ui.change_instruction_button_edit
        self.change_instruction_button_edit.clicked.connect(self.change_instruction)




        self.Add_new_instructions_button_edit = self.ui.Add_new_instructions_button_edit




        self.InstructionSelector_create = self.ui.comboBox_list_agent_for_create_instruction_create
        self.list_agents()


        self.InstructionCategory_create = self.ui.comboBox_category_instruction_create
        self.list_category_instruction()


        self.UseVectorstoreToGenerateFiles = self.ui.UseVectorstoreToGenerateFiles


        self.KeyInFirebase_AgentCreate = self.ui.KeyInFirebase
        self.NameAgent_AgentCreate = self.ui.NameAgent
        self.ModelSelect_AgentCreate = self.ui.ModelSelect
        self.AgentCategory_AgentCreate = self.ui.AgentCategory

        self.Vectorstoreinassistant_AgentCreate = self.ui.Vectorstoreinassistant
        self.VectorstoreinassistantByUser_AgentCreate = self.ui.VectorstoreinassistantByUser

        self.VectorstoreinThread_AgentCreate = self.ui.VectorstoreinThread
        self.VectorstoreinThreadByUser_AgentCreate = self.ui.VectorstoreinThreadByUser

        self.Upload1fileinThread_AgentCreate = self.ui.Upload1fileinThread
        self.Upload1fileinThreadByUser_AgentCreate = self.ui.Upload1fileinThreadByUser

        self.Upload1fileinmessage_AgentCreate = self.ui.Upload1fileinmessage
        self.Upload1fileinmessageByUser_AgentCreate = self.ui.Upload1fileinmessageByUser

        self.Upload1imageforvisioninThread_AgentCreate = self.ui.Upload1imageforvisioninThread
        self.Upload1imageforvisioninThreadByUser_AgentCreate = self.ui.Upload1imageforvisioninThreadByUser

        self.Uploadlistfileforcodeinterpreterinthread_AgentCreate = self.ui.Uploadlistfileforcodeinterpreterinthread
        self.UploadlistfileforcodeinterpreterinthreadByUser_AgentCreate = self.ui.Uploadlistfileforcodeinterpreterinthread

        self.Promptmain_AgentCreate = self.ui.Promptmain
        self.PromptExample_AgentCreate = self.ui.PromptExample
        self.PromptRules_AgentCreate = self.ui.PromptRules


        self.InstructionAgentCreate = self.ui.InstructionAgentCreate
        self.AditionalInstructionsAgentCreate = self.ui.AditionalInstructionsAgentCreate


        self.AgentToolsAgentCreate = self.ui.AgentTools
        self.FunctionPythonAgentCreate = self.ui.FunctionPython
        self.FunctionPythonOutputAgentCreate = self.ui.FunctionPythonOutput
    

        self.namefunction_agentcreate = self.ui.namefunction_agentcreate



        self.CreateAgentButton = self.ui.CreateAgent
        self.CreateAgentButton.clicked.connect(self.CreateAgentButtonClicked)
        self.list_category_Agent()

        self.myStackedWidget = self.ui.myStackedWidget



        self.Instructioninput_create = self.ui.New_instruction_html_create
        self.Instructioninput_create.textChanged.connect(lambda: self.adjust_height(self.Instructioninput_create, max_height=300))
 
        self.NameForInstruction_create = self.ui.NameForInstruction_create

        self.CreateInstructionbutton_create = self.ui.CreateInstructionbutton_create
        self.CreateInstructionbutton_create.clicked.connect(self.create_instruction)

        self.show()

    def CreateAgentButtonClicked(self):
        
        KeyInFirebase_AgentCreate = self.KeyInFirebase_AgentCreate.toPlainText()
        ModelSelect_AgentCreate = self.ModelSelect_AgentCreate.toPlainText()
        Vectorstoreinassistant_AgentCreate = self.Vectorstoreinassistant_AgentCreate.toPlainText()
        VectorstoreinThread_AgentCreate = self.VectorstoreinThread_AgentCreate.toPlainText()
        Upload1fileinThread_AgentCreate = self.Upload1fileinThread_AgentCreate.toPlainText()
        Upload1fileinmessage_AgentCreate = self.Upload1fileinmessage_AgentCreate.toPlainText()
        Upload1imageforvisioninThread_AgentCreate = self.Upload1imageforvisioninThread_AgentCreate.toPlainText()
        Uploadlistfileforcodeinterpreterinthread_AgentCreate = self.Uploadlistfileforcodeinterpreterinthread_AgentCreate.toPlainText()
        Promptmain_AgentCreate = self.Promptmain_AgentCreate.toPlainText()
        PromptRules_AgentCreate = self.PromptRules_AgentCreate.toPlainText()
        PromptExample_AgentCreate = self.PromptExample_AgentCreate.toPlainText()
        NameAgent_AgentCreate = self.NameAgent_AgentCreate.toPlainText()
        category_target = self.AgentCategory_AgentCreate.currentText()
        namefunction_agentcreate = self.namefunction_agentcreate.toPlainText()
        AgentToolsAgentCreate = self.AgentToolsAgentCreate.toPlainText()
        InstructionAgentCreate = self.InstructionAgentCreate.toPlainText()
        FunctionPythonAgentCreate = self.FunctionPythonAgentCreate.toPlainText()
        AditionalInstructionsAgentCreate = self.AditionalInstructionsAgentCreate.toPlainText()
        FunctionPythonOutputAgentCreate = self.FunctionPythonOutputAgentCreate.toPlainText()
        
        self.thread_processe_create_agent = QProcessCreateAgent(
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
            category_target,
            namefunction_agentcreate,
            AgentToolsAgentCreate,
            InstructionAgentCreate,
            FunctionPythonAgentCreate,
            AditionalInstructionsAgentCreate,
            FunctionPythonOutputAgentCreate

        )
        self.thread_processe_create_agent.ModalSucess.connect(self.update_custommodals_SuccessModal)
        self.thread_processe_create_agent.ModalInfo.connect(self.update_custommodals_info)

        self.thread_processe_create_agent.start()


#         self.AgentToolsAgentCreate_()

#         self.InstructionAgentCreate_()

#         self.FunctionPythonAgentCreate_()

#         self.FunctionPythonOutputAgentCreate_()



#         PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/Agents/{category_target}'))
#         file_path = os.path.join(PATH_caminho, f"{NameAgent_AgentCreate}.py")
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(F'''
# #########################################
# # IMPORT SoftwareAI Core
# from ..._init_core_ import *
# #########################################
# # IMPORT SoftwareAI Libs 
# from ..._init_libs_ import *
# #########################################
# # IMPORT SoftwareAI All Paths 
# from ..._init_paths_ import *
# #########################################
# # IMPORT SoftwareAI Instructions
# from ...SoftwareAI.Instructions._init_Instructions_ import *
# #########################################
# # IMPORT SoftwareAI Tools
# from ...SoftwareAI.Tools._init_tools_ import *
# #########################################
# # IMPORT SoftwareAI Keys 
# from ..._init_keys_ import *
# #########################################

# def {NameAgent_AgentCreate}_{KeyInFirebase_AgentCreate}(self):
#     key = "{KeyInFirebase_AgentCreate}"
#     nameassistant = "{NameAgent_AgentCreate}"
#     model_select = "{ModelSelect_AgentCreate}"
    
#     Upload_1_file_in_thread = {Upload1fileinThread_AgentCreate}
#     Upload_1_file_in_message = {Upload1fileinmessage_AgentCreate}
#     Upload_1_image_for_vision_in_thread = {Upload1imageforvisioninThread_AgentCreate}
#     vectorstore_in_assistant = {Vectorstoreinassistant_AgentCreate}
#     vectorstore_in_Thread = {VectorstoreinThread_AgentCreate}
#     Upload_list_for_code_interpreter_in_thread = {Uploadlistfileforcodeinterpreterinthread_AgentCreate}

#     {NameAgent_AgentCreate} = AutenticateAgent.create_or_auth_AI(key, instruction{NameAgent_AgentCreate}, nameassistant, model_select, tools_{NameAgent_AgentCreate}, vectorstore_in_assistant)
#     mensagem = f"""
#     {Promptmain_AgentCreate}
#     """
#     exemplo = f""" 
#     {PromptExample_AgentCreate}
#     """
#     regras = f""" 
#     {PromptRules_AgentCreate}
#     """
#     mensage_final = mensagem + exemplo + regras
#     response = ResponseAgent.ResponseAgent_message_with_assistants(mensage_final,
#                                                                     Upload_1_file_in_thread,
#                                                                     Upload_1_file_in_message,
#                                                                     Upload_1_image_for_vision_in_thread, 
#                                                                     Upload_list_for_code_interpreter_in_thread,
#                                                                     vectorstore_in_Thread,
#                                                                     tools_{NameAgent_AgentCreate}, 
#                                                                     {NameAgent_AgentCreate}, 
#                                                                     model_select,
#                                                                     adxitional_instructions_{NameAgent_AgentCreate}, key)
#     return response
#             ''')
#             file.close()

#         self.update_custommodals_SuccessModal("Agent Created !!, Configuring launchers")


#         with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Tools')), f"_init_tools_.py"), 'a', encoding='utf-8') as file:
#             file.write(F'''
# from .{self.AgentCategory_AgentCreate.currentText()}.{self.NameAgent_AgentCreate.toPlainText()}_tools import *
#             ''')
#             file.close()

#         self.update_custommodals_info("Launcher Tools Configured !!")




#         with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Instructions')), f"_init_Instructions_.py"), 'a', encoding='utf-8') as file:
#             file.write(F'''
# from .{self.AgentCategory_AgentCreate.currentText()}.{self.NameAgent_AgentCreate.toPlainText()} import *
#             ''')
#             file.close()

#         self.update_custommodals_info("Launcher Instructions Configured !!")



#         with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Functions')), f"_init_functions_.py"), 'a', encoding='utf-8') as file:
#             file.write(F'''
# from .{self.namefunction_agentcreate.toPlainText()} import *
#             ''')
#             file.close()

#         self.update_custommodals_info("Launcher Functions Configured !!")


#         base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Functions_Submit_Outputs'))
#         init_file_path = os.path.join(base_path, '_init_submit_outputs_.py')

#         with open(init_file_path, 'r+', encoding='utf-8') as file:
#             content = file.read()
#             new_import = f"from .{self.namefunction_agentcreate.toPlainText()} import submit_output_{self.namefunction_agentcreate.toPlainText()}\n"
#             if new_import not in content:
#                 file.seek(0)
#                 file.write(new_import + content)
#                 file.truncate()


#         with open(init_file_path, 'r+', encoding='utf-8') as file:
#             content = file.read()
#             if f"submit_output_{self.namefunction_agentcreate.toPlainText()}" not in content:
#                 updated_content = content.replace(
#                     "functions_to_call = [",
#                     f"functions_to_call = [\n        submit_output_{self.namefunction_agentcreate.toPlainText()},"
#                 )
#                 file.seek(0)
#                 file.write(updated_content)
#                 file.truncate()


#         self.update_custommodals_info("Launcher Functions Outputs Configured !!")



#         self.update_custommodals_SuccessModal("The agent was created with SoftwareAI, now you can add arguments to this agent if you want !!")






    def FunctionPythonOutputAgentCreate_(self):
        if self.FunctionPythonOutputAgentCreate.toPlainText().strip():

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Functions_Submit_Outputs'))
            file_path = os.path.join(PATH_caminho, f"{self.namefunction_agentcreate.toPlainText()}_submit_outputs.py")
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
{self.FunctionPythonOutputAgentCreate.toPlainText()}

                ''')
                file.close()

                self.update_custommodals_info("Function Python Output Agent Created !!")


    def AgentToolsAgentCreate_(self):
        if self.AgentToolsAgentCreate.toPlainText().strip():

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Tools/{self.AgentCategory_AgentCreate.currentText()}'))
            file_path = os.path.join(PATH_caminho, f"{self.NameAgent_AgentCreate.toPlainText()}_tools.py")
            with open(file_path, 'w', encoding='utf-8') as file:
                content = self.InstructionAgentCreate.toPlainText()
                file.write(f'''

tools_{self.NameAgent_AgentCreate.toPlainText()} = [
{self.AgentToolsAgentCreate.toPlainText()}
]

                ''')
                file.close()
                self.update_custommodals_info("Agent Tools Created !!")



    def InstructionAgentCreate_(self):

        if self.InstructionAgentCreate.toPlainText().strip():
            if self.AditionalInstructionsAgentCreate.toPlainText().strip():
                AditionalInstructionsAgentCreate = f"""{self.AditionalInstructionsAgentCreate.toPlainText()}"""
            else:
                AditionalInstructionsAgentCreate = "None"

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/{self.AgentCategory_AgentCreate.currentText()}'))
            file_path = os.path.join(PATH_caminho, f"{self.NameAgent_AgentCreate.toPlainText()}.py")
            with open(file_path, 'w', encoding='utf-8') as file:
                content = self.InstructionAgentCreate.toPlainText()
                file.write(F'''
instruction{self.NameAgent_AgentCreate.toPlainText()} = """ 
{content}
""" 
adxitional_instructions_{self.NameAgent_AgentCreate.toPlainText()} = {AditionalInstructionsAgentCreate}

                ''')
                file.close()
                self.update_custommodals_info("Instruction Agent Created !!")

    def FunctionPythonAgentCreate_(self):
                
        if self.FunctionPythonAgentCreate.toPlainText().strip():

            PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Functions'))
            file_path = os.path.join(PATH_caminho, f"{self.namefunction_agentcreate.toPlainText()}_function.py")
            with open(file_path, 'w', encoding='utf-8') as file:
                content = self.FunctionPythonAgentCreate.toPlainText()
                file.write(f'''

{content}

                ''')
                file.close()
                self.update_custommodals_info("Function Python Agent Created !!")




    def list_category_Agent(self):
        paths_category = [
            'Software_Requirements_Analysis',
            'Software_Planning',
            'Software_Documentation',
            'Software_Development',
            'Pre_Project',
            'Company_Managers',
            'Company_CEO',
        ]
        for path in paths_category:
            self.AgentCategory_AgentCreate.addItem(path)

    def create_instruction(self):
        if self.Instructioninput_create.toPlainText().strip():
            NameForInstruction_create = self.NameForInstruction_create.text()
            agent_target =  self.InstructionSelector_create.currentText()
            category_target = self.InstructionCategory_create.currentText()
            paths_category = self.init_paths_category()
            for path in paths_category:
                if path == category_target:
                    PATH_caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/{category_target}'))
                    file_path = os.path.join(PATH_caminho, f"{NameForInstruction_create}.py")
                    with open(file_path, 'w', encoding='utf-8') as file:
                        content = self.Instructioninput_create.toPlainText()
                        file.write(F'''instruction{agent_target} = """{content}"""\nadxitional_instructions_{agent_target} = None''')
                        file.close()

                    self.Instructioninput_create.clear()
                    self.update_custommodals_SuccessModal("Your Instruction Was Created", "bottom-left")
        else:
            self.update_custommodals_erro("The Instruction Field Is Empty.")

    def list_agents(self):
        paths_agents = self.init_paths_agents()
        for path in paths_agents:
            agentss = os.listdir(path)
            for agent in agentss:
                iagents_refact = agent.replace(".py", "").replace("__pycache__", "").strip()
                if iagents_refact:
                    self.InstructionSelector_create.addItem(iagents_refact)


    def list_category_instruction(self):
        paths_category = [
            'Software_Requirements_Analysis',
            'Software_Planning',
            'Software_Documentation',
            'Software_Development',
            'Pre_Project',
            'Company_Managers',
            'Company_CEO',
        ]
        for path in paths_category:
            self.InstructionCategory_create.addItem(path)



    def change_instruction(self):
        if self.Instructioninput_edit.toPlainText().strip():
            instructionarqname = self.InstructionSelector.currentText()
            paths_instruct = self.init_paths()
            for path in paths_instruct:
                instructions = os.listdir(path)
                for instruct in instructions:
                    instruct_refact = instruct.replace(".py", "").replace("__pycache__", "").strip()
                    if instruct_refact == instructionarqname:
                        file_path = os.path.join(path, f"{instruct_refact}.py")
                        with open(file_path, 'w', encoding='utf-8') as file:
                            content = self.Instructioninput_edit.toPlainText()
                            file.write(content)
                            file.close()
                        self.update_custommodals_SuccessModal(description="Your Instruction Has Been Updated", pos="bottom-left")
                        self.Instructioninput_edit.clear()
                        self.open_and_read(file_path)
        else:
            self.update_custommodals_erro("The Instruction Field Is Empty.")


    def on_InstructionSelector_changed(self, text):
        paths_instruct = self.init_paths()
        for path in paths_instruct:
            instructions = os.listdir(path)
            for instruct in instructions:
                instruct_refact = instruct.replace(".py", "").replace("__pycache__", "").strip()
                if instruct_refact == text:
                    file_path = os.path.join(path, f"{instruct_refact}.py")
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.CurrentInstruction.clear()
                        self.CurrentInstruction.append(content)


    def list_instruction(self):
        paths_instruct = self.init_paths()
        for path in paths_instruct:
            instructions = os.listdir(path)
            for instruct in instructions:
                instruct_refact = instruct.replace(".py", "").replace("__pycache__", "").strip()
                if instruct_refact:
                    self.InstructionSelector.addItem(instruct_refact)


    def adjust_height(self, element, max_height = 150, increase=True):
        base_height = 50
        current_text_length = len(element.toPlainText())
        if current_text_length == 0:
            element.setMinimumHeight(base_height)
            element.setMinimumHeight(base_height)
            element.setMaximumHeight(base_height)
            return
        if increase:
            extra_lines = (current_text_length // 40) * 15  
            new_height = base_height + extra_lines
            if new_height > max_height:
                new_height = max_height
        else:
            new_height = max(base_height, max_height - (current_text_length // 40) * 15)

        element.setMinimumHeight(new_height)
        element.setMaximumHeight(new_height)

    def init_paths_category(self):
        paths_category = [
            'Software_Requirements_Analysis',
            'Software_Planning',
            'Software_Documentation',
            'Software_Development',
            'Pre_Project',
            'Company_Managers',
            'Company_CEO',
        ]
        return paths_category
    
    def init_paths_agents(self):
        paths_instruct = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Software_Requirements_Analysis')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Software_Planning')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Software_Documentation')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Software_Development')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Pre_Project')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Company_Managers')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/Agents/Company_CEO')),
        ]
        return paths_instruct
    
    def init_paths(self):
        paths_instruct = [
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Software_Requirements_Analysis')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Software_Planning')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Software_Documentation')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Software_Development')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Pre_Project')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Company_Managers')),
            os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../SoftwareAI/CoreApp/SoftwareAI/Instructions/Company_CEO')),
        ]
        return paths_instruct
    


    def open_and_read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.CurrentInstruction.setPlainText(content)



    def update_custommodals_erro(self, description, pos='center-center'):

        myModal = QCustomModals.ErrorModal(
            title="Information", 
            parent=self.myStackedWidget,
            position=pos,
            closeIcon=":/feather/icons/feather/window_close.png",
            modalIcon=":/material_design/icons/material_design/info.png",
            description=description,
            isClosable=False,
            duration=3000
        )
        myModal.show()


    def update_custommodals_warning(self, description, pos='center-center'):

        myModal = QCustomModals.WarningModal(
            title="Information", 
            parent=self.myStackedWidget,
            position=pos,
            closeIcon=":/feather/icons/feather/window_close.png",
            modalIcon=":/material_design/icons/material_design/info.png",
            description=description,
            isClosable=False,
            duration=3000
        )
        myModal.show()


    def update_custommodals_info(self, description, pos='top-right'):

        myModal = QCustomModals.InformationModal(
            title="Information", 
            parent=self.myStackedWidget,
            position=pos,
            closeIcon=":/feather/icons/feather/window_close.png",
            modalIcon=":/material_design/icons/material_design/info.png",
            description=description,
            isClosable=False,
            duration=3000
        )
        myModal.show()


    def update_custommodals_SuccessModal(self, description, pos='center-center'):

        myModal = QCustomModals.SuccessModal(
            title="Information", 
            parent=self.myStackedWidget,
            position=pos,
            closeIcon=":/feather/icons/feather/window_close.png",
            modalIcon=":/material_design/icons/material_design/info.png",
            description=description,
            isClosable=False,
            duration=5000
        )
        myModal.show()


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
