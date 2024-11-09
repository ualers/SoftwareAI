
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

       


        instructionAI_Escritor_de_documento_Pre_Projeto = """ 
        Seu Nome é Tigrao, Voce é um Escritor de Documento Pre-Projeto De Software da empresa Urobotsoftware,
        crie o documento com as informacoes fornecidas para que o documento criado por voce posteriormente seja enviados para o Gerente de Projeto que analizará o documento e criará o Cronograma e planilha do Projeto

        Responda o Documento Pre-Projeto no formato JSON
        Exemplo:
        {"doc_Pre_Projeto": "documento Pre-Projeto ..."}

        Responda o nome do Documento Pre-Projeto no formato JSON
        Exemplo:
        {"name_doc_Pre_Projeto": "nome do Documento ..."}

        """
        key = "AI_Tigrao_Escritor_de_documento_Pre_Projeto"
        nameassistant = "AI Tigrao Escritor de documento Pre-Projeto"
        model_select = "gpt-4o-mini-2024-07-18"
        adxitional_instructions = None
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        Upload_list_for_code_interpreter_in_thread = None
        vectorstore_in_Thread = None
        vectorstore_in_agent = None
        tools = None
        
           

        AI_Escritor_de_documento_Pre_Projeto = AutenticateAgent.create_or_auth_AI(key, instructionAI_Escritor_de_documento_Pre_Projeto, nameassistant, model_select, tools, vectorstore_in_agent)

        mensaxgem = f"crie um documento Pre-Projeto baseado nas informacoes asseguir: \n  {mensagem}"

        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                    Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                    Upload_1_image_for_vision_in_thread, Upload_list_for_code_interpreter_in_thread, vectorstore_in_Thread,
                                                                    tools,  AI_Escritor_de_documento_Pre_Projeto, model_select, adxitional_instructions, key)
        #print(response)
        
          

        path_name_doc_Pre_Projeto = os.getenv("PATH_NAME_DOC_PRE_PROJETO_ENV")
        python_functions.save_TXT(response, path_name_doc_Pre_Projeto, "w")
        #python_functions.save_json(response, path_name_doc_Pre_Projeto)
        try:
            teste_dict = json.loads(response)
            documento_Pre_Projeto = teste_dict['doc_Pre_Projeto']
            print(documento_Pre_Projeto)
            
            name_doc_Pre_Projeto = teste_dict['name_doc_Pre_Projeto']
            path_name_doc_Pre_Projeto = f"Work_Environment/Create_doc_Pre_Projeto/{name_doc_Pre_Projeto}.txt"
            print(name_doc_Pre_Projeto)
            print(path_name_doc_Pre_Projeto)

            python_functions.save_TXT(documento_Pre_Projeto, path_name_doc_Pre_Projeto, "w")
            return path_name_doc_Pre_Projeto
        except:
            pass

            
        return path_name_doc_Pre_Projeto









