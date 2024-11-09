
#########################################
# IMPORT SoftwareAI Core
from ..._init_core_ import * #AutenticateAgent, ResponseAgent, python_functions
#########################################
# IMPORT SoftwareAI Agents 
# from ..._init_agents_ import AgentInitializer
#########################################
# IMPORT SoftwareAI Libs 
from ..._init_libs_ import *
#########################################
# IMPORT SoftwareAI All Paths 
from ..._init_paths_ import *
#########################################


class ByteManager:
    def __init__(self, 
                Company_Managers,
                Pre_Project_Document,
                Gerente_de_projeto,
                Equipe_De_Solucoes,
                Softwareanaysis,
                SoftwareDevelopment,
                ):
        
        self.Company_Managers = Company_Managers
        self.Pre_Project_Document = Pre_Project_Document
        self.Gerente_de_projeto = Gerente_de_projeto
        self.Equipe_De_Solucoes = Equipe_De_Solucoes
        self.Softwareanaysis = Softwareanaysis
        self.SoftwareDevelopment = SoftwareDevelopment

    ##############################################################################################
    def AI_1_ByteManager_Company_Owners(self,mensagem):
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
            
            resposta_do_matrixminder = self.Company_Managers.AI_MatrixMinder_Company_Managers(pergunta_ao_matrixminder)#invoke_matrixminder(pergunta_ao_matrixminder)
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


            mensaxgem = f"""crie um nome do repositorio desse software no github com base na descricao:\n
            {pergunta_ao_tigrao}
            """
            format = 'Responda no formato JSON Exemplo: {"nome": "nome..."}'
            mensagem = mensaxgem + format
            response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
            try:
                    
                repo_name = response["nome"]
                print(repo_name)
                repo_name_str = f"{repo_name}"
                repo_name_replace = repo_name_str.replace("-", "")
                print(repo_name_replace)
                repo_name = repo_name_replace
            except Exception as errror2:
                print(errror2)
                print(response)

            # Dicionário com os novos caminhos

            # Caminho base para todos os arquivos
            base_path = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}"

            # Dicionário com os caminhos relativos de cada arquivo
            file_paths = {
                "PATH_SOFTWARE_DEVELOPMENT_PY_ENV": os.path.join(base_path, "Software_Development", "python_software.py"),
                "PATH_SOFTWARE_DEVELOPMENT_TXT_ENV": os.path.join(base_path, "Software_Development", "python_software.txt"),
                "PATH_NAME_DOC_PRE_PROJETO_ENV": os.path.join(base_path, "Create_doc_Pre_Projeto", "documento_pre_projeto.txt"),
                "PATH_DOCUMENTACAO_ENV": os.path.join(base_path, "Create_documentation", "README.md"),
                "PATH_NOME_DO_CRONOGRAMA_ENV": os.path.join(base_path, "Create_Cronograma_e_planilha_Projeto", "documento_cronograma_do_projeto.txt"),
                "PATH_PLANILHA_PROJETO_ENV": os.path.join(base_path, "Create_Cronograma_e_planilha_Projeto", "documento_planilha_do_projeto.txt"),
                "PATH_ROADMAP_ENV": os.path.join(base_path, "Create_Roadmap_Projeto", "documento_Roadmap_do_projeto.txt"),
                "PATH_ANALISE_ENV": os.path.join(base_path, "Software_Requirements_Analysis", "analise.txt")
            }

            for path in file_paths.values():
                os.makedirs(os.path.dirname(path), exist_ok=True)
                if not os.path.exists(path):
                    with open(path, "w") as file:
                        file.write("")  

            for key in list(os.environ.keys()):
                if key.endswith('_ENV'):
                    del os.environ[key]

            PATH_SOFTWARE_DEVELOPMENT_PY_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Software_Development\python_software.py"
            PATH_SOFTWARE_DEVELOPMENT_TXT_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Software_Development\python_software.txt"
            PATH_NAME_DOC_PRE_PROJETO_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Create_doc_Pre_Projeto\documento_pre_projeto.txt"
            PATH_DOCUMENTACAO_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Create_documentation\README.md"
            PATH_NOME_DO_CRONOGRAMA_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Create_Cronograma_e_planilha_Projeto\documento_cronograma_do_projeto.txt"
            PATH_PLANILHA_PROJETO_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Create_Cronograma_e_planilha_Projeto\documento_planilha_do_projeto.txt"
            PATH_ROADMAP_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Create_Roadmap_Projeto\documento_Roadmap_do_projeto.txt"
            PATH_ANALISE_ENV = rf"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\Work_Environment\{repo_name}\Software_Requirements_Analysis\analise.txt"
            
            new_paths = {
                "PATH_SOFTWARE_DEVELOPMENT_PY_ENV": os.path.join(base_path, "Software_Development", "python_software.py"),
                "PATH_SOFTWARE_DEVELOPMENT_TXT_ENV": os.path.join(base_path, "Software_Development", "python_software.txt"),
                "PATH_NAME_DOC_PRE_PROJETO_ENV": os.path.join(base_path, "Create_doc_Pre_Projeto", "documento_pre_projeto.txt"),
                "PATH_DOCUMENTACAO_ENV": os.path.join(base_path, "Create_documentation", "README.md"),
                "PATH_NOME_DO_CRONOGRAMA_ENV": os.path.join(base_path, "Create_Cronograma_e_planilha_Projeto", "documento_cronograma_do_projeto.txt"),
                "PATH_PLANILHA_PROJETO_ENV": os.path.join(base_path, "Create_Cronograma_e_planilha_Projeto", "documento_planilha_do_projeto.txt"),
                "PATH_ROADMAP_ENV": os.path.join(base_path, "Create_Roadmap_Projeto", "documento_Roadmap_do_projeto.txt"),
                "PATH_ANALISE_ENV": os.path.join(base_path, "Software_Requirements_Analysis", "analise.txt")
            }

            envvv = "CoreApp/ambiente.env"
            flag = python_functions.update_multiple_env_variables(new_paths, envvv)

            from dotenv import load_dotenv
            load_dotenv(dotenv_path=r"C:\Users\Media Cuts Studio\Desktop\Saas do site\Projetos de codigo aberto\SoftwareAI\CoreApp\ambiente.env")

            if flag:
                print(flag)
                resposta_do_tigrao_com_doc_pre_projeto = self.Pre_Project_Document.AI_1_Pre_Project_Document_Writer(mensagem=pergunta_ao_tigrao)#invoke_tigrao(pergunta_ao_tigrao)

                print(resposta_do_tigrao_com_doc_pre_projeto)

                Uploadfile = resposta_do_tigrao_com_doc_pre_projeto

                path_planilha_Projeto, path_nome_do_cronograma, path_name_doc_Pre_Projeto = self.Gerente_de_projeto.Bob_Gerente_de_projeto(Uploadfile)
                

                path_Roadmap, cronograma_do_projeto, planilha, doc_Pre_Projeto = self.Equipe_De_Solucoes.Dallas_Equipe_De_Solucoes_Roadmap(path_nome_do_cronograma, path_planilha_Projeto, path_name_doc_Pre_Projeto)
                
                # file_paths_to_project = [f"{path_Roadmap}", f"{cronograma_do_projeto}", f"{planilha}", f"{doc_Pre_Projeto}"]
                # print(file_paths_to_project)
                # vectorstore_id = Agent_files.auth_or_create_vectorstore("project_", file_paths_to_project)
                # print(vectorstore_id)
    
                anaysis_in_txt_path = self.Softwareanaysis.AI_SynthOperator(path_Roadmap, cronograma_do_projeto, planilha, doc_Pre_Projeto)

                script_version_1_path = self.SoftwareDevelopment.AI_QuantumCore(
                        PATH_NOME_DO_CRONOGRAMA_ENV,
                        PATH_PLANILHA_PROJETO_ENV,
                        PATH_NAME_DOC_PRE_PROJETO_ENV,
                        PATH_ROADMAP_ENV,
                        PATH_ANALISE_ENV
                    )


                #resposta_AI_ByteManager_dict = json.loads(passando_resposta_do_tigrao_para_AI_ByteManager)
            
                #resposta_AI_ByteManager = resposta_AI_ByteManager_dict['resposta']
                


                return script_version_1_path
