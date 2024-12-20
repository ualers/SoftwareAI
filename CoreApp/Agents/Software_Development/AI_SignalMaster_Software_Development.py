
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



class SoftwareDevelopment_SignalMaster:
    def __init__(self):
        pass

    ##############################################################################################
    def AI_SignalMaster(self, python_file_path, repo_name: str, branch_name: str, analisyspng=None):
        python_content = python_functions.analyze_file(python_file_path)
        """
        Nome da IA: SignalMaster \n
        Função: Desenvolvedor Pleno em Python \n
        Horario de trabalho: 1H
        
        :param analysis_txt_path: str \n
        :param output: path_to_py
        """   

        key = "AI_SignalMaster_Desenvolvedor_Pleno_de_Software_em_Python"
        nameassistant = "AI SignalMaster Desenvolvedor Pleno de Software em Python"
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


        # path_localYoutube = r"C:\Users\ualer\Downloads\Saas do site\Youtube Downloader (dev)"
        # path_localTwitch = r"C:\Users\ualer\Downloads\Saas do site\Twitch Downloader (dev)"
        # all_software_name = "All_Software_in_company"
        # file_path_all_software_in_company = [

        #     f"{path_localTwitch}/main_Twitch_Downloader.py",
        #     f"{path_localTwitch}/CoreApp/Securityclass_Twitch_Downloader.py",
        #     f"{path_localTwitch}/Update_Twitch_Downloader.py",
        #     f"{path_localTwitch}/Update_exe_Twitch_Downloader.py", f"{path_localTwitch}/Update_Update_Twitch_Downloader.py",
        #     f"{path_localTwitch}/TwitchDownloader.py", f"{path_localTwitch}/Enviar_atualizacao_Twitch_Downloader.py",
        #     f"{path_localTwitch}/Convert_ui_Twitch_Downloader.py", f"{path_localTwitch}/uisave/UI_Convert_Twitch_Downloader.py",
        #     #f"{path_localTwitch}/uisave/mode_all_vod_dialog.xml", f"{path_localTwitch}/uisave/login.xml", f"{path_localTwitch}/uisave/main_window.xml",
        #     f"{path_localTwitch}/CoreApp/ui/mode_all_vod_dialog_ui_Twitch_Downloader.py",
        #     f"{path_localTwitch}/CoreApp/ui/main_window_ui_Twitch_Downloader.py", f"{path_localTwitch}/CoreApp/ui/login_ui_Twitch_Downloader.py",
           
        #     f"{path_localYoutube}/main_Youtube_Downloader.py",
        #     f"{path_localYoutube}/CoreApp/Securityclass_Youtube_Downloader.py",
        #     f"{path_localYoutube}/Update_Youtube_Downloader.py",
        #     f"{path_localYoutube}/Update_exe_Youtube_Downloader.py", f"{path_localYoutube}/Update_Update_Youtube_Downloader.py",
        #     f"{path_localYoutube}/YoutubeDownloader.py", f"{path_localYoutube}/Enviar_atualizacao_Youtube_Downloader.py",
        #     f"{path_localYoutube}/Convert_ui_Youtube_Downloader.py", f"{path_localYoutube}/uisave/UI_Convert_Youtube_Downloader.py",
        #     #f"{path_local}/uisave/latestchannelstreams.xml", f"{path_local}/uisave/main_window.xml",
        #     f"{path_localYoutube}/CoreApp/ui/latestchannelstreams_ui_Youtube_Downloader.py", f"{path_localYoutube}/CoreApp/ui/main_window_ui_Youtube_Downloader.py"

        # ]

        # vector_store_id_all_software_in_company = Agent_files.auth_or_create_vectorstore(all_software_name, file_path_all_software_in_company)


        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_list_for_code_interpreter_in_thread = None
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None #[vector_store_id_all_software_in_company]
        vectorstore_in_Thread = None

        github_username, github_token = GithubKeys.SignalMaster_github_keys()

        
        AI_SignalMaster = AutenticateAgent.create_or_auth_AI(key, instructionSignalMaster, nameassistant, model_select, tools_SignalMaster, vectorstore_in_assistant)
        
        
        mensaxgem = f"""melhore esse script em python\n
        script:\n
        {python_content}
        """

        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_SignalMaster, 
                                                                        AI_SignalMaster, 
                                                                        model_select,
                                                                        adxitional_instructions_DataWeaver, key)


        
        path_Software_Development_txt = os.getenv("PATH_SOFTWARE_DEVELOPMENT_TXT_ENV")
        python_functions.save_TXT(response, path_Software_Development_txt, "w")
        python_software_in_txt = python_functions.analyze_txt(path_Software_Development_txt)


        mensaxgem = f"""corrija todos os erros de sintaxe do codigo asseguir:\n
        {python_software_in_txt}\n
        caso nao tenha erros de sintaxe retorne o codigo 
        """
        format = 'Responda no formato JSON Exemplo: {"codigo": "import..."}'
        path_Software_Development_py = os.getenv("PATH_SOFTWARE_DEVELOPMENT_PY_ENV")
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        codigo = response["codigo"]
        python_functions.save_python_code(codigo, path_Software_Development_py)




        mensaxgem = f"""crie uma mensagem de commit para o pull request no github do codigo asseguir descrevendo as melhorias feitas:\n
        codigo melhorado:\n
        {codigo}\n
        codigo antigo:\n
        {python_content}
       
        """
        
        format = 'Responda no formato JSON Exemplo: {"mensagem": "mensagem de commit para o pull request..."}'
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        commit_message = response["mensagem"]
        

        title_prompt = f"""Crie um título para um pull request no GitHub com base no código e na mensagem de commit:
        código:
        {codigo}
        commit_message:
        {commit_message}
        """
        format = 'Responda no formato JSON Exemplo: {"nome_para_pr": "nome do pull request..."}'
        title_message = title_prompt + format
        response = ResponseAgent.ResponseAgent_message_completions(title_message, "", True)
        pr_title = response.get("nome_para_pr", "Título do Pull Request")

        
        mensaxgem = f"""Realize melhorias no código e cria um pull request no repositório GitHub.\n
        repo_owner:\n
        A-I-O-R-G
        repo_name:\n
        {repo_name}\n
        branch_name:\n
        {branch_name}\n
        file_path:\n
        {path_Software_Development_py}\n
        commit_message:\n
        {commit_message}\n
        improvements:\n
        {codigo}\n
        pr_title:\n
        {pr_title}
        token:\n
        {github_token}
        """
        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_SignalMaster, 
                                                                        AI_SignalMaster, 
                                                                        model_select,
                                                                        adxitional_instructions_DataWeaver, key)
       






        #file_teste_path = CipherMind_Testing_in_Software_development.AI_CipherMind(script_version_1_path, path_doc)

        #github_username, github_password, github_tokenNexGenCoder = Github_functions.NexGenCoder_github_keys()
        #NexGenCoder_Testing_in_Software_development.AI_NexGenCoder(file_teste_path, repo_owner, repo_name, branch_name,  github_tokenNexGenCoder)




        return response







