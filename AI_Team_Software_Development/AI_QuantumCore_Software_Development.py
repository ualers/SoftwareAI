
import subprocess
import threading
from CoreApp.SoftwareAI_Core import AutenticateAgent, ResponseAgent, quantumcore_review_pr, python_functions, Agent_files, Github_functions,Agent_files_update
import sys

from AI_Team_Software_Documentation.AI_CloudArchitect_Software_Documentation import Software_Documentation
from AI_Team_Software_Development.AI_SignalMaster_Software_Development import SoftwareDevelopment_SignalMaster
from AI_Team_Software_Development.AI_DataWeaver_Software_Development import software_improvements


# SoftwareAI
class SoftwareDevelopment:

    ##############################################################################################
    def AI_QuantumCore(analysis_txt_path):
        """
        Nome da IA: QuantumCore \n
        Função: Desenvolvedor Pleno em Python \n
        Horario de trabalho: 1H
        
        :param analysis_txt_path: str \n
        :param output: path_to_py
        """   

        instructionQuantumCore = """ 
        Seu nome é QuantumCore, você é um Desenvolvedor Pleno em Python na empresa urobotsoftware. Sua principal responsabilidade é desenvolver software de alta qualidade com base nos requisitos fornecidos pelo Analista de Requisitos de Software e nos padrões de software já existentes na empresa, que foram upados via vectorstore.

        ### Responsabilidades:

        1. **Recepção do Arquivo:**
        - Receber e revisar o arquivo contendo a análise de requisitos de software, que inclui tanto os requisitos funcionais quanto os não funcionais.
        - Assegurar-se de que todos os requisitos estejam claramente documentados e que não existam ambiguidades que possam impactar o desenvolvimento.

        2. **Análise de Requisitos:**
        - Compreender detalhadamente todos os requisitos especificados no documento, incluindo funcionalidades, desempenho, segurança, escalabilidade e outras características críticas do software a ser desenvolvido.
        - Utilizar o **vectorstore** para verificar os padrões já implementados em softwares anteriores da empresa, assegurando a consistência com os requisitos e boas práticas internas.
        - Identificar áreas que necessitem de esclarecimento ou detalhamento adicional e comunicar-se proativamente com o Analista de Requisitos de Software.

        3. **Planejamento do Desenvolvimento:**
        - Dividir os requisitos em tarefas de desenvolvimento claras e gerenciáveis, priorizando-as conforme a complexidade e dependências.
        - Estabelecer um cronograma detalhado para o desenvolvimento das funcionalidades, alinhando-o com o cronograma do projeto fornecido e garantindo a alocação eficiente do tempo e recursos.
        - Selecionar as tecnologias, frameworks e bibliotecas Python mais adequadas para o desenvolvimento, levando em consideração o que já foi utilizado e validado pela empresa, conforme armazenado no **vectorstore**.

        4. **Implementação do Software:**
        - Desenvolver o software de acordo com os requisitos funcionais e não funcionais, aplicando boas práticas de programação Python, incluindo Clean Code, modularidade, reutilização de código e aderência a padrões de codificação (PEP 8).
        - Consultar o **vectorstore** para reutilizar módulos ou padrões existentes, sempre que aplicável, garantindo consistência e eficiência.
        - Implementar testes unitários e de integração para garantir a robustez e qualidade do software durante todo o ciclo de desenvolvimento.
        - Utilizar controle de versão (Git) de maneira eficiente.

        5. **Documentação do Código:**
        - Documentar o código desenvolvido de forma clara e concisa, e manter consistência com a documentação de projetos anteriores, conforme os padrões armazenados no **vectorstore**.
        - Criar e manter documentação técnica abrangente, incluindo arquivos README (.md) e outros documentos relevantes.

        6. **Colaboração com Outros Membros da Equipe:**
        - Trabalhar em colaboração com o Analista de Requisitos, Testadores de Software e outros desenvolvedores, assegurando a aderência aos padrões internos.

        7. **Entrega do Software:**
        - Preparar o software para entrega, incluindo builds finais, criação de pacotes Python e configuração do ambiente de produção, automatizando o processo sempre que possível.

        8. **Resolução de Problemas:**
        - Identificar, diagnosticar e resolver problemas ou bugs durante o desenvolvimento, propondo melhorias baseadas em soluções anteriores armazenadas no **vectorstore**.

        9. **Criação e Upload no GitHub:**
        - Criar um repositório no GitHub para o projeto.
        - Fazer o upload da documentação (.md) e dos arquivos de código Python para o repositório recém-criado, assegurando que a estrutura do repositório esteja organizada e a documentação esteja atualizada.

        ### Formato de Resposta:

        Responda no formato JSON conforme o exemplo abaixo:
        ```json
        {
            "status_do_desenvolvimento": "Progresso conforme o planejado",
            "tarefas_completas": [
                "Implementação da funcionalidade de autenticação de usuários",
                "Criação de testes unitários para o módulo de autenticação",
                "Documentação do código para a funcionalidade de autenticação"
            ],
            "pendencias": [
                "Clarificação necessária para o requisito de segurança adicional",
                "Aprovação do design da API pelo Analista de Requisitos"
            ],
            "proximas_tarefas": [
                "Início da integração com o sistema de pagamentos",
                "Teste de desempenho para a funcionalidade de processamento de pedidos"
            ],
            "observacoes": "Nenhum impedimento significativo até o momento. Desenvolvimento dentro do prazo."
        }
        """
        key = "AI_QuantumCore_Desenvolvedor_Pleno_de_Software_em_Python"
        nameassistant = "AI QuantumCore Desenvolvedor Pleno de Software em Python"
        model_select = "gpt-4o-mini-2024-07-18"

        adxitional_instructions = """
        Clareza e Precisão: Assegure-se de que todos os aspectos do software sejam desenvolvidos com alta precisão e clareza, garantindo que o código seja fácil de entender, manter e expandir.
        \n
        Comunicação Proativa: Mantenha uma comunicação constante e proativa com os outros membros da equipe para resolver dúvidas e evitar mal-entendidos que possam impactar o progresso do projeto.
        \n
        Foco na Qualidade: Priorize a qualidade do código, garantindo que todas as funcionalidades sejam implementadas de maneira eficiente, segura e robusta.
        \n
        Cumprimento de Prazos: Cumpra rigorosamente os prazos estabelecidos no cronograma, e informe qualquer potencial atraso o mais cedo possível, junto com um plano de ação para mitigação.
                
        """
        tools=[
            {"type": "file_search"},
            {
                "type": "function",
                "function": {
                    "name": "create_github_repo_and_upload",
                    "description": "Cria um repositório no GitHub e realiza o upload da documentação (.md) e do código Python.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "repo_name": {
                                "type": "string",
                                "description": "Nome do repositório a ser criado no GitHub."
                            },
                            "repo_description": {
                                "type": "string",
                                "description": "Descrição do repositório."
                            },
                            "readme_file_path": {
                                "type": "string",
                                "description": "Caminho do arquivo .md (README) a ser carregado no repositório."
                            },
                            "code_file_paths": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "description": "Lista de caminhos dos arquivos de código Python a serem carregados no repositório."
                            },
                            "token": {
                                "type": "string",
                                "description": "Token de autenticação do GitHub para realizar operações na API."
                            }
                        },
                        "required": ["repo_name", "repo_description", "readme_file_path", "code_file_paths", "token"]
                    }
                }
            }
        ]
        path_Conhecimentos_python = r"C:\Users\ualer\Downloads\Saas do site\A-I-O-R-G\AI_Team_Software_Development\Conhecimentos_python_em_pdf"
        name_for_vectorstore = "Conhecimentos_python_em_pdf"
        file_path_Conhecimentos_python_em_pdf = [
            f"{path_Conhecimentos_python}/Automate the Boring Stuff with Python.pdf",
            f"{path_Conhecimentos_python}/Effective Python 2nd.pdf",
            f"{path_Conhecimentos_python}/Fluent Python.pdf",
            f"{path_Conhecimentos_python}/pep8-readthedocs-io-en-release-1.7.x.pdf",
            f"{path_Conhecimentos_python}/pep257-readthedocs-io-en-0.6.0.pdf",
            f"{path_Conhecimentos_python}/python_para_desenvolvedores.pdf",
            f"{path_Conhecimentos_python}/python-clean-code-best-practices-and-techniques-for-writing-clear-concise-and-maintainable-code-publishdrivenbsped.pdf",
            f"{path_Conhecimentos_python}/python-cookbook-3rd-edition-9781449357337-1449357334.pdf",
            f"{path_Conhecimentos_python}/python-type-checking-readthedocs-io-en-latest.pdf",
        ]
        list_file_id_Conhecimentos_python_em_pdf = Agent_files.auth_or_upload_multiple_files(name_for_vectorstore, file_path_Conhecimentos_python_em_pdf)
        vector_store_id_conhecimentospython = Agent_files.auth_or_create_vector_store_with_multiple_files(name_for_vectorstore, list_file_id_Conhecimentos_python_em_pdf)


        path_local = r"C:\Users\ualer\Downloads\Saas do site\Youtube Downloader (dev)"
        youtube_downloader_software_name = "youtube_downloader"
        file_path_youtube_downloader_software_in_company = [

            f"{path_local}/main.py",
            f"{path_local}/CoreApp/Securityclass.py",
            f"{path_local}/Update.py",
            f"{path_local}/Update_exe.py", f"{path_local}/Update_Update.py",
            f"{path_local}/YoutubeDownloader.py", f"{path_local}/Enviar_atualizacao.py",
            f"{path_local}/Convert_ui.py", f"{path_local}/uisave/UI_Convert.py",
            #f"{path_local}/uisave/latestchannelstreams.xml", f"{path_local}/uisave/main_window.xml",
            f"{path_local}/CoreApp/ui/latestchannelstreams_ui.py", f"{path_local}/CoreApp/ui/main_window_ui.py"

            
        ]

        path_localTwitch = r"C:\Users\ualer\Downloads\Saas do site\Twitch Downloader (dev)"
        Twitch_downloader_software_name = "Twitch_downloader"
        file_path_Twitch_downloader_software_in_company = [

            f"{path_localTwitch}/main.py",
            f"{path_localTwitch}/CoreApp/Securityclass.py",
            f"{path_localTwitch}/Update.py",
            f"{path_localTwitch}/Update_exe.py", f"{path_localTwitch}/Update_Update.py",
            f"{path_localTwitch}/TwitchDownloader.py", f"{path_localTwitch}/Enviar_atualizacao.py",
            f"{path_localTwitch}/Convert_ui.py", f"{path_localTwitch}/uisave/UI_Convert.py",
            #f"{path_localTwitch}/uisave/mode_all_vod_dialog.xml", f"{path_localTwitch}/uisave/login.xml", f"{path_localTwitch}/uisave/main_window.xml",
            f"{path_localTwitch}/CoreApp/ui/mode_all_vod_dialog_ui.py", f"{path_localTwitch}/CoreApp/ui/main_window_ui.py", f"{path_localTwitch}/CoreApp/ui/login_ui.py"
            
        ]

        vector_store_id_youtube_downloader_software = Agent_files.auth_or_create_vectorstore(youtube_downloader_software_name, file_path_youtube_downloader_software_in_company)
        
        vector_store_id_Twitch_downloader_software = Agent_files.auth_or_create_vectorstore(Twitch_downloader_software_name, file_path_Twitch_downloader_software_in_company)
        

        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None

        github_username, github_token = Github_functions.QuantumCore_github_keys()


        
        AI_QuantumCore = AutenticateAgent.create_or_auth_AI(key, instructionQuantumCore, nameassistant, model_select, tools, vectorstore_in_assistant)
        
        
        #analysis_txt = python_functions.analyze_txt(analysis_txt_path)
        #update_vector_storage_at_assistant_level = analysis_txt_path
        vector_store_id = Agent_files.auth_or_create_vectorstore("Software_Requirements_Analysis", [analysis_txt_path])
        AI_QuantumCore = Agent_files_update.update_vectorstore_in_agent(AI_QuantumCore, [vector_store_id])
        
        mensaxgem = f"crie um script em python com base nos requisitos fornecidos no arquivo"

        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem, Upload_1_file_in_thread, Upload_1_file_in_message, Upload_1_image_for_vision_in_thread, vectorstore_in_Thread, tools, AI_QuantumCore, model_select, adxitional_instructions, key)
        
        path_Software_Development_txt = f"Work_Environment/Software_Development/python_software.txt"
        python_functions.save_TXT(response, path_Software_Development_txt, "w")
        python_software_in_txt = python_functions.analyze_txt(path_Software_Development_txt)


        mensaxgem = f"""corrija todos os erros de sintaxe do codigo asseguir:\n
        {python_software_in_txt}
        """
        format = 'Responda no formato JSON Exemplo: {"codigo": "import..."}'
        path_Software_Development_py = f"Work_Environment/Software_Development/python_software.py"
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        codigo = response["codigo"]
        python_functions.save_python_code(codigo, path_Software_Development_py)




        mensaxgem = f"""crie um nome e descricao para o repositorio desse software no github:\n
        {codigo}
        """
        format = 'Responda no formato JSON Exemplo: {"nome": "nome..."}, {"descricao": "descricao..."}'
        path_Software_Development_py = f"Work_Environment/Software_Development/python_software.py"
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        repo_name = response["nome"]
        repo_description = response["descricao"]


        readme_file_path = Software_Documentation.CloudArchitect_Software_Documentation(path_Software_Development_py)
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
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensaxgem, Upload_1_file_in_thread, Upload_1_file_in_message, Upload_1_image_for_vision_in_thread, vectorstore_in_Thread, tools, AI_QuantumCore, model_select, adxitional_instructions, key)
        print(response)




        # mensaxgem = f"""crie um nome para a branch com pull request do repositorio no github:\n
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


        #file_teste_path = CipherMind_Testing_in_Software_development.AI_CipherMind(script_version_1_path, path_doc)

        #github_username, github_password, github_tokenNexGenCoder = Github_functions.NexGenCoder_github_keys()
        #NexGenCoder_Testing_in_Software_development.AI_NexGenCoder(file_teste_path, repo_owner, repo_name, branch_name,  github_tokenNexGenCoder)
        #flagquantumcore_review_pr = quantumcore_review_pr(repo_owner, repo_name, pr_number)
        #print(flagquantumcore_review_pr)


        return response







