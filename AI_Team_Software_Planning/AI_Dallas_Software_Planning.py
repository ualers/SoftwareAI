
import subprocess
import threading
from CoreApp.SoftwareAI_Core import AutenticateAgent, ResponseAgent, python_functions
import sys
import json

# SoftwareAI

class Equipe_De_Solucoes:
        
    def Dallas_Equipe_De_Solucoes_Roadmap(cronograma_do_projeto, planilha_json, doc_Pre_Projeto):
        read_cronograma_do_projeto = python_functions.analyze_txt(cronograma_do_projeto)
        read_planilha_json = python_functions.analyze_csv(planilha_json)
        read_doc_Pre_Projeto = python_functions.analyze_txt(doc_Pre_Projeto)

        """Cria e Retorna o RoadMap"""    
        instruction_agente_1_da_equipe_de_solucoes = """ 
        Seu Nome é Dallas, Voce Faz parte da Equipe de Solucoes da empresa Urobotsoftware, seu objetivo é Planejar um Roadmap do Projeto com base no Cronograma,Planilha e Documento Pre Projeto 

        Responda o Roadmap do Projeto no formato JSON
        Exemplo:
        {"Roadmap": "Roadmap do Projeto ..."}
        {"nome_do_Roadmap": "nome_do_Roadmap_do_projeto ..."}

        """
        
        key = "AI_Dallas_Equipe_de_Solucoes"
        nameassistant = "AI Dallas Equipe de Solucoes"
        model_select = "gpt-4o-mini-2024-07-18"
        # Tools 
        adxitional_instructions = None
        Uploadfile_in_thread = None
        Uploadfile_in_message = None
        tools = None
        vectorstore = None
        # ----------------------------------------------- 
        AI_Dallas_Equipe_de_Solucoes = AutenticateAgent.create_or_auth_AI(key, instruction_agente_1_da_equipe_de_solucoes, nameassistant, model_select, tools, vectorstore)
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
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem, Uploadfile_in_thread, Uploadfile_in_message, AI_Dallas_Equipe_de_Solucoes, model_select, adxitional_instructions, key)
        path_Roadmap = f"Work_Environment/Create_Roadmap_Projeto/documento_Roadmap_do_projeto.txt"
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
        

