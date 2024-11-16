
#########################################
# IMPORT SoftwareAI Core
from ..._init_core_ import *
#########################################
# IMPORT SoftwareAI Libs 
from ..._init_libs_ import *
#########################################
# IMPORT SoftwareAI Instructions
from ...SoftwareAI.Instructions._init_Instructions_ import *
#########################################
# IMPORT SoftwareAI Tools
from ...SoftwareAI.Tools._init_tools_ import *
#########################################


class SoftwareDevelopment:
    def __init__(self, Software_Documentation,
                SoftwareImprovements_DataWeaver,
                SoftwareDevelopment_SignalMaster,
                SoftwareDevelopment_NexGenCoder):
        
        self.Software_Documentation = Software_Documentation
        self.SoftwareImprovements_DataWeaver = SoftwareImprovements_DataWeaver
        self.SoftwareDevelopment_SignalMaster = SoftwareDevelopment_SignalMaster
        self.SoftwareDevelopment_NexGenCoder = SoftwareDevelopment_NexGenCoder

    ##############################################################################################
    def AI_QuantumCore(
                    self,
                    timeline_file_path,
                    spreadsheet_file_path,
                    pre_project_file_path,
                    Roadmap_file_path,
                    analysis_txt_path
                    
                    ):
        """
        Nome da IA: QuantumCore \n
        Função: Desenvolvedor Pleno em Python \n
        Horario de trabalho: 1H
        
        :param analysis_txt_path: str \n
        :param output: path_to_py
        """   

        key = "AI_QuantumCore_Desenvolvedor_Pleno_de_Software_em_Python"
        nameassistant = "AI QuantumCore Desenvolvedor Pleno de Software em Python"
        model_select = "gpt-4o-mini-2024-07-18"




        
        # path_Conhecimentos_python = r"C:\Users\ualer\Downloads\Saas do site\A-I-O-R-G\AI_Team_Software_Development\Conhecimentos_python_em_pdf"
        # name_for_vectorstore = "Conhecimentos_python_em_pdf"
        # file_path_Conhecimentos_python_em_pdf = [
        #     f"{path_Conhecimentos_python}/Automate the Boring Stuff with Python.pdf",
        #     f"{path_Conhecimentos_python}/Effective Python 2nd.pdf",
        #     f"{path_Conhecimentos_python}/Fluent Python.pdf",
        #     f"{path_Conhecimentos_python}/pep8-readthedocs-io-en-release-1.7.x.pdf",
        #     f"{path_Conhecimentos_python}/pep257-readthedocs-io-en-0.6.0.pdf",
        #     f"{path_Conhecimentos_python}/python_para_desenvolvedores.pdf",
        #     f"{path_Conhecimentos_python}/python-clean-code-best-practices-and-techniques-for-writing-clear-concise-and-maintainable-code-publishdrivenbsped.pdf",
        #     f"{path_Conhecimentos_python}/python-cookbook-3rd-edition-9781449357337-1449357334.pdf",
        #     f"{path_Conhecimentos_python}/python-type-checking-readthedocs-io-en-latest.pdf",
        # ]
        # list_file_id_Conhecimentos_python_em_pdf = Agent_files.auth_or_upload_multiple_files(name_for_vectorstore, file_path_Conhecimentos_python_em_pdf)
        # vector_store_id_conhecimentospython = Agent_files.auth_or_create_vector_store_with_multiple_files(name_for_vectorstore, list_file_id_Conhecimentos_python_em_pdf)


        # path_local = r"C:\Users\ualer\Downloads\Saas do site\Youtube Downloader (dev)"
        # youtube_downloader_software_name = "youtube_downloader"
        # file_path_youtube_downloader_software_in_company = [

        #     f"{path_local}/main.py",
        #     f"{path_local}/CoreApp/Securityclass.py",
        #     f"{path_local}/Update.py",
        #     f"{path_local}/Update_exe.py", f"{path_local}/Update_Update.py",
        #     f"{path_local}/YoutubeDownloader.py", f"{path_local}/Enviar_atualizacao.py",
        #     f"{path_local}/Convert_ui.py", f"{path_local}/uisave/UI_Convert.py",
        #     #f"{path_local}/uisave/latestchannelstreams.xml", f"{path_local}/uisave/main_window.xml",
        #     f"{path_local}/CoreApp/ui/latestchannelstreams_ui.py", f"{path_local}/CoreApp/ui/main_window_ui.py"

            
        # ]

        # path_localTwitch = r"C:\Users\ualer\Downloads\Saas do site\Twitch Downloader (dev)"
        # Twitch_downloader_software_name = "Twitch_downloader"
        # file_path_Twitch_downloader_software_in_company = [

        #     f"{path_localTwitch}/main.py",
        #     f"{path_localTwitch}/CoreApp/Securityclass.py",
        #     f"{path_localTwitch}/Update.py",
        #     f"{path_localTwitch}/Update_exe.py", f"{path_localTwitch}/Update_Update.py",
        #     f"{path_localTwitch}/TwitchDownloader.py", f"{path_localTwitch}/Enviar_atualizacao.py",
        #     f"{path_localTwitch}/Convert_ui.py", f"{path_localTwitch}/uisave/UI_Convert.py",
        #     #f"{path_localTwitch}/uisave/mode_all_vod_dialog.xml", f"{path_localTwitch}/uisave/login.xml", f"{path_localTwitch}/uisave/main_window.xml",
        #     f"{path_localTwitch}/CoreApp/ui/mode_all_vod_dialog_ui.py", f"{path_localTwitch}/CoreApp/ui/main_window_ui.py", f"{path_localTwitch}/CoreApp/ui/login_ui.py"
            
        # ]

        # vector_store_id_youtube_downloader_software = Agent_files.auth_or_create_vectorstore(youtube_downloader_software_name, file_path_youtube_downloader_software_in_company)
        
        # vector_store_id_Twitch_downloader_software = Agent_files.auth_or_create_vectorstore(Twitch_downloader_software_name, file_path_Twitch_downloader_software_in_company)
        
        read_analysis_txt_path = python_functions.analyze_txt(analysis_txt_path)


        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None
        Upload_list_for_code_interpreter_in_thread = None

        github_username, github_token = Github_functions.QuantumCore_github_keys()

        AI_QuantumCore = AutenticateAgent.create_or_auth_AI(key, instructionQuantumCore, nameassistant, model_select, tools_QuantumCore, vectorstore_in_assistant)
        
        #analysis_txt = python_functions.analyze_txt(analysis_txt_path)
        #update_vector_storage_at_assistant_level = analysis_txt_path
        #vector_store_id = Agent_files.auth_or_create_vectorstore("Software_Requirements_Analysis", [analysis_txt_path])
       #AI_QuantumCore = Agent_files_update.update_vectorstore_in_agent(AI_QuantumCore, [vector_store_id])
        
        mensaxgem = f"""crie um script em python com base nos requisitos fornecidos no arquivo\n
        
        analysis
        {read_analysis_txt_path}
        """

        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread,
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread, 
                                                                        tools_QuantumCore,
                                                                        AI_QuantumCore, 
                                                                        model_select,
                                                                        adxitional_instructions_QuantumCore,
                                                                        key
                                                                            
                                                                    )
        
        path_Software_Development_txt =  os.getenv("PATH_SOFTWARE_DEVELOPMENT_TXT_ENV")
        python_functions.save_TXT(response, path_Software_Development_txt, "w")
        python_software_in_txt = python_functions.analyze_txt(path_Software_Development_txt)


        mensaxgem = f"""corrija todos os erros de sintaxe do codigo asseguir :\n
        {python_software_in_txt}
        """
        regras = "\ncaso nao haja erros de sintaxe retorne o codigo\n"
        format = 'Responda no formato JSON Exemplo: {"codigo": "import..."}'
        path_Software_Development_py = os.getenv("PATH_SOFTWARE_DEVELOPMENT_PY_ENV")
        mensagem = mensaxgem + regras + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        codigo = response["codigo"]
        python_functions.save_python_code(codigo, path_Software_Development_py)




        mensaxgem = f"""crie um nome e descricao para o repositorio desse software no github:\n
        {codigo}
        """
        regras = "Descrição do Repositório NÃO exceder o limite de 350 caracteres"
        format = 'Responda no formato JSON Exemplo: {"nome": "nome..."}, {"descricao": "descricao..."}'
        
        mensagem = mensaxgem + regras + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        try:
            repo_name = response["nome"]
            repo_description = response["descricao"]
        except Exception as errror2:
            print(errror2)
            print(response)

        from dotenv import load_dotenv
        load_dotenv(dotenv_path=r"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\ambiente.env")

        path_Software_Development_py = os.getenv("PATH_SOFTWARE_DEVELOPMENT_PY_ENV")
        path_Analysis = os.getenv("PATH_ANALISE_ENV")
        path_Roadmap = os.getenv("PATH_ROADMAP_ENV")
        path_Spreadsheet = os.getenv("PATH_PLANILHA_PROJETO_ENV")
        path_Timeline = os.getenv("PATH_NOME_DO_CRONOGRAMA_ENV")
        path_Preproject = os.getenv("PATH_NAME_DOC_PRE_PROJETO_ENV")
        path_DOCUMENTACAO_ENV = os.getenv("PATH_DOCUMENTACAO_ENV")
        

        readme_file_path = self.Software_Documentation.CloudArchitect_Software_Documentation_Type_Create(path_Software_Development_py, path_Analysis, path_Roadmap, path_Spreadsheet, path_Timeline, path_Preproject)
        code_file_paths = [path_Software_Development_py]

        mensaxgem = f"""Cria um repositório no GitHub e realiza o upload da documentação (.md) e do código Python.\n
        repo_name:\n
        {repo_name}\n
        repo_description:\n
        {repo_description}\n
        readme_file_path:\n
        {readme_file_path}\n
        code_file_paths:\n
        {code_file_paths}\n
        token:\n
        {github_token}\n
        """
        #format = 'Responda no formato JSON Exemplo: {"nome": "nome..."}'
        #mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_QuantumCore, 
                                                                        AI_QuantumCore, 
                                                                        model_select,
                                                                        adxitional_instructions_QuantumCore, key)
        print(response)



        mensaxgem = f"""Realiza o upload dos arquivos do projeto, incluindo documentação, timeline, roadmap e análises.\n
        repo_name:\n
        {repo_name}\n
        timeline_file_path:\n
        {timeline_file_path}\n
        spreadsheet_file_path:\n
        {spreadsheet_file_path}\n
        pre_project_file_path:\n
        {pre_project_file_path}\n
        Roadmap_file_path:\n
        {Roadmap_file_path}\n
        analise_file_path:\n
        {analysis_txt_path}\n
        token:\n
        {github_token}\n
        """
        #format = 'Responda no formato JSON Exemplo: {"nome": "nome..."}'
        #mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_QuantumCore, 
                                                                        AI_QuantumCore, 
                                                                        model_select,
                                                                        adxitional_instructions_QuantumCore, key)
        print(response)

        code_python_software_old = python_functions.analyze_txt(os.getenv("PATH_SOFTWARE_DEVELOPMENT_PY_ENV"))
        save_code_old = codigo
        pr_number = 1
        branch_name = f"main_1"
        for i in range(5):
            branch_name = f"main_{i + 1}"
            

            path_Software_Development_py = os.getenv("PATH_SOFTWARE_DEVELOPMENT_PY_ENV")

            flag_improvements = self.SoftwareImprovements_DataWeaver.AI_DataWeaver_improvements(path_Software_Development_py, "", "")
            print(flag_improvements)

            flag_SoftwareDevelopment_SignalMaster = self.SoftwareDevelopment_SignalMaster.AI_SignalMaster(path_Software_Development_py, repo_name, branch_name)
            print(flag_SoftwareDevelopment_SignalMaster)

            flag_SoftwareDevelopment_NexGenCoder = self.SoftwareDevelopment_NexGenCoder.AI_NexGenCoder(repo_name, pr_number)
            print(flag_SoftwareDevelopment_NexGenCoder)
            
            
            path_python_software_new = python_functions.analyze_txt(path_Software_Development_py)

            readme_file_path_improvements = self.Software_Documentation.CloudArchitect_Software_Documentation_Type_Update(repo_name, path_DOCUMENTACAO_ENV, code_python_software_old, path_python_software_new, path_Analysis, path_Roadmap, path_Spreadsheet, path_Timeline, path_Preproject)

            code_python_software_old = python_functions.analyze_txt(path_Software_Development_py)

        # mensaxgem = f"""crie um nome para a branch de 10 caracteres do pull request do repositorio no github:\n
        # repositorio:\n
        # {repo_name}\n
        # repo_description:\n
        # {repo_description}\n
        # """
        # format = 'Responda no formato JSON Exemplo: {"branch_name": "branch name..."}'
        # mensagem = mensaxgem + format
        # response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        # branch_name = response["branch_name"]
        # repo_owner = "A-I-O-R-G"

        # flagAI_DataWeaver_improvements = software_improvements.AI_DataWeaver_improvements(path_Software_Development_py, repo_name, branch_name)
        # print(flagAI_DataWeaver_improvements)


        # file_teste_path = CipherMind_Testing_in_Software_development.AI_CipherMind(script_version_1_path, path_doc)

        # github_username, github_password, github_tokenNexGenCoder = Github_functions.NexGenCoder_github_keys()
        # NexGenCoder_Testing_in_Software_development.AI_NexGenCoder(file_teste_path, repo_owner, repo_name, branch_name,  github_tokenNexGenCoder)
        # flagquantumcore_review_pr = quantumcore_review_pr(repo_owner, repo_name, pr_number)
        # print(flagquantumcore_review_pr)


        # return response







