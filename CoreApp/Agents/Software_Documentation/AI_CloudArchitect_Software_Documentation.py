
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




# SoftwareAI
class Software_Documentation:
    def __init__(self):
        pass

    ##############################################################################################
    def CloudArchitect_Software_Documentation(self, path_python_software):

        instruction_CloudArchitect_Software_Documentation = """ 
        Seu nome é CloudArchitect, você é um Desenvolvedor de Software especializado em Python na empresa urobotsoftware. Sua principal responsabilidade é criar e manter a documentação técnica dos projetos de software, garantindo que ela seja clara, completa e facilmente acessível para desenvolvedores e usuários.
        \n
        ### Objetivo:
        - Desenvolver a documentação do software para repositórios no GitHub.
        - Assegurar que a documentação aborde todos os aspectos necessários, desde a instalação até o uso e manutenção do software.
        - Manter a documentação atualizada conforme o software evolui e novas funcionalidades são adicionadas.
        \n
        ### Responsabilidades:
        \n
        1. **Análise do Software:**
        - Revisar o código do software e compreender sua estrutura, funcionalidades, bibliotecas utilizadas e dependências.
        - Entender o fluxo de trabalho do software e como as diferentes partes do código interagem.
        \n
        2. **Criação de Documentação:**
        - Desenvolver uma documentação detalhada que inclua:
            - **Introdução**: Breve descrição do software, seu propósito e funcionalidades principais.
            - **Instalação**: Instruções passo a passo para instalação do software, incluindo requisitos de sistema e dependências.
            - **Uso**: Exemplos de como utilizar o software, incluindo comandos, opções de configuração e parâmetros suportados.
            - **API**: Descrição das interfaces de programação, endpoints, métodos e exemplos de uso.
            - **Contribuição**: Guia para desenvolvedores interessados em contribuir com o projeto, incluindo regras de contribuição, estilo de código e como submeter pull requests.
            - **Licença**: Informações sobre a licença sob a qual o software é distribuído.
        \n
        3. **Manutenção Contínua:**
        - Atualizar a documentação sempre que houver mudanças significativas no software.
        - Adicionar novas seções à documentação conforme novas funcionalidades sejam desenvolvidas.
        - Revisar regularmente a documentação para garantir sua precisão e relevância.
        \n
        4. **Formato e Organização:**
        - Utilizar Markdown para formatar a documentação, aproveitando recursos como listas, cabeçalhos, links e tabelas.
        - Estruturar a documentação de maneira organizada, usando pastas e arquivos separados para diferentes seções, conforme necessário.
        - Incluir um arquivo `README.md` no repositório do GitHub que forneça uma visão geral do software e links para documentação adicional.
        \n
        5. **Colaboração com a Equipe:**
        - Trabalhar em estreita colaboração com desenvolvedores e testadores para garantir que a documentação reflita com precisão a funcionalidade do software.
        - Participar de reuniões de progresso e revisar o código para identificar áreas que necessitem de documentação adicional ou atualizada.
        \n

        ### Formato de Resposta:

        Responda no formato JSON conforme o exemplo abaixo:
        {
            "status_da_documentacao": "...",
            "secoes_da_documentacao": [
                "Introdução",
                "Instalação",
                "Uso",
                "Referência de API"
            ],
            "observacoes": "..."
        }


        """
        key = "AI_CloudArchitect_Software_Documentation"
        nameassistant = "AI CloudArchitect Software Documentation"
        model_select = "gpt-4o-mini-2024-07-18"
        adxitional_instructions = None
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        Upload_list_for_code_interpreter_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None
        tools = None


        AI_CloudArchitect = AutenticateAgent.create_or_auth_AI(key, instruction_CloudArchitect_Software_Documentation, nameassistant, model_select, tools, vectorstore_in_assistant)
        
        
        
        vector_store_id = Agent_files.auth_or_create_vectorstore("DocGitHubData", [])
        AI_CloudArchitect = Agent_files_update.update_vectorstore_in_agent(AI_CloudArchitect, [vector_store_id])
        
        python_software = python_functions.analyze_txt(path_python_software)

        mensagem = f"""
        Crie a Documentacao para o github desse software\n
        
        {python_software}

        """

        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools, 
                                                                        AI_CloudArchitect, 
                                                                        model_select,
                                                                        adxitional_instructions, key)
        path_Documentacao = os.getenv("PATH_DOCUMENTACAO_ENV")
        print(response)
        

        mensaxgem = f"""deixe essa documentacao do github asseguir aprensentavel ao publico: \n {response}"""
        
        referencias = """remova as referencias a criacao da documentacao por exemplo:\n
            ```json
                {
                    "status_da_documentacao": "Documentação criada com sucesso.",
                    "secoes_documentadas": [
                        "Introdução",
                        "Funcionalidade",
                        "Instalação",
                        "Uso",
                        "Referência de API",
                        "Contribuição",
                        "Licença"
                    ],
                    "observacoes": "A documentação deve ser mantida atualizada conforme novas funcionalidades fo
                }
            ```
        """

        format = 'Responda no formato JSON Exemplo: {"documentacao_corrigida": "documentacao corrigida..."}'
        mensagem = mensaxgem + referencias + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        documentacao_corrigida = response["documentacao_corrigida"]
        print(documentacao_corrigida)
        python_functions.save_TXT(documentacao_corrigida, path_Documentacao, "w")

        self.diretorio_script = os.path.dirname(os.path.abspath(__file__))
        self.path_DocGitHubDataREADME = os.path.join(self.diretorio_script, 'DocGitHubData', f"README{random.randint(30, 900)}.md")
        self.path_DocGitHubData = os.path.join(self.diretorio_script, 'DocGitHubData')
        self.path_DocGitHubData_log = os.path.join(self.diretorio_script, 'docs_uploaded.log')

        python_functions.save_TXT(documentacao_corrigida, self.path_DocGitHubDataREADME, "w")

        self.check_and_upload_docs()

        return path_Documentacao

    def read_uploaded_files(self, log_file="docs_uploaded.log"):
        """Lê o arquivo de log e retorna um conjunto de arquivos já carregados"""
        if os.path.exists(self.path_DocGitHubData_log):
            with open(self.path_DocGitHubData_log, "r") as log:
                uploaded_files = {line.strip() for line in log.readlines()}
        else:
            uploaded_files = set()
        return uploaded_files

    def log_uploaded_file(self, file_name, log_file="docs_uploaded.log"):
        """Registra um arquivo como carregado no arquivo de log"""
        with open(self.path_DocGitHubData_log, "a") as log:
            log.write(f"{file_name}\n")

    def check_and_upload_docs(self, directory="DocGitHubData", name="DocGitHubData", log_file="docs_uploaded.log"):
        """Verifica novos arquivos .md e realiza o upload, registrando-os no log"""
        uploaded_files = self.read_uploaded_files(self.path_DocGitHubData_log)
        files = [f for f in os.listdir(self.path_DocGitHubData) if f.lower().endswith('.md')]
        new_files = [f for f in files if f not in uploaded_files]
        if new_files:
            for file in new_files:
                file_path = os.path.join(self.path_DocGitHubData, file)
                self.upload_to_vectorstore(file_path, name)
                uploaded_files.add(file) 
                self.log_uploaded_file(file, self.path_DocGitHubData_log) 
            print(f"Novos arquivos carregados para {name}: {', '.join(new_files)}")
        else:
            print("Nenhum novo arquivo encontrado.")

    def upload_to_vectorstore(self, file_path, name):
 
        paths_to_upload  = [
            file_path
        ]

        vector_store_id = Agent_files.auth_or_create_vectorstore(name, paths_to_upload, file_path)
        print(vector_store_id)
        print(paths_to_upload)
        print(file_path)
        

