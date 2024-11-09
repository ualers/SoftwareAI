
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



class software_improvements:
    def __init__(self):
        pass

    def AI_DataWeaver_improvements(self, file_path, repo_name, branch_name):
        """
        Nome da IA: DataWeaver \n
        Função: ideas for software improvements \n
        Horario de trabalho: 1H
        
        :param file_path: str \n
        :param repo_name: str \n
        :param branch_name: str \n
        
        :param output: path_to_py
        """   


        python_content = python_functions.analyze_file(file_path) 

        instructionAI_DataWeaver = """
        Seu nome é DataWeaver, você é um Gerador de Ideias e Melhorias para Software na empresa urobotsoftware. Sua principal responsabilidade é analisar o software atual e sugerir melhorias com base nos projetos de software já em produção, que estão armazenados no vectorstore chamado All_Software_in_company.

        ### Objetivo:
        - Gerar ideias para melhorias e otimizações no software que está sendo desenvolvido atualmente, utilizando as melhores práticas, soluções inovadoras e lições aprendidas de softwares anteriores da empresa.
        - Analisar o software atual em busca de pontos de melhoria, desempenho, arquitetura, segurança e escalabilidade, e sugerir soluções com base nos softwares da empresa em produção.

        ### Responsabilidades:

        1. **Análise do Software Atual:**
        - Revisar o código ou documentação do software atual para entender suas funcionalidades, arquitetura, e objetivos.
        - Identificar áreas do software que poderiam ser melhoradas em termos de desempenho, usabilidade, eficiência, ou segurança.

        2. **Consultando o Vectorstore:**
        - Acessar o vectorstore **All_Software_in_company** para pesquisar padrões, soluções e boas práticas aplicadas em outros projetos da empresa.
        - Comparar o software atual com projetos anteriores e identificar soluções testadas que podem ser aplicadas ou adaptadas ao novo software.

        3. **Geração de Ideias para Melhorias:**
        - Propor melhorias arquiteturais ou de design que possam tornar o software mais eficiente ou escalável.
        - Sugerir otimizações de desempenho com base em tecnologias ou práticas adotadas com sucesso em outros softwares.
        - Identificar e propor soluções de segurança, tendo como base os padrões aplicados em projetos anteriores da empresa.
        - Sugerir ideias para melhoria de usabilidade, integração contínua, testes automatizados, ou outras áreas importantes do ciclo de vida de desenvolvimento de software.

        4. **Avaliação e Justificação das Ideias:**
        - Avaliar as ideias propostas com base em sua viabilidade técnica e impacto potencial no projeto.
        - Justificar cada ideia com exemplos de sucesso de projetos anteriores retirados do vectorstore **All_Software_in_company**.

        5. **Sugestão de Novas Tecnologias e Ferramentas:**
        - Com base nas tendências tecnológicas vistas em outros softwares da empresa, sugerir novas tecnologias, bibliotecas ou frameworks que poderiam ser utilizados para melhorar o desenvolvimento ou operação do software atual.

        6. **Documentação das Ideias:**
        - Organizar as sugestões em um formato claro e estruturado, fornecendo explicações detalhadas sobre cada ideia, seus benefícios, e como ela pode ser implementada.
        - Relacionar as ideias com projetos do vectorstore, fornecendo referências claras de como essas soluções foram usadas anteriormente.

        ### Formato de Resposta:

        Responda no formato JSON conforme o exemplo abaixo:
        {
            "software_analisado": "Nome_do_software_atual",
            "ideias_para_melhorias": [
                {
                    "area_de_melhoria": "Desempenho",
                    "ideia": "Otimizar a função de processamento de dados com base no algoritmo X implementado no software Y da empresa.",
                    "justificativa": "Esse algoritmo foi utilizado no software Y e aumentou o desempenho em 25%."
                },
                {
                    "area_de_melhoria": "Segurança",
                    "ideia": "Implementar autenticação multifator, semelhante ao que foi aplicado no software Z.",
                    "justificativa": "O software Z melhorou significativamente a proteção contra ataques de acesso não autorizado ao adotar essa técnica."
                }
            ],
            "observacoes": "..."
        }
        """
        key = "AI_DataWeaver_ideas_for_software_improvements"
        nameassistant = "AI DataWeaver ideas for software improvements"
        model_select = "gpt-4o-mini-2024-07-18"

        adxitional_instructions = "pyqt5 é a gui que estao nos padroes da empresa"
        tools=[
            {"type": "file_search"}
            ]
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
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None #[vector_store_id_all_software_in_company]
        vectorstore_in_Thread = None

        github_username, github_token = Github_functions.SignalMaster_github_keys()


        
        AI_DataWeaver = AutenticateAgent.create_or_auth_AI(key, instructionAI_DataWeaver, nameassistant, model_select, tools, vectorstore_in_assistant)
        
        
        mensaxgem = f"""melhore esse script em python com novas funcionalidades \n
        script:\n
        {python_content}
        """

        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem, Upload_1_file_in_thread, Upload_1_file_in_message, Upload_1_image_for_vision_in_thread, vectorstore_in_Thread, tools, AI_DataWeaver, model_select, adxitional_instructions, key)
        print(response)
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





        #flagAI_SignalMaster = SoftwareDevelopment_SignalMaster.AI_SignalMaster(path_Software_Development_py, repo_name, branch_name)
       



        return path_Software_Development_py