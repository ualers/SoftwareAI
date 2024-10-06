
import subprocess
import threading
from CoreApp.SoftwareAI_Core import AutenticateAgent, ResponseAgent, python_functions
import os
import json
import pandas as pd
from io import StringIO

# SoftwareAI
class Gerente_de_projeto:
        
    ##############################################################################################
    def Bob_Gerente_de_projeto(path_name_doc_Pre_Projeto):

        """Cria o cronograma e planilha"""
        instructionGerente_de_Projeto = """ 
        Seu Nome é Bob, Voce é um Gerente de projeto da empresa Urobotsoftware, seu objetivo é criar um cronograma e planilha do Projeto com base no Documento Pre Projeto

        Responda o cronograma no formato JSON
        Exemplo:
        {"cronograma": "cronograma do Projeto ..."}
        {"nome_do_cronograma": "nome_do_cronograma_do_projeto ..."}


        Responda a planilha do Projeto no formato JSON
        Exemplo:
        {"planilha": "planilha do Projeto ..."}
        {"nome_da_planilha": "nome_da_planilha_do_projeto ..."}

        """
        key = "AI_Bob_Gerente_de_Projeto"
        nameassistant = "AI Bob Gerente de Projeto"
        model_select = "gpt-4o-mini-2024-07-18"
        adxitional_instructions = None
        Uploadfile_in_thread = None
        Uploadfile_in_message = None
        tools = None
        vectorstore = None

        AI_Gerente_de_Projeto = AutenticateAgent.create_or_auth_AI(key, instructionGerente_de_Projeto, nameassistant, model_select, tools, vectorstore)

        doc_Pre_Projeto = python_functions.analyze_txt(path_name_doc_Pre_Projeto)

        mensagem = f"""
        Crie o cronograma do projeto com base no documento pre projeto\n
        
        Documento Pre Projeto
        \n
        {doc_Pre_Projeto}

        """

        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem, Uploadfile_in_thread, Uploadfile_in_message, AI_Gerente_de_Projeto, model_select, adxitional_instructions, key)
        path_nome_do_cronograma = f"Work_Environment/Create_Cronograma_e_planilha_Projeto/documento_cronograma_do_projeto.txt"
        
        python_functions.save_TXT(response, path_nome_do_cronograma, "w")
        #python_functions.save_json(response, path_name_doc_Pre_Projeto)
        try:
            teste_dict = json.loads(response)

            
            cronograma_do_projeto = teste_dict['cronograma']
            nome_do_cronograma = teste_dict['nome_do_cronograma']
            path_nome_do_cronograma = f"Work_Environment/Create_Cronograma_e_planilha_Projeto/{nome_do_cronograma}.txt"
            print(cronograma_do_projeto)
            print(nome_do_cronograma)

            python_functions.save_TXT(cronograma_do_projeto, path_nome_do_cronograma, "w")

            #return path_nome_do_cronograma

        except:
            pass #return path_name_doc_Pre_Projeto

        
        doc_cronograma = python_functions.analyze_txt(path_nome_do_cronograma)
        mensagem = f"""
        Crie a planilha do projeto com base no documento pre projeto e cronograma\n
        
        Documento Pre Projeto
        \n
        {doc_Pre_Projeto}
        \n
        Documento cronograma
        \n
        {doc_cronograma}

        """
        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem, Uploadfile_in_thread, Uploadfile_in_message, AI_Gerente_de_Projeto, model_select, adxitional_instructions, key)
        path_planilha_Projeto = f"Work_Environment/Create_Cronograma_e_planilha_Projeto/documento_planilha_do_projeto.txt"
        python_functions.save_TXT(response, path_planilha_Projeto, "w")
        # try:
        #     # Supondo que o response seja uma string CSV ou JSON
        #     response_io = StringIO(response)
        #     dataframe = pd.read_csv(response_io)  # Ou pd.read_json(response_io) dependendo do formato
            
        #     # Salvar o DataFrame como CSV
        #     path_planilha_Projeto = f"Create_Cronograma_e_planilha_Projeto/documento_planilha_do_projeto.txt"
        #     python_functions.save_csv(dataframe, path_planilha_Projeto)
        # except Exception as e:
        #     print(f"Erro ao processar e salvar o DataFrame: {e}")
        try:
            teste_dict = json.loads(response)

            planilha_json = teste_dict['planilha']
            nome_da_planilha = teste_dict['nome_da_planilha']
            path_nome_da_planilha = f"Work_Environment/Create_Cronograma_e_planilha_Projeto/{nome_da_planilha}.csv"
            print(planilha_json)
            print(nome_da_planilha)

            python_functions.save_csv(planilha_json, path_nome_da_planilha)
            return path_planilha_Projeto, path_nome_do_cronograma, path_name_doc_Pre_Projeto
        except:
            print("planilha e cronograma foram criados ")
            return path_planilha_Projeto, path_nome_do_cronograma, path_name_doc_Pre_Projeto



