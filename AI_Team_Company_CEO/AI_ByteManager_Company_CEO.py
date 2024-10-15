
import subprocess
import threading
from CoreApp.SoftwareAI_Core import AutenticateAgent, ResponseAgent, Github_functions, python_functions, Agent_files, Agent_files_update
from AI_Team_Company_Managers.AI_MatrixMinder_Company_Managers import Company_Managers
from AI_Team_Pre_Project.AI_Tigrao_Pre_Project import Pre_Project_Document
from AI_Team_Software_Planning.AI_Bob_Software_Planning import Gerente_de_projeto
from AI_Team_Software_Planning.AI_Dallas_Software_Planning import Equipe_De_Solucoes
from AI_Team_Software_Requirements_Analysis.AI_SynthOperator_Software_Requirements_Analysis import Softwareanaysis
from AI_Team_Software_Development.AI_QuantumCore_Software_Development import SoftwareDevelopment

from AI_Team_Testing_in_Software_Development.AI_NexGenCoder_Testing_in_Software_Development import NexGenCoder_Testing_in_Software_development
from AI_Team_Testing_in_Software_Development.AI_CipherMind_Testing_in_Software_Development import CipherMind_Testing_in_Software_development


import asyncio
import json
import discord




class ByteManager:

    ##############################################################################################
    def AI_1_ByteManager_Company_Owners(mensagem):
        """Nome da IA: ByteManager \n
        Função: Dono de Empresa de Software \n
        Horario de trabalho: 2H
        
        """    

        instruction_AI_ByteManager = """ 
        Seu Nome é ByteManager, Voce Faz parte da equipe de Donos da Empresa Urobotsoftware\n
        Suas Responsabilidades Principais São:\n

        Visão Estratégica:\n

        Analisar e interpretar dados de mercado para identificar novas oportunidades de desenvolvimento de software.
        Definir e ajustar a visão e missão da empresa com base em tendências tecnológicas emergentes.\n
        
        Gestão de Projetos:\n

        Supervisionar o progresso dos projetos em todas as etapas do desenvolvimento de software, garantindo que os prazos e metas sejam cumpridos.
        Aprovar ou rejeitar solicitações de novos projetos com base na viabilidade técnica e comercial.\n
        
        Inovação e Crescimento:\n

        Propor e implementar inovações em produtos existentes ou no desenvolvimento de novos produtos.
        Explorar e analisar novos mercados e segmentos para expansão da empresa.\n
        
        Reuniões de Sincronização Regulares:
        Propor reuniões regulares (diárias ou semanais) para que as equipes compartilhem atualizações, desafios e objetivos. 
        Isso ajuda a alinhar todos em torno do progresso e a identificar possíveis obstáculos cedo.

        

        Responda no formato JSON
        Exemplo:
        {"resposta": "resposta ..."}
        \n
        \n
        Voce pode consultar o Manager de Software chamado MatrixMinder, ele é um Manager de Software da empresa Urobotsoftware,

        \n
        As Responsabilidades Principais Dele São:\n

        Coordenação de Projetos:

        Supervisionar e coordenar todas as atividades dos projetos de software, garantindo que as metas sejam alcançadas dentro dos prazos estipulados.
        Facilitar a comunicação entre as equipes de desenvolvimento, design e testes para assegurar a colaboração eficiente.
        \n
        Alocação de Recursos:

        Gerenciar e alocar recursos (tecnológicos e financeiros) de maneira eficaz para otimizar o desempenho dos projetos.
        Priorizar tarefas e determinar a melhor distribuição de workload entre as equipes.
        \n
        Monitoramento de Desempenho:

        Acompanhar o progresso dos projetos em tempo real, utilizando métricas de desempenho para identificar possíveis gargalos ou desvios no cronograma.
        Fornecer feedback contínuo para as equipes com base em análises de desempenho, ajudando a manter os padrões de qualidade elevados.
        \n
        Caso queira consultar o MatrixMinder Responda no formato JSON
        Exemplo:
        {"consultarMatrixMinder": "Pergunta ao MatrixMinder..."}

        

        Caso seja solicitado algum codigo crie uma descricao completa do que foi solicitado e Responda no formato JSON
        Exemplo:
        {"solicitadoalgumcodigo": "descricao..."}


        """
        key = "AI_ByteManager_Company_Owners"
        nameassistant = "AI ByteManager Donos da Empresa Urobotsoftware"
        model_select = "gpt-4o-mini-2024-07-18"
        tools = [{"type": "file_search"}]
        vectorstore_in_assistant = None #[ 
        #             "vs_USBolYuyy7cVXhfBWFToQcaN"
        #         ]
        vectorstore_in_Thread = None

        adxitional_instructions = None
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        Upload_list_for_code_interpreter_in_thread = None


        AI_ByteManager = AutenticateAgent.create_or_auth_AI(key, instruction_AI_ByteManager, nameassistant, model_select, tools, vectorstore_in_assistant)

        mensaxgem = f"""decida oque o usuario esta solicitando com base na mensagem asseguir: {mensagem} \n       
        
        """  

        exemplo = "Caso seja solicitado algum script ou software Responda no formato JSON Exemplo: {'solicitadoalgumcodigo': 'solicitacao...'} "
            
        mensaxgemfinal = mensaxgem + exemplo
        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgemfinal,
                                                                Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                Upload_1_image_for_vision_in_thread, Upload_list_for_code_interpreter_in_thread,
                                                                vectorstore_in_Thread,
                                                                tools,  AI_ByteManager, model_select, adxitional_instructions, key)
        print(response)
        try:
            teste_dict = json.loads(response)
        except:
            teste_dict = response


        if 'resposta' in teste_dict:
            resposta_AI_ByteManager = teste_dict['resposta']
            return resposta_AI_ByteManager
        
        if 'consultarMatrixMinder' in teste_dict:
            pergunta_ao_matrixminder = teste_dict['consultarMatrixMinder']    
            resposta_do_matrixminder = Company_Managers.AI_MatrixMinder_Company_Managers(pergunta_ao_matrixminder)#invoke_matrixminder(pergunta_ao_matrixminder)
            passando_resposta_do_matrixminder = ResponseAgent.ResponseAgent_message_with_assistants(resposta_do_matrixminder,
                                                                    Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                    Upload_1_image_for_vision_in_thread,  Upload_list_for_code_interpreter_in_thread, vectorstore_in_Thread,
                                                                    tools, AI_ByteManager, model_select, adxitional_instructions, key)
            
            resposta_AI_ByteManager_dict = json.loads(passando_resposta_do_matrixminder)
            resposta_AI_ByteManager = resposta_AI_ByteManager_dict['resposta']
            return resposta_AI_ByteManager
        
        if 'solicitadoalgumcodigo' in teste_dict:

            mensaxgem = f"crie uma descricao completa de {mensagem}  "
            AI_ByteManager_response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                    Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                    Upload_1_image_for_vision_in_thread, Upload_list_for_code_interpreter_in_thread, vectorstore_in_Thread,
                                                                    tools,  AI_ByteManager, model_select, adxitional_instructions, key)

            


            teste_dict = json.loads(AI_ByteManager_response)
            pergunta_ao_tigrao = teste_dict['solicitadoalgumcodigo']    


            resposta_do_tigrao_com_doc_pre_projeto = Pre_Project_Document.AI_1_Pre_Project_Document_Writer(pergunta_ao_tigrao)#invoke_tigrao(pergunta_ao_tigrao)



            Uploadfile = resposta_do_tigrao_com_doc_pre_projeto
            path_planilha_Projeto, path_nome_do_cronograma, path_name_doc_Pre_Projeto = Gerente_de_projeto.Bob_Gerente_de_projeto(Uploadfile)
            
            
            path_Roadmap, cronograma_do_projeto, planilha, doc_Pre_Projeto = Equipe_De_Solucoes.Dallas_Equipe_De_Solucoes_Roadmap(path_nome_do_cronograma, path_planilha_Projeto, path_name_doc_Pre_Projeto)
            
            file_paths_to_project = [f"{path_Roadmap}", f"{cronograma_do_projeto}", f"{planilha}", f"{doc_Pre_Projeto}"]
            print(file_paths_to_project)
            vectorstore_id = Agent_files.auth_or_create_vectorstore("project_", file_paths_to_project)
            print(vectorstore_id)
  


            anaysis_in_txt_path = Softwareanaysis.AI_SynthOperator([vectorstore_id])


            
            script_version_1_path = SoftwareDevelopment.AI_QuantumCore(anaysis_in_txt_path)


            #resposta_AI_ByteManager_dict = json.loads(passando_resposta_do_tigrao_para_AI_ByteManager)
        
            #resposta_AI_ByteManager = resposta_AI_ByteManager_dict['resposta']
            


            return script_version_1_path
