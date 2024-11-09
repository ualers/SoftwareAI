
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
        instructionAI_SignalMaster = """
        Seu nome é SignalMaster, você é um Desenvolvedor Sênior em Python na empresa urobotsoftware. Sua principal responsabilidade é receber scripts ou softwares Python desenvolvidos pela equipe e melhorá-los com base nos padrões de desenvolvimento de softwares já em produção na empresa, os quais serão fornecidos via vectorstore.

        ### Objetivo:
        - Analisar e melhorar o código recebido, garantindo que ele siga as melhores práticas de desenvolvimento e esteja alinhado com os padrões de software da urobotsoftware.
        - Usar as informações fornecidas pelo vectorstore para aplicar padrões de código, arquitetura, e otimizações usadas em outros projetos em produção.

        ### Responsabilidades:

        1. **Análise do Software Atual:**
        - Rever o código atual fornecido para entender sua funcionalidade, estrutura, e pontos fracos ou ineficientes.
        - Avaliar o código em termos de desempenho, segurança, escalabilidade e facilidade de manutenção.

        2. **Consultando o Vectorstore:**
        - Consultar os softwares em produção fornecidos pelo vectorstore para extrair padrões de desenvolvimento, arquitetura, estilo de codificação e boas práticas.
        - Identificar melhorias ou otimizações possíveis, inspiradas em projetos anteriores da empresa.

        3. **Aprimoramento do Código:**
        - Melhorar a estrutura e organização do código para garantir modularidade, reutilização e clareza.
        - Otimizar o desempenho, identificando possíveis gargalos e aplicando técnicas eficientes de processamento e manipulação de dados.
        - Implementar melhorias em segurança e robustez do código, com base em padrões já estabelecidos nos projetos em produção.
        - Garantir que o código esteja documentado de maneira clara, seguindo os padrões de documentação da empresa.

        4. **Refatoração e Melhoria Contínua:**
        - Refatorar o código para remover redundâncias e simplificar lógicas complexas sem alterar o comportamento desejado.
        - Garantir que o código esteja aderente às convenções de estilo, como PEP 8, e às boas práticas da empresa.
        - Adicionar comentários explicativos onde necessário, além de garantir que os nomes de variáveis, funções e classes sejam intuitivos e expressivos.

        5. **Integração com Padrões de Produção:**
        - Incorporar tecnologias, bibliotecas ou frameworks que são comumente utilizados pela empresa para garantir padronização entre projetos.
        - Assegurar que o software seja compatível com a infraestrutura de produção existente, utilizando padrões de integração contínua e entrega contínua (CI/CD) já estabelecidos.

        6. **Testes e Validação:**
        - Verificar se o software possui testes adequados, e adicionar ou melhorar a cobertura de testes unitários e de integração.
        - Garantir que os testes sejam compatíveis com as ferramentas e metodologias de teste em uso pela empresa.

        7. **Colaboração com a Equipe:**
        - Trabalhar em conjunto com os desenvolvedores que criaram o software original, fornecendo feedback e sugestões para melhorias futuras.
        - Participar de reuniões de revisão de código e sessões de discussão técnica com outros membros da equipe para garantir que as melhorias propostas sejam compreendidas e implementadas corretamente.

        ### Formato de Resposta:

        Responda no formato JSON conforme o exemplo abaixo:
        {
            "status_do_Desenvolvimento": "...",
            "melhorias_realizadas": [
                "Refatoração do módulo X",
                "Otimização de desempenho no processamento de Y",
                "Adição de testes unitários para a função Z"
            ],
            "observacoes": "..."
        }
        """
        key = "AI_SignalMaster_Desenvolvedor_Pleno_de_Software_em_Python"
        nameassistant = "AI SignalMaster Desenvolvedor Pleno de Software em Python"
        model_select = "gpt-4o-mini-2024-07-18"
        adxitional_instructions = "pyqt5 é a gui que estao nos padroes da empresa"
        tools=[
            {"type": "file_search"},
            {
                "type": "function",
                "function": {
                    "name": "improve_code_and_create_pull_request",
                    "description": "Realiza melhorias no código e cria um pull request no repositório GitHub.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "repo_owner": {
                                "type": "string",
                                "description": "Nome do dono do repositório no GitHub."
                            },
                            "repo_name": {
                                "type": "string",
                                "description": "Nome do repositório no GitHub."
                            },
                            "branch_name": {
                                "type": "string",
                                "description": "Nome da branch onde o código será atualizado."
                            },
                            "file_path": {
                                "type": "string",
                                "description": "Caminho do arquivo no repositório."
                            },
                            "commit_message": {
                                "type": "string",
                                "description": "Mensagem de commit descrevendo as melhorias."
                            },
                            "improvements": {
                                "type": "string",
                                "description": "Novo código melhorado."
                            },
                            "token": {
                                "type": "string",
                                "description": "Token de autenticação do GitHub."
                            }
                        },
                        "required": ["repo_owner", "repo_name", "branch_name", "file_path", "commit_message", "improvements", "token"]
                    }
                }
            }
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

        
        AI_SignalMaster = AutenticateAgent.create_or_auth_AI(key, instructionAI_SignalMaster, nameassistant, model_select, tools, vectorstore_in_assistant)
        
        
        mensaxgem = f"""melhore esse script em python\n
        script:\n
        {python_content}
        """

        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem, Upload_1_file_in_thread, Upload_1_file_in_message, Upload_1_image_for_vision_in_thread, vectorstore_in_Thread, tools, AI_SignalMaster, model_select, adxitional_instructions, key)
        
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
        token:\n
        {github_token}
        """
        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem, Upload_1_file_in_thread, Upload_1_file_in_message, Upload_1_image_for_vision_in_thread, vectorstore_in_Thread, tools, AI_SignalMaster, model_select, adxitional_instructions, key)
       






        #file_teste_path = CipherMind_Testing_in_Software_development.AI_CipherMind(script_version_1_path, path_doc)

        #github_username, github_password, github_tokenNexGenCoder = Github_functions.NexGenCoder_github_keys()
        #NexGenCoder_Testing_in_Software_development.AI_NexGenCoder(file_teste_path, repo_owner, repo_name, branch_name,  github_tokenNexGenCoder)




        return response







