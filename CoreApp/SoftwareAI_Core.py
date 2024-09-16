from firebase_admin import credentials, initialize_app, storage, db, delete_app
#from CoreApp.Securityclass import Security
from openai import OpenAI
import time
import subprocess
import pandas as pd
import os
import shutil
import json
import tiktoken
from github import Github
import re
import requests
import base64
import random
from datetime import datetime, timedelta
import json
key_api = 'key'

client = OpenAI(
    api_key=key_api,
)

cred1 = {
  "type": "service_account",
  "project_id": "aicompanydata1",
  "private_key_id": "key",
  "private_key": "key",
  "client_email": "key",
  "client_id": "key",
  "auth_uri": "key",
  "token_uri": "key",
  "auth_provider_x509_cert_url": "key",
  "client_x509_cert_url": "key",
  "universe_domain": "key"
}
credt1 = credentials.Certificate(cred1)
app1 = initialize_app(credt1, {
        'storageBucket': 'aicompanydata1key.pot.com',
        'databaseURL': 'https://aicompanydata1key.firebasedatabase.app'
}, name='app1')


bucket = storage.bucket(app=app1)

class AutenticateAgent:

    def create_or_auth_AI(key: str, instructionsassistant, nameassistant: str, model_select: str, tools, vectorstore: list):
        """ 
        :param key: this is the key that represents the agent in the database
            
        :param instructionsassistant: This argument is the instruction of the agent's behavior The maximum length is 256,000 characters.
        
        :param nameassistant: This argument is the name of the agent The maximum length is 256 characters.
        
        :param model_select: This argument is the AI model that the agent will use
            
        :param tools: This argument is the agent's tools  There can be a maximum of 128 tools per assistant. Tools can be of types code_interpreter, file_search, vectorstore, or function.
            
        :param vectorstore: This argument is the vector storage id desired when creating or authenticating the agent
            
        """


        try:
            ref1 = db.reference(f'ai_org_assistant_id/User_{key}', app=app1)
            data1 = ref1.get()
            assistant_id = data1['assistant_id']
            if tools:
                client.beta.assistants.update(
                    assistant_id=str(assistant_id),
                    tools=tools
                    
                )

            if vectorstore:
                client.beta.assistants.update(
                    assistant_id=str(assistant_id),
                    tool_resources={"file_search": {"vector_store_ids": vectorstore}},
                )

            return str(assistant_id)
        except Exception as err234:
            if tools:
                assistant = client.beta.assistants.create(
                    name=nameassistant,
                    tools=tools,
                    instructions=instructionsassistant,
                    model=model_select,
                )
                if vectorstore:
                    client.beta.assistants.update(
                        assistant_id=assistant.id,
                        tool_resources={"file_search": {"vector_store_ids": vectorstore}},
                    )
            else:
                assistant = client.beta.assistants.create(
                    name=nameassistant,
                    instructions=instructionsassistant,
                    model=model_select,
                )


            ref1 = db.reference(f'ai_org_assistant_id', app=app1)
            controle_das_funcao2 = f"User_{key}"
            controle_das_funcao_info_2 = {
                "assistant_id": f'{assistant.id}',
                "key": f'{key}'
            }
            ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
            return str(assistant.id)
        
    def create_or_auth_thread(key, file_in_thread: str, attachavectorstoretoThreads: str):
        """ 
        :param key: this is the key that represents the agent in the database
            
        :param file_in_thread: This argument is the id of the desired file in the thread
        :param attachavectorstoretoThreads: attach a vector store to Threads "vector_store_ids": ["vs_2"]

        """

        
        try:
            ref1 = db.reference(f'ai_org_thread_Id/User_{key}', app=app1)
            data1 = ref1.get()
            thread_Id = data1['thread_id']
            print(thread_Id)
            if attachavectorstoretoThreads:
                client.beta.threads.update(
                    str(thread_Id),
                    tool_resources={
                        "file_search": {
                        "vector_store_ids": [attachavectorstoretoThreads]
                        }
                    }
                    
                )
            return str(thread_Id)
        except Exception as err234z:
            print(err234z)
            if file_in_thread:
                thread = client.beta.threads.create(
                    tool_resources={"file_search": {"file_id": [file_in_thread]}},
                )
                if attachavectorstoretoThreads:
                    client.beta.threads.update(
                        str(thread_Id),
                        tool_resources={
                            "file_search": {
                            "vector_store_ids": [attachavectorstoretoThreads]
                            }
                        }
                        
                    )
                ref1 = db.reference(f'ai_org_thread_Id', app=app1)
                controle_das_funcao2 = f"User_{key}"
                controle_das_funcao_info_2 = {
                    "thread_id": f'{thread.id}',
                    "key": f'{key}'
                }
                ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
                return str(thread.id)

            else:        
                thread = client.beta.threads.create()
                if attachavectorstoretoThreads:
                    client.beta.threads.update(
                        str(thread_Id),
                        tool_resources={
                            "file_search": {
                            "vector_store_ids": [attachavectorstoretoThreads]
                            }
                        }
                        
                    )
                ref1 = db.reference(f'ai_org_thread_Id', app=app1)
                controle_das_funcao2 = f"User_{key}"
                controle_das_funcao_info_2 = {
                    "thread_id": f'{thread.id}',
                    "key": f'{key}'
                }
                ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
                return str(thread.id)

class ResponseAgent:
    def ResponseAgent_message_completions(prompt, sistema = "", json_format = True):

        #key_api = os.getenv("OPENAI_API_KEY")  # Get the API key from the environment
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {key_api}",
            "Content-Type": "application/json"
        }

        formato = "text"
        if json_format:
            formato = "json_object"

        mensagem = []
        if sistema != "":
            mensagem.append({"role": "system", "content": sistema})
        mensagem.append({"role": "user", "content": prompt})

        data = {
            "model": "gpt-4o-mini",  # Ensure to specify the correct model
            "messages": mensagem,
            "max_tokens": 16_384,  # You can adjust this as needed
            "response_format": { "type": formato },
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            response_json = response.json()
            if json_format:
                return json.loads(response_json['choices'][0]['message']['content'])
            return response_json['choices'][0]['message']['content']
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
        
        
    def ResponseAgent_message_with_assistants(mensagem, Upload_1_file_in_thread: str, Upload_1_file_in_message: str, Upload_1_image_for_vision_in_thread: str, vectorstore_in_Thread: str, tools, agent_id: str, model_select: str, aditional_instructions, key):
        """ 
        :param mensagem: This argument is the desired message that the agent responds to | If not use = None
            
        :param Upload_1_file_in_thread: This argument is the location of the file that will be uploaded to the thread | If not use = None
        
        :param Upload_1_file_in_message: This argument is the location of the file that will be uploaded along with the message | If not use = None
        
        :param agent_id: This argument is the id of the authenticated or created agent
            
        :param model_select: This argument is the AI model that the agent will use
        
        :param aditional_instructions: This argument is an additional instruction to the agent's behavior | If not use = None

        :param key: this is the key that represents the agent in the database


        
        """

        
        if Upload_1_file_in_message:
            
            message_file = client.files.create(
                file=open(Upload_1_file_in_message, "rb"), purpose="assistants"
            )
            threead_id = AutenticateAgent.create_or_auth_thread(key, Upload_1_file_in_thread, vectorstore_in_Thread)
            if Upload_1_image_for_vision_in_thread:
                flag = Agent_files.upload_image_for_vision_in_thread(Upload_1_image_for_vision_in_thread, threead_id)
                print(flag)

            message = client.beta.threads.messages.create(
                thread_id=threead_id,
                role="user",
                content=mensagem,
                attachments=[{ "file_id": message_file.id }]  
            )
            


        elif Upload_1_file_in_thread:
            
            message_file = client.files.create(
                file=open(Upload_1_file_in_thread, "rb"), purpose="assistants"
            )
            file_in_thread = message_file.id 
            threead_id = AutenticateAgent.create_or_auth_thread(key, file_in_thread, vectorstore_in_Thread)

            if Upload_1_image_for_vision_in_thread:
                flag = Agent_files.upload_image_for_vision_in_thread(Upload_1_image_for_vision_in_thread, threead_id)
                print(flag)

        #if Uploadfile_in_message is None or Uploadfile_in_thread is None or Uploadfile_in_message and Uploadfile_in_thread is None:
        else:
            
            threead_id = AutenticateAgent.create_or_auth_thread(key, Upload_1_file_in_thread, vectorstore_in_Thread)
            if Upload_1_image_for_vision_in_thread:
                flag = Agent_files.upload_image_for_vision_in_thread(Upload_1_image_for_vision_in_thread, threead_id)
                print(flag)
            message = client.beta.threads.messages.create(
                thread_id=threead_id,
                role="user",
                content=mensagem,
                
            )





        if tools:

            run = client.beta.threads.runs.create(
                thread_id=threead_id,
                assistant_id=agent_id,
                tools=tools,
                additional_instructions=aditional_instructions,
                model=model_select,
            )

        else:

            run = client.beta.threads.runs.create(
                thread_id=threead_id,
                assistant_id=agent_id,
                additional_instructions=aditional_instructions,
                model=model_select,
            )


        contador = 0
        while True:
            time.sleep(2)
            run_status = client.beta.threads.runs.retrieve(
                thread_id=threead_id,
                run_id=run.id
            )
            print(run_status.status)

            if run_status.status == 'requires_action':
                for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                    if tool_call.type == 'function':
                        function_name = tool_call.function.name
                        function_arguments = tool_call.function.arguments
                        if function_name == 'test_software':
                            args = json.loads(function_arguments)
                            report = test_software(
                                test_file_path=args['test_file_path'],
                                repo_owner=args['repo_owner'],
                                repo_name=args['repo_name'],
                                branch_name=args['branch_name'],
                                file_path=args['file_path'],
                                token=args['token']
                            )
                            tool_call_id = tool_call.id  
                            client.beta.threads.runs.submit_tool_outputs(
                                thread_id=threead_id,
                                run_id=run.id,
                                tool_outputs=[
                                    {
                                        "tool_call_id": tool_call_id, 
                                        "output": json.dumps(report)  
                                    }
                                ]
                            )


                        elif function_name == 'create_github_repo_and_upload':
                            args = json.loads(function_arguments)
                            result = create_github_repo_and_upload(
                                repo_name=args['repo_name'],
                                repo_description=args['repo_description'],
                                readme_file_path=args['readme_file_path'],
                                code_file_paths=args['code_file_paths'],
                                token=args['token']
                            )
                            tool_call_id = tool_call.id
                            client.beta.threads.runs.submit_tool_outputs(
                                thread_id=threead_id,
                                run_id=run.id,
                                tool_outputs=[
                                    {
                                        "tool_call_id": tool_call_id, 
                                        "output": json.dumps(result)  
                                    }
                                ]
                            )

                        elif function_name == 'improve_code_and_create_pull_request':
                            args = json.loads(function_arguments)
                            result = improve_code_and_create_pull_request(
                                repo_owner=args['repo_owner'],
                                repo_name=args['repo_name'],
                                branch_name=args['branch_name'],
                                file_path=args['file_path'],
                                commit_message=args['commit_message'],
                                improvements=args['improvements'],
                                token=args['token']
                            )
                            tool_call_id = tool_call.id
                            client.beta.threads.runs.submit_tool_outputs(
                                thread_id=threead_id,
                                run_id=run.id,
                                tool_outputs=[
                                    {
                                        "tool_call_id": tool_call_id,
                                        "output": json.dumps(result)
                                    }
                                ]
                            )

            elif run_status.status == 'completed':
                break
            elif run_status.status == 'failed':
                pass
            elif run_status.status == 'in_progress':
                print("in_progress")
            else:
                contador += 1 
                if contador == 15:
                    break
                print("Aguardando a execução ser completada...")

        messages = client.beta.threads.messages.list(
            thread_id=threead_id
        )
        for message in messages:
            for mensagem_contexto in message.content:
                valor_texto = mensagem_contexto.text.value
                
                return valor_texto

            break

class Github_functions:
    def NexGenCoder_gmail_keys():
        gmail = "key@gmail.com"
        key = "key123"
        return gmail, key
    
    def NexGenCoder_github_keys():
        github_username = "key756"
        github_password = "key!@key123"
        github_token = "key"
        return github_username, github_password, github_token



    def QuantumCore_gmail_keys():
        gmail = "key@gmail.com"
        key = "key@123"
        return gmail, key

    def QuantumCore_github_keys():
        github_username = "key"
        github_token = "key"
        return github_username, github_token
    
    
    def quantumcore_discord_keys():
        token = "key.GgPwEc.key"
        
        return token


    def SignalMaster_github_keys():
        github_username = "key"
        github_token = "key"
        return github_username, github_token
    

    def SignalMaster_gmail_keys():
        gmail = "key@gmail.com"
        key = "key@1234"
        return gmail, key
    

    def SignalMaster_discord_keys():
        token = "key.Gm44yb.key"
        
        return token

    # def verify_repo_and_upload_py(repo: str, py: str, GITHUB_TOKEN: str, description: str, private: bool):
    #     try:


        
    #     except:

    #         # Autenticação com o token de acesso pessoal
    #         g = Github(GITHUB_TOKEN)
            
    #         # Obtendo o usuário autenticado
    #         user = g.get_user()
            
    #         # Criando um novo repositório
    #         repo = user.create_repo(
    #             name=repo,
    #             description=description,
    #             private=private
    #         )
            
    #         print(f"Repositório '{repo}' criado com sucesso!")
    #         print(f"URL: {repo.html_url}")



    def create_github_repo(token, repo_name, description, private):
    
        
        
        
        # Remover caracteres de controle da descrição
        sanitized_description = re.sub(r'[\x00-\x1F\x7F]', '', description)
        
        # Autenticação com o token de acesso pessoal
        g = Github(token)
        
        # Obtendo o usuário autenticado
        user = g.get_user()
        
        # Criando um novo repositório
        repo = user.create_repo(
            name=repo_name,
            description=sanitized_description,
            private=private
        )

        return repo.html_url, repo_name

    def upload_past_to_github(username, token, owner, repo_name, folder_path, destination_path):
        g = Github(username, token)
        repo = g.get_user(owner).get_repo(repo_name)
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                relative_path = os.path.relpath(file_path, folder_path)
                destination_file_path = os.path.join(destination_path, relative_path)
                destination_file_path = f"{file_name}/{file_name}"
                try:
                    existing_file = repo.get_contents(destination_file_path)
                    sha = existing_file.sha
                except Exception:
                    sha = None
                if sha is not None:
                    repo.update_file(destination_file_path, f"Committing {destination_file_path}", content, sha)
                else:
                    repo.create_file(destination_file_path, f"Committing {destination_file_path}", content)
                return f"Arquivo {destination_file_path} enviado com sucesso para o repositório {owner}/{repo_name}"
                


    def upload_py_to_github(username, token, owner, repo_name, file_paths):
        def get_file_content(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        g = Github(username, token)
        repo = g.get_user(owner).get_repo(repo_name)
    
        try:
            file = repo.get_contents(file_paths)
            sha = file.sha
        except Exception:
            sha = None
        content = get_file_content(file_paths)
        if sha is not None:
            repo.update_file(file_paths, f"Committing {file_paths}", content, sha)
        else:
            repo.create_file(file_paths, f"Committing {file_paths}", content)
        return f"Arquivo {file_paths} Foi  para o repositório {owner}/{repo_name}"
    
class Agent_files_update:
    def update_vectorstore_in_agent(assistant_id, vector_store_id: list):
        assistant = client.beta.assistants.update(
            assistant_id=assistant_id,
            tools=[{"type": "file_search"}],
            tool_resources={"file_search": {"vector_store_ids": vector_store_id}},
        )
        return assistant.id
    
    def update_new_files_in_thread():
        pass

class Agent_files:

    def upload_image_for_vision_in_thread(image_file_path: str, thread_id: str):
        try:
            with open(image_file_path, "rb") as image_file:
                file = client.files.create(
                    file=image_file,
                    purpose="vision"
                )
            client.beta.threads.update(
                thread_id=thread_id,  
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_file",
                                "image_file": {"file_id": file.id} 
                            }
                        ],
                    }
                ]
            )
            return f"Image uploaded successfully with file_id: {file.id}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    
    def auth_or_upload_multiple_files(name_for: str, list_files_path: list):
        try:
            ref1 = db.reference(f'auth_or_upload_multiple_files/User_{name_for}', app=app1)
            data1 = ref1.get()
            list_return = data1['list']
            return list(list_return)
        except:
            lista_de_file_id = []
            for file in list_files_path:
                message_file = client.files.create(
                    file=open(file, "rb"), purpose="assistants"
                )
                lista_de_file_id.append(message_file.id)

            ref1 = db.reference(f'auth_or_upload_multiple_files', app=app1)
            controle_das_funcao2 = f"User_{name_for}"
            controle_das_funcao_info_2 = {
                "list": lista_de_file_id,
            }
            ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
            return lista_de_file_id

    def auth_or_create_vector_store_with_multiple_files(name_for_vectorstore: str, file_ids: list): 
        """
        You can add multiple files to a vector store by creating batches of up to 500 files.

        \n
        vector_store_id="vs_abc123"\n
        file_ids=['file_1', 'file_2', 'file_3', 'file_4', 'file_5']\n


        """
        try:
            ref1 = db.reference(f'auth_or_create_vector_store_with_multiple_files/User_{name_for_vectorstore}', app=app1)
            data1 = ref1.get()
            vector_store_return = data1['vectorstore']
            return str(vector_store_return)
        except:
            vector_store = client.beta.vector_stores.create(name=name_for_vectorstore)
            client.beta.vector_stores.file_batches.create_and_poll(
                vector_store_id=vector_store.id,
                file_ids=file_ids
            )
            ref1 = db.reference(f'auth_or_create_vector_store_with_multiple_files', app=app1)
            controle_das_funcao2 = f"User_{name_for_vectorstore}"
            controle_das_funcao_info_2 = {
                "vectorstore": vector_store.id,
            }
            ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)

            return vector_store.id


    def auth_or_create_vectorstore(name_for_vectorstore: str, file_paths: list):
        """Create or auth vector store \n 
        O tamanho máximo por arquivo é 512 MB. Cada arquivo deve conter no máximo 5.000.000 de tokens por arquivo (calculado automaticamente quando você anexa um arquivo).
        \n 
        name_for_vectorstore = "teste"\n 
        file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"]"""

        try:
            ref1 = db.reference(f'ai_org_vector_store/User_{name_for_vectorstore}', app=app1)
            data1 = ref1.get()
            vector_store_id = data1['vector_store_id']
            return str(vector_store_id)
        except:
            vector_store = client.beta.vector_stores.create(name=name_for_vectorstore)
            file_streams = [open(path, "rb") for path in file_paths]
            client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id, files=file_streams
            )
            ref1 = db.reference(f'ai_org_vector_store', app=app1)
            controle_das_funcao2 = f"User_{name_for_vectorstore}"
            controle_das_funcao_info_2 = {
                "name_for_vectorstore": f'{name_for_vectorstore}',
                "vector_store_id": f'{vector_store.id}'
            }
            ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
            return vector_store.id
        
class python_functions:

    def execute_python_code_created(filename):
        try:
            result = subprocess.run(['python', filename], capture_output=True, text=True)
            return f"Saída padrão: {result.stdout}" 
        except Exception as e:
            pass

    def save_data_frame_planilha(planilha_json, path_nome_da_planilha):
        df = pd.DataFrame(planilha_json)
        df.to_csv(path_nome_da_planilha, index=False)

    def save_python_code(code_string, name_script):
        with open(name_script, 'w', encoding="utf-8") as file:
            file.write(code_string)

    def save_csv(dataframe, path_nome_do_cronograma):
        """
        Salva o DataFrame em um arquivo CSV no caminho especificado.

        :param dataframe: O DataFrame a ser salvo.
        :param path_nome_do_cronograma: O caminho e nome do arquivo CSV onde o DataFrame será salvo.
        """
        try:
            dataframe.to_csv(path_nome_do_cronograma, index=False, encoding='utf-8')
            print(f"Arquivo salvo com sucesso em: {path_nome_do_cronograma}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV: {e}")

    def save_TXT(string, filexname, letra):
        with open(filexname, letra, encoding="utf-8") as file:
            file.write(f'\n{string}')
   
    def save_json(string, filexname):
        with open(filexname, 'w', encoding='utf-8') as json_file:
            json.dump(string, json_file, ensure_ascii=False, indent=4)
        print("JSON salvo em 'documento_pre_projeto.json'")


    def delete_all_lines_in_txt(filepath):
        with open(filepath, 'w') as file:
            pass  
    
    def move_arqvios(a, b):
        pasta1 = os.listdir(a)
        for arquivo in pasta1:
            caminho_arquivo_origem = os.path.join(a, arquivo)
            caminho_arquivo_destino = os.path.join(b, arquivo)
            shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)
            print(f'{arquivo} movido para {b}')

    def executar_agentes(mensagem, name_for_script, nome_agente):
        comando_terminal = ['start', 'python', f'{nome_agente}.py', mensagem, name_for_script]
        subprocess.Popen(comando_terminal, shell=True)

    def analyze_txt_0(file):
        with open(file, 'r') as file:
            linhas = file.readlines()
            ultima_linha = linhas[-1].strip()
            return ultima_linha
    def analyze_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    return content
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        return content
                except UnicodeDecodeError:
                    return None

    def analyze_txt(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    return content
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        return content
                except UnicodeDecodeError:
                    pass

    def analyze_csv(file_path):
        import csv
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def analyze_json(file_path):
        import json
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"Dados JSON:\n{data}")


def run_tests(test_file_path):
    """Executa os testes no arquivo .py especificado e retorna o resultado detalhado."""
    try:
        # Executa os testes usando pytest e captura a saída
        result = subprocess.run(['pytest', test_file_path], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Testes foram executados com sucesso
            return {
                'output': result.stdout,
                'error': result.stderr,
                'success': True
            }
        else:
            # Houve falhas na execução dos testes
            return {
                'output': result.stdout,
                'error': result.stderr,
                'success': False
            }

    except Exception as e:
        # Captura qualquer exceção que possa ocorrer
        print(f"Ocorreu um erro ao executar os testes: {str(e)}")
        return {
            'output': None,
            'error': str(e),
            'success': False
        }

def generate_test_report(test_file_path):
    """Gera um relatório detalhado dos testes executados."""
    test_results = run_tests(test_file_path)
    
    report = {
        'test_file': test_file_path,
        'timestamp': datetime.now().isoformat(),
        'status': 'success' if test_results['success'] else 'failure'
    }
    
    if test_results['success']:
        report['details'] = test_results['output'] + test_results['error'] 
    else:
        report['details'] = test_results['error'] if test_results['error'] else test_results['output']
    
    return report

def save_test_report_to_pull_request(report, file_path, repo_owner, repo_name, branch_name, token):
    """Salva o relatório de teste em um pull request no GitHub."""

    file_pathRelatório = "Work_Environment/Create_Testing_in_Software_Development/Testing_in_Software.txt"
    with open(file_pathRelatório, 'w') as json_file:
        json.dump(report, json_file, indent=4)
    print(f"Relatório de teste salvo no arquivo {file_pathRelatório}")

    # Converta o relatório para JSON
    report_json = json.dumps(report, indent=4)

    # Verificar se o branch principal existe (ex: 'main')
    repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs/heads/main"
    response = requests.get(repo_url, headers={'Authorization': f'token {token}'})

    if response.status_code == 404:  # Branch principal não existe
        print("Branch 'main' não encontrado. Criando branch 'main' a partir de um commit inicial.")

        # Criar um commit inicial vazio
        create_commit_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/commits"
        commit_data = {
            "message": "Initial commit",
            "tree": "",
            "parents": []
        }
        response = requests.post(create_commit_url, headers={'Authorization': f'token {token}'}, json=commit_data)
        if response.status_code != 201:
            print(f"Erro ao criar commit inicial: {response.content}")
            return
        commit_sha = response.json()['sha']

        # Criar o branch 'main' usando o commit inicial
        create_branch_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs"
        branch_data = {
            "ref": "refs/heads/main",
            "sha": commit_sha
        }
        response = requests.post(create_branch_url, headers={'Authorization': f'token {token}'}, json=branch_data)
        if response.status_code != 201:
            print(f"Erro ao criar o branch 'main': {response.content}")
            return
        print("Branch 'main' criado com sucesso.")

    # Crie um novo branch baseado no branch principal
    response = requests.get(repo_url, headers={'Authorization': f'token {token}'})
    main_sha = response.json().get('object', {}).get('sha')

    if not main_sha:
        print("Erro ao obter SHA do branch principal.")
        return
    randomnumber = random.randint(1, 175)
    branch_name = f"{branch_name}_{randomnumber}"
    print(branch_name)
    new_branch_data = {
        "ref": f"refs/heads/{branch_name}",
        "sha": main_sha
    }
    create_branch_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs"
    response = requests.post(create_branch_url, headers={'Authorization': f'token {token}'}, json=new_branch_data)
    if response.status_code != 201:
        print(f"Erro ao criar o branch: {response.content}")

        # Crie um novo branch baseado no branch principal
        response = requests.get(repo_url, headers={'Authorization': f'token {token}'})
        main_sha = response.json().get('object', {}).get('sha')

        if not main_sha:
            print("Erro ao obter SHA do branch principal.")
            return
        randomnumber = random.randint(1, 175)
        branch_name = f"{branch_name}_{randomnumber}"
        print(branch_name)
        new_branch_data = {
            "ref": f"refs/heads/{branch_name}",
            "sha": main_sha
        }
        create_branch_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs"
        response = requests.post(create_branch_url, headers={'Authorization': f'token {token}'}, json=new_branch_data)
        if response.status_code != 201:
            print(f"Erro ao criar o branch: {response.content}")
            return
        
    # Adicionar o arquivo ao novo branch
    create_file_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    commit_message = f"Test software report {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    content_base64 = base64.b64encode(report_json.encode()).decode()

    file_data = {
        "message": commit_message,
        "content": content_base64,
        "branch": branch_name
    }

    response = requests.put(create_file_url, headers={'Authorization': f'token {token}'}, json=file_data)
    if response.status_code not in [201, 200]:
        print(f"Erro ao adicionar o arquivo: {response.content}")
        return

    # Criar um pull request para o branch criado
    prompt = f"""Crie um relatorio completo para o pull request com base nesses testes:\n
    {report_json}
      
    """
    formato = """Responda no formato JSON
    Exemplo:
    {"resposta": "resposta ..."}"""
    promptt = prompt + formato

    pullrequestsreport = ResponseAgent.ResponseAgent_message_completions(promptt, "", True)
    print(pullrequestsreport)
    try:
        resposta = pullrequestsreport["resposta"]
    except:
        resposta = pullrequestsreport

    create_pr_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    pr_data = {
        "title": "Test software report",
        "body": f"""{resposta} \n {report_json}""",
        "head": branch_name,
        "base": "main"
    }
    response = requests.post(create_pr_url, headers={'Authorization': f'token {token}'}, json=pr_data)
    if response.status_code == 201:
        print("Pull request criado com sucesso.")
    else:
        print(f"Erro ao criar o pull request: {response.content}")

def test_software(test_file_path, repo_owner, repo_name, branch_name, file_path, token):
    """Executa testes de software, gera um relatório detalhado e salva em um Pull Request no GitHub."""
    report = generate_test_report(test_file_path)
    save_test_report_to_pull_request(report, file_path, repo_owner, repo_name, branch_name, token)
    return report

def handle_test_software(test_file_path, repo_owner, repo_name, branch_name, file_path, token):
    """Função manipuladora para executar os testes e retornar o relatório."""
    report = test_software(test_file_path, repo_owner, repo_name, branch_name, file_path, token)
    return {"report": report}

def submit_test_results(client, thread_id, run_id, test_report, function_name):
    """
    Envia os resultados dos testes para a API da OpenAI usando a chamada de função.

    :param client: Instância do cliente da API da OpenAI
    :param thread_id: ID da thread em execução
    :param run_id: ID do run específico
    :param test_report: Dicionário contendo os resultados dos testes
    """
   
    function_data = {
        "thread_id": thread_id,
        "run_id": run_id,
        "test_report": test_report
    }

    response = client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_output={
            "function_name": function_name,
            "arguments": json.dumps(function_data)
        }
    )

    if response.status == "success":
        print("Resultados dos testes enviados com sucesso.")
    else:
        print(f"Erro ao enviar resultados dos testes: {response}")

def create_github_repo_and_upload(repo_name: str, repo_description: str, readme_file_path: str, code_file_paths: list, token: str):
    # URL para criar o repositório dentro da organização
    repo_url = f"https://api.github.com/orgs/A-I-O-R-G/repos"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    repo_data = {
        "name": repo_name,
        "description": repo_description,
        "private": False
    }

    response = requests.post(repo_url, json=repo_data, headers=headers)

    if response.status_code == 201:
        print(f"Repositório {repo_name} criado com sucesso na organização A-I-O-R-G!")
    else:
        print(f"Falha ao criar o repositório. Status: {response.status_code}, Resposta: {response.json()}")
        return {"status": "error", "message": response.json()}

    # URL para fazer upload dos arquivos
    repo_git_url = f"https://api.github.com/repos/A-I-O-R-G/{repo_name}/contents/"

    def upload_file_to_github(file_path, commit_message):
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as file:
            file_content = file.read()
            file_base64 = base64.b64encode(file_content).decode('utf-8')

        upload_data = {
            "message": commit_message,
            "content": file_base64
        }

        file_url = repo_git_url + file_name
        upload_response = requests.put(file_url, json=upload_data, headers=headers)

        if upload_response.status_code == 201:
            print(f"Arquivo {file_name} carregado com sucesso no repositório.")
        else:
            print(f"Falha ao fazer upload do arquivo {file_name}. Status: {upload_response.status_code}")
            return {"status": "error", "message": upload_response.json()}

    # Upload do arquivo README.md
    upload_file_to_github(readme_file_path, "Adicionando documentação")

    # Upload dos arquivos Python
    for code_file_path in code_file_paths:
        upload_file_to_github(code_file_path, "Adicionando código fonte")

    # Adicionando colaborador com permissões de administrador
    collaborator_url = f"https://api.github.com/repos/A-I-O-R-G/{repo_name}/collaborators/SignalMaster727"

    collaborator_data = {
        "permission": "admin"
    }

    collaborator_response = requests.put(collaborator_url, headers=headers, json=collaborator_data)

    if collaborator_response.status_code == 201 or collaborator_response.status_code == 204:
        print(f"Colaborador 'SignalMaster727' adicionado com sucesso com permissões de administrador.")
    else:
        print(f"Falha ao adicionar colaborador. Status: {collaborator_response.status_code}, Resposta: {collaborator_response.json()}")
        return {"status": "error", "message": collaborator_response.json()}

    return {"status": "success", "message": "Repositório, arquivos e colaborador adicionados com sucesso"}

def submit_upload_results(client, thread_id, run_id, result_data, function_name):
    """
    Envia os resultados do upload do repositório e arquivos para a API da OpenAI.

    :param client: Instância do cliente da API da OpenAI
    :param thread_id: ID da thread em execução
    :param run_id: ID do run específico
    :param result_data: Dicionário contendo o status do upload
    :param function_name: Nome da função para registrar a execução
    """
    function_data = {
        "thread_id": thread_id,
        "run_id": run_id,
        "result_data": result_data
    }

    response = client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_output={
            "function_name": function_name,
            "arguments": json.dumps(function_data)
        }
    )

    if response.status == "success":
        print("Resultados do upload enviados com sucesso.")
    else:
        print(f"Erro ao enviar resultados do upload: {response}")

def improve_code_and_create_pull_request(repo_owner: str, repo_name: str, branch_name: str, file_path: str, commit_message: str, improvements: str, token: str):
    """
    Realiza melhorias no código e cria um pull request no repositório GitHub dentro de uma organização.
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Verificar se a branch principal existe (ex: 'main')
    repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches/main"
    response = requests.get(repo_url, headers=headers)
    
    if response.status_code == 404:  # Branch principal não existe
        print("Branch 'main' não encontrada. Criando a branch 'main' a partir de um commit inicial.")
        # Criar um commit inicial vazio
        create_commit_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/commits"
        commit_data = {
            "message": "Initial commit",
            "tree": "",  # Crie um commit com uma árvore vazia
            "parents": []
        }
        response = requests.post(create_commit_url, headers=headers, json=commit_data)
        if response.status_code != 201:
            print(f"Erro ao criar o commit inicial: {response.content}")
            return
        commit_sha = response.json()['sha']

        # Criar a branch 'main' usando o commit inicial
        create_branch_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs"
        branch_data = {
            "ref": "refs/heads/main",
            "sha": commit_sha
        }
        response = requests.post(create_branch_url, headers=headers, json=branch_data)
        if response.status_code != 201:
            print(f"Erro ao criar a branch 'main': {response.content}")
            return
        print("Branch 'main' criada com sucesso.")

    # Obter SHA do branch principal
    response = requests.get(repo_url, headers=headers)
    main_sha = response.json().get('commit', {}).get('sha')
    if not main_sha:
        print("Erro ao obter SHA do branch principal.")
        return

    # Criar uma nova branch baseada no branch principal
    new_branch_data = {
        "ref": f"refs/heads/{branch_name}",
        "sha": main_sha
    }
    create_branch_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs"
    response = requests.post(create_branch_url, headers=headers, json=new_branch_data)
    if response.status_code != 201:
        print(f"Erro ao criar o branch: {response.content}")
        return

    # Verificar se o arquivo já existe no branch principal
    file_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}?ref=main"
    response = requests.get(file_url, headers=headers)
    file_sha = None
    if response.status_code == 200:
        file_sha = response.json().get('sha')  # Obter SHA do arquivo existente

    # Adicionar ou atualizar o arquivo no novo branch
    file_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    improved_content_base64 = base64.b64encode(improvements.encode()).decode()
    file_data = {
        "message": commit_message,
        "content": improved_content_base64,
        "branch": branch_name
    }
    if file_sha:
        file_data["sha"] = file_sha  # Incluir o SHA para atualização

    response = requests.put(file_url, headers=headers, json=file_data)
    if response.status_code not in [201, 200]:
        print(f"Erro ao adicionar o arquivo: {response.content}")
        return

    # Criar título para o pull request usando a OpenAI API
    title_prompt = f"""Crie um título para um pull request no GitHub com base no código e na mensagem de commit:
    código:
    {improvements}
    commit_message:
    {commit_message}
    """
    format = 'Responda no formato JSON Exemplo: {"nome_para_pr": "nome do pull request..."}'
    title_message = title_prompt + format
    response = ResponseAgent.ResponseAgent_message_completions(title_message, "", True)
    pr_title = response.get("nome_para_pr", "Título do Pull Request")

    # Criar o pull request
    pr_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    pr_data = {
        "title": pr_title,
        "body": commit_message,
        "head": branch_name,
        "base": "main"  # Supondo que a branch principal seja 'main'
    }
    pr_response = requests.post(pr_url, json=pr_data, headers=headers)
    if pr_response.status_code == 201:
        print("Pull request criado com sucesso!")
        return {"status": "success", "message": "Pull request criado com sucesso", "pull_request_url": pr_response.json()['html_url']}
    else:
        print(f"Erro ao criar o pull request: {pr_response.content}")
        return {"status": "error", "message": pr_response.json()}

def merge_pull_request(repo_owner: str, repo_name: str, pr_number: int, token: str):
    """
    Faz o merge de um pull request aprovado com a branch principal.
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Obter as informações do PR
    pr_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    pr_response = requests.get(pr_url, headers=headers)

    if pr_response.status_code != 200:
        print(f"Erro ao buscar PR. Status: {pr_response.status_code}")
        return {"status": "error", "message": pr_response.json()}

    pr_data = pr_response.json()

    # Verificar se o pull request foi aprovado
    if pr_data['mergeable'] is False:
        return {"status": "error", "message": "Pull request não está pronto para merge."}

    # Fazer o merge do pull request
    merge_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/merge"
    merge_data = {
        "commit_title": f"Merge PR #{pr_number}: {pr_data['title']}",
        "commit_message": "Merge realizado automaticamente pelo QuantumCore.",
        "merge_method": "merge"  # ou 'squash' ou 'rebase', se preferir outros métodos de merge
    }

    merge_response = requests.put(merge_url, json=merge_data, headers=headers)

    if merge_response.status_code == 200:
        print("Merge realizado com sucesso!")
        return {"status": "merged", "message": "Pull request foi mergeado com sucesso."}
    else:
        print(f"Erro ao fazer merge. Status: {merge_response.status_code}")
        return {"status": "error", "message": merge_response.json()}
    
def quantumcore_review_pr(repo_owner: str, repo_name: str, pr_number: int):
    """
    QuantumCore analisa o pull request e decide se aprova ou solicita mais melhorias.
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
    adxitional_instructions = None
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

    Upload_1_file_in_thread = None
    Upload_1_file_in_message = None
    Upload_1_image_for_vision_in_thread = None
    vectorstore_in_assistant = None
    vectorstore_in_Thread = None

    github_username, github_token = Github_functions.QuantumCore_github_keys()


    
    AI_QuantumCore = AutenticateAgent.create_or_auth_AI(key, instructionQuantumCore, nameassistant, model_select, tools, vectorstore_in_assistant)
    
    

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Buscar informações do pull request
    pr_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    pr_response = requests.get(pr_url, headers=headers)

    if pr_response.status_code != 200:
        print(f"Erro ao buscar PR. Status: {pr_response.status_code}")
        return {"status": "error", "message": pr_response.json()}

    pr_data = pr_response.json()

    # Analisar o código no pull request
    code_url = pr_data['commits_url']
    commits_response = requests.get(code_url, headers=headers)
    if commits_response.status_code != 200:
        print(f"Erro ao buscar commits. Status: {commits_response.status_code}")
        return {"status": "error", "message": commits_response.json()}

    commits_data = commits_response.json()
    improvements = ""
    
    # Iterar pelos commits e realizar a análise
    for commit in commits_data:
        commit_message = commit['commit']['message']
        commit_url = commit['url']

        # Fazer a análise de melhoria via QuantumCore
        analysis_message = f"""
        Analisar este commit e decidir se o código está adequado ou se requer melhorias:
        Commit: {commit_message}
        URL: {commit_url}
        """
        response = ResponseAgent.ResponseAgent_message_with_assistants(analysis_message, Upload_1_file_in_thread, Upload_1_file_in_message, Upload_1_image_for_vision_in_thread, vectorstore_in_Thread, tools, AI_QuantumCore, model_select, adxitional_instructions, key)
        print(response)
        
        mensaxgem = f""" com base nessa analize responda a decisao de aprovar ou rejeitar o pull request 
        {response}\n
        caso a decisao seja rejeitar pull request sugira melhorias e motivos da rejeicao 
        """
        format = 'Responda a decisao de sim ou nao no formato JSON Exemplo: {"decisao": "sim ou nao..."}'
        mensagem = mensaxgem + format
        response = ResponseAgent.ResponseAgent_message_completions(mensagem, "", True)
        JSONformat = response["decisao"]
        if JSONformat == "sim":
            pass
        else:
            improvements += JSONformat

    if improvements:
        print("QuantumCore encontrou melhorias necessárias.")
        return {
            "status": "improvement_needed",
            "message": improvements
        }
    else:
        review_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/reviews"
        review_data = {
            "body": f"""Aprovado por QuantumCore.\n 
                    {response}
            """,
            "event": "APPROVE"
        }
        review_response = requests.post(review_url, json=review_data, headers=headers)
        if review_response.status_code == 200:
            print("Pull request aprovado com sucesso!")
            resultado = merge_pull_request(repo_owner, repo_name, pr_number, github_token)
            return {"status": "approved", "message": f"Pull request aprovado com sucesso. {resultado}"}
        else:
            print(f"Erro ao aprovar o PR. Status: {review_response.status_code}")
            return {"status": "error", "message": review_response.json()}
    
