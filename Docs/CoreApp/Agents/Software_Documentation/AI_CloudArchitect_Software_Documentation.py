
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






# SoftwareAI
class Software_Documentation:
    def __init__(self):
        pass

    def CloudArchitect_Software_Documentation_Type_Create(self, path_python_software, path_Analysis, path_Roadmap, path_Spreadsheet, path_Timeline, path_Preproject):

        python_software = python_functions.analyze_txt(path_python_software)

        Analysis = python_functions.analyze_txt(path_Analysis)

        Roadmap = python_functions.analyze_txt(path_Roadmap)

        Spreadsheet = python_functions.analyze_txt(path_Spreadsheet)

        Timeline = python_functions.analyze_txt(path_Timeline)

        Preproject = python_functions.analyze_txt(path_Preproject)

        key = "AI_CloudArchitect_Software_Documentation"
        nameassistant = "AI CloudArchitect Software Documentation"
        model_select = "gpt-4o-mini-2024-07-18"
        
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        Upload_list_for_code_interpreter_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None



        AI_CloudArchitect = AutenticateAgent.create_or_auth_AI(key, instructionCloudArchitect, nameassistant, model_select, tools_CloudArchitect, vectorstore_in_assistant)
        
        
        
        vector_store_id = Agent_files.auth_or_create_vectorstore("DocGitHubData")
        #AI_CloudArchitect = Agent_files_update.update_vectorstore_in_agent(AI_CloudArchitect, [vector_store_id])
        
        mensagem = f"""
        Crie a Documentacao para o github desse software com base no codigo do software e nas documentacoes\n
        Codigo Software:\n
        {python_software}\n
        Documentacao Analysis:\n
        {Analysis}\n
        Documentacao Roadmap:\n
        {Roadmap}\n
        Documentacao Spreadsheet:\n
        {Spreadsheet}\n
        Documentacao Timeline:\n
        {Timeline}\n
        Documentacao Preproject:\n
        {Preproject}\n




        """
        rregras = "Regras: NÃO use a function update_readme_to_github"
        mensagem_final = mensagem + rregras
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem_final,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_CloudArchitect, 
                                                                        AI_CloudArchitect, 
                                                                        model_select,
                                                                        adxitional_instructions_CloudArchitect, key)
        path_Documentacao = os.getenv("PATH_DOCUMENTACAO_ENV")
        print(response)
        

        # # referencias = """remova as referencias a criacao da documentacao por exemplo:\n
        # #     ```json
        # #         {
        # #             "status_da_documentacao": "Documentação criada com sucesso.",
        # #             "secoes_documentadas": [
        # #                 "Introdução",
        # #                 "Funcionalidade",
        # #                 "Instalação",
        # #                 "Uso",
        # #                 "Referência de API",
        # #                 "Contribuição",
        # #                 "Licença"
        # #             ],
        # #             "observacoes": "A documentação deve ser mantida atualizada conforme novas funcionalidades "
        # #         }
        # #     ```
        # # """

        mensaxgem = f"""deixe essa documentacao do github asseguir no formato markdown: \n {response}"""
        format = 'Responda no formato JSON Exemplo: {"documentacao": "documentacao..."}'
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        documentacao_corrigida = response["documentacao"]
        print(documentacao_corrigida)
        python_functions.save_TXT(documentacao_corrigida, path_Documentacao, "w")

        self.diretorio_script = os.path.dirname(os.path.abspath(__file__))
        self.path_DocGitHubDataREADME = os.path.join(self.diretorio_script, 'DocGitHubData', f"README{random.randint(30, 900)}.md")
        self.path_DocGitHubData = os.path.join(self.diretorio_script, 'DocGitHubData')
        self.path_DocGitHubData_log = os.path.join(self.diretorio_script, 'docs_uploaded.log')

        python_functions.save_TXT(documentacao_corrigida, self.path_DocGitHubDataREADME, "w")

        self.check_and_upload_docs()

        return path_Documentacao



    def CloudArchitect_Software_Documentation_Type_Update(self, repo_name, path_readme, code_python_software_old, code_path_python_software_new, path_Analysis, path_Roadmap, path_Spreadsheet, path_Timeline, path_Preproject):

        
        Readme = python_functions.analyze_txt(path_readme)

        # python_software_old = python_functions.analyze_txt(code_python_software_old)

        # python_software_new = python_functions.analyze_txt(code_path_python_software_new)

        # Analysis = python_functions.analyze_txt(path_Analysis)

        # Roadmap = python_functions.analyze_txt(path_Roadmap)

        # Spreadsheet = python_functions.analyze_txt(path_Spreadsheet)

        # Timeline = python_functions.analyze_txt(path_Timeline)

        # Preproject = python_functions.analyze_txt(path_Preproject)

        key = "AI_CloudArchitect_Software_Documentation"
        nameassistant = "AI CloudArchitect Software Documentation"
        model_select = "gpt-4o-mini-2024-07-18"
        
        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        Upload_list_for_code_interpreter_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None



        AI_CloudArchitect = AutenticateAgent.create_or_auth_AI(key, instructionCloudArchitect, nameassistant, model_select, tools_CloudArchitect, vectorstore_in_assistant)

        # vector_store_id = Agent_files.auth_or_create_vectorstore("DocGitHubData")
        #AI_CloudArchitect = Agent_files_update.update_vectorstore_in_agent(AI_CloudArchitect, [vector_store_id])
        
        mensagem = f"""
        Atualize a Documentacao atual do github desse software com base no codigo do software antigo e o software novo \n
        Repo Name:\n
        {repo_name}\n
        Documentacao atual do github:\n
        {Readme}\n
        codigo python do software antigo :\n
        {code_python_software_old}
        codigo python do software novo :\n
        {code_path_python_software_new}\n

        """
        # Documentacao Analysis:\n
        # {Analysis}\n
        # Documentacao Roadmap:\n
        # {Roadmap}\n
        # Documentacao Spreadsheet:\n
        # {Spreadsheet}\n
        # Documentacao Timeline:\n
        # {Timeline}\n
        # Documentacao Preproject:\n
        # {Preproject}\n
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_CloudArchitect, 
                                                                        AI_CloudArchitect, 
                                                                        model_select,
                                                                        adxitional_instructions_CloudArchitect, key)
        path_Documentacao = os.getenv("PATH_DOCUMENTACAO_ENV")
        print(response)
        

        mensaxgem = f"""deixe essa documentacao do github asseguir aprensentavel ao publico: \n {response}"""
        
        # referencias = """remova as referencias a criacao da documentacao por exemplo:\n
        #     ```json
        #         {
        #             "status_da_documentacao": "Documentação criada com sucesso.",
        #             "secoes_documentadas": [
        #                 "Introdução",
        #                 "Funcionalidade",
        #                 "Instalação",
        #                 "Uso",
        #                 "Referência de API",
        #                 "Contribuição",
        #                 "Licença"
        #             ],
        #             "observacoes": "A documentação deve ser mantida atualizada conforme novas funcionalidades "
        #         }
        #     ```
        # """

        format = 'Responda no formato JSON Exemplo: {"documentacao_corrigida": "documentacao corrigida..."}'
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        documentacao_corrigida = response["documentacao_corrigida"]
        print(documentacao_corrigida)
        python_functions.save_TXT(documentacao_corrigida, path_Documentacao, "w")

        self.diretorio_script = os.path.dirname(os.path.abspath(__file__))
        self.path_DocGitHubDataREADME = os.path.join(self.diretorio_script, 'DocGitHubData', f"README{random.randint(30, 900)}.md")
        self.path_DocGitHubData = os.path.join(self.diretorio_script, 'DocGitHubData')
        self.path_DocGitHubData_log = os.path.join(self.diretorio_script, 'docs_uploaded.log')

        python_functions.save_TXT(documentacao_corrigida, self.path_DocGitHubDataREADME, "w")

        github_username, github_token = Github_functions.CloudArchitect_github_keys()

        mensagem = f"""
        Atualiza o Readme do repositorio no github\n
        file_path_readme_improvements:\n
        {path_readme}\n
        repo_name:\n
        {repo_name}\n
        token:\n
        {github_token}\n

        """

        
        response = ResponseAgent.ResponseAgent_message_with_assistants(mensagem,
                                                                        Upload_1_file_in_thread,
                                                                        Upload_1_file_in_message,
                                                                        Upload_1_image_for_vision_in_thread, 
                                                                        Upload_list_for_code_interpreter_in_thread,
                                                                        vectorstore_in_Thread,
                                                                        tools_CloudArchitect, 
                                                                        AI_CloudArchitect, 
                                                                        model_select,
                                                                        adxitional_instructions_CloudArchitect, key)
        path_Documentacao = os.getenv("PATH_DOCUMENTACAO_ENV")
        print(response)
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
        

