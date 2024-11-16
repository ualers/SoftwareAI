
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


class Pre_Project_Document:
    def __init__(self):
        pass


    def AI_1_Pre_Project_Document_Writer(self, mensagem):
        """
        Nome da IA: Tigrao \n
        Função: Escritor de Documento Pre-Projeto De Software \n
        Horario de trabalho: 1H\n
        :param mensagem: str \n
        :param output: path_name_doc_Pre_Projeto
        """   

       

        key = "AI_Tigrao_Escritor_de_documento_Pre_Projeto"
        nameassistant = "AI Tigrao Escritor de documento Pre-Projeto"
        model_select = "gpt-4o-mini-2024-07-18"
        
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        Upload_list_for_code_interpreter_in_thread = None
        vectorstore_in_Thread = None
        vectorstore_in_agent = None

           

        AI_Escritor_de_documento_Pre_Projeto = AutenticateAgent.create_or_auth_AI(key, instructionTigrao, nameassistant, model_select, tools_Tigrao, vectorstore_in_agent)

        mensaxgem = f"crie um documento Pre-Projeto baseado nas informacoes asseguir: \n  {mensagem}"
        format = 'Responda no formato JSON Exemplo: {"doc_Pre_Projeto": "..."},{"name_doc_Pre_Projeto": "..."} '
        mensage3 = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensage3,
                                                                    Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                    Upload_1_image_for_vision_in_thread, Upload_list_for_code_interpreter_in_thread, vectorstore_in_Thread,
                                                                    tools_Tigrao,  AI_Escritor_de_documento_Pre_Projeto, model_select, adxitional_instructions_Tigrao, key)
        #print(response)
        
        #python_functions.save_json(response, path_name_doc_Pre_Projeto)
        try:
            teste_dict = json.loads(response)
            documento_Pre_Projeto = teste_dict['doc_Pre_Projeto']
            print(documento_Pre_Projeto)
            
            name_doc_Pre_Projeto = teste_dict['name_doc_Pre_Projeto']
            path_name_doc_Pre_Projeto = os.getenv("PATH_NAME_DOC_PRE_PROJETO_ENV")
            path = os.path.dirname(path_name_doc_Pre_Projeto)
            novo_caminho = os.path.join(path, name_doc_Pre_Projeto)
            print(name_doc_Pre_Projeto)
           

            python_functions.save_TXT(documento_Pre_Projeto, novo_caminho, "w")
            return path_name_doc_Pre_Projeto
        except Exception as E:
            print(E)
            path_name_doc_Pre_Projeto = os.getenv("PATH_NAME_DOC_PRE_PROJETO_ENV")
            python_functions.save_TXT(response, path_name_doc_Pre_Projeto, "w")
            return path_name_doc_Pre_Projeto









