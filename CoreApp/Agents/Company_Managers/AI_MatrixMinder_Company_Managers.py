
#########################################
# IMPORT SoftwareAI Core
from ..._init_core_ import *
#########################################
# IMPORT SoftwareAI Agents 
from ..._init_agents_ import *
#########################################
# IMPORT SoftwareAI Libs 
from ..._init_libs_ import *
#########################################



class Company_Managers:
        
    def AI_MatrixMinder_Company_Managers(self, mensaagem, Analysis_txt, file_path_py, Roadmap_txt, Documentation_md, Project_spreadsheet_txt):
        
        # Analysis_txt = python_functions.analyze_txt(Analysis_txt)
        # file_path_py = python_functions.analyze_txt(file_path_py)
        # Roadmap_txt = python_functions.analyze_txt(Roadmap_txt)
        # Documentation_md = python_functions.analyze_txt(Documentation_md)
        # Project_spreadsheet_txt = python_functions.analyze_txt(Project_spreadsheet_txt)



        """Nome da IA: MatrixMinder\n
            Função: Manager de Software"""    


        instruction_MatrixMinder = """ 
     
        Seu nome é MatrixMinder, você é o Manager de Software da empresa Urobotsoftware. Sua principal responsabilidade é receber e analisar os arquivos enviados por Byte Manager, o CEO da Urobotsoftware, que representam solicitações de atualização de software.

        Seu objetivo é verificar se o que foi solicitado é uma atualização . Caso seja, você deve aprovar a requisição de atualização

        Formato de Resposta:
        Responda no formato JSON.

        """
        key = "AI_MatrixMinder_Manager_de_Software"
        nameassistant = "AI MatrixMinder Manager de Software"
        model_select = "gpt-4o-mini"
        adxitional_instructions = None
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None
        
        Upload_list_for_code_interpreter_in_thread = None
        # Upload_list_for_code_interpreter_in_thread = [
        #     Analysis_txt,
        #     file_path_py,
        #     Roadmap_txt,
        #     Documentation_md,
        #     Project_spreadsheet_txt
        # ]
        tools = [
                 {"type": "file_search"}
                ]
        MatrixMinderAnálxise = "MatrixMinderAnálise"
        file_path_MatrixMinderAnálise = [
            Analysis_txt,
            file_path_py,
            Roadmap_txt,
            Documentation_md,
            Project_spreadsheet_txt
        ]
        print(file_path_MatrixMinderAnálise)
        vector_store_id_MatrixMinderAnálise = Agent_files.auth_or_create_vectorstore(MatrixMinderAnálxise, file_path_MatrixMinderAnálise)
        vectorstore_in_Thread = vector_store_id_MatrixMinderAnálise

        AI_MatrixMinder = AutenticateAgent.create_or_auth_AI(key, instruction_MatrixMinder, nameassistant, model_select, tools, vectorstore_in_assistant)

        mensaxgem = f"""
        decidir se oque foi solicitado na mensagem é uma atualizacao: {mensaagem}
        \n

        """
        AI_ByteManager_response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                Upload_1_image_for_vision_in_thread, Upload_list_for_code_interpreter_in_thread,
                                                                vectorstore_in_Thread,
                                                                tools,  AI_MatrixMinder, model_select, adxitional_instructions, key)
        try:
            resposta = AI_ByteManager_response['resposta']
        except:
            resposta = AI_ByteManager_response

        print(resposta)


        return resposta







