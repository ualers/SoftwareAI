
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




class Equipe_De_Solucoes:
    def __init__(self):
        pass

    def Dallas_Equipe_De_Solucoes_Roadmap(self, cronograma_do_projeto, planilha_json, doc_Pre_Projeto):
        read_cronograma_do_projeto = python_functions.analyze_txt(cronograma_do_projeto)
        read_planilha_json = python_functions.analyze_txt(planilha_json)
        read_doc_Pre_Projeto = python_functions.analyze_txt(doc_Pre_Projeto)

        key = "AI_Dallas_Equipe_de_Solucoes"
        nameassistant = "AI Dallas Equipe de Solucoes"
        model_select = "gpt-4o-mini-2024-07-18"

        
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None
        Upload_list_for_code_interpreter_in_thread = None

        # ----------------------------------------------- 
        AI_Dallas_Equipe_de_Solucoes = AutenticateAgent.create_or_auth_AI(key, instructionDallas, nameassistant, model_select, tools_Dallas, vectorstore_in_assistant)
        mensagem = f"""
        Planeje um Roadmap do Projeto com base no Cronograma,Planilha e Documento Pre Projeto asseguir:\n

        Cronograma
        \n
        {read_cronograma_do_projeto}
        \n
        Planilha
        \n
        {read_planilha_json}
        \n
        Documento Pre Projeto 
        \n
        {read_doc_Pre_Projeto}
        """
        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_Dallas, 
                                                                        AI_Dallas_Equipe_de_Solucoes, 
                                                                        model_select,
                                                                        adxitional_instructions_Dallas, key)

        path_Roadmap = os.getenv("PATH_ROADMAP_ENV")
        python_functions.save_TXT(response, path_Roadmap, "w")
        #python_functions.save_json(response, path_name_doc_Pre_Projeto)
        try:
            teste_dict = json.loads(response)

            Roadmap = teste_dict['Roadmap']
            nome_do_Roadmap = teste_dict['nome_do_Roadmap']
            path_nome_do_Roadmap = f"Work_Environment/Create_Roadmap_Projeto/{nome_do_Roadmap}.txt"
            print(Roadmap)
            print(nome_do_Roadmap)

            python_functions.save_TXT(Roadmap, path_nome_do_Roadmap, "w")
            planilha = planilha_json
            return str(path_Roadmap), str(cronograma_do_projeto), str(planilha), str(doc_Pre_Projeto)
        except:
            planilha = planilha_json
            return str(path_Roadmap), str(cronograma_do_projeto), str(planilha), str(doc_Pre_Projeto)
        

