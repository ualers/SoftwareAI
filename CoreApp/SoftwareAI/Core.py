#########################################
# IMPORT SoftwareAI Functions
from .Functions._init_functions_ import *
#########################################
# IMPORT SoftwareAI Functions Submit Outputs
from .Functions_Submit_Outputs._init_submit_outputs_ import _init_output_
#########################################
# IMPORT SoftwareAI Agents 
from .._init_agents_ import *
#########################################
# IMPORT SoftwareAI Libs 
from .._init_libs_ import *
#########################################
# IMPORT SoftwareAI Keys 
from .._init_keys_ import *
#########################################


key_api = OpenAIKeys.keys_openai()
client = OpenAI(
    api_key=key_api,
)

app1, bucket = keys_app_1()

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
        
    def create_or_auth_thread(key, file_in_thread: str, attachavectorstoretoThreads: str, code_interpreter_in_thread=None):
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
            elif code_interpreter_in_thread:
                thread = client.beta.threads.create(
                    tool_resources={"code_interpreter": {"file_ids": code_interpreter_in_thread}}
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
                        str(thread.id),
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
            "model": "gpt-4o-mini",  
            "messages": mensagem,
            "store": True,
            "max_tokens": 16_384,
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
        
    def ResponseAgent_message_with_assistants(mensagem,
                                            Upload_1_file_in_thread,
                                            Upload_1_file_in_message,
                                            Upload_1_image_for_vision_in_thread,
                                            Upload_list_for_code_interpreter_in_thread,
                                            vectorstore_in_Thread,
                                            tools, agent_id,
                                            model_select, aditional_instructions,
                                            key):
        
        """ 
        :param mensagem: This argument is the desired message that the agent responds to | If not use = None
            
        :param Upload_1_file_in_thread: This argument is the location of the file that will be uploaded to the thread | If not use = None
        
        :param Upload_1_file_in_message: This argument is the location of the file that will be uploaded along with the message | If not use = None
        
        :param agent_id: This argument is the id of the authenticated or created agent
            
        :param model_select: This argument is the AI model that the agent will use
        
        :param aditional_instructions: This argument is an additional instruction to the agent's behavior | If not use = None

        :param key: this is the key that represents the agent in the database


        
        """

        
        if Upload_1_image_for_vision_in_thread:
            code_interpreter_in_thread = None
            Upload_1_file_in_thread = None
            with open(Upload_1_image_for_vision_in_thread, "rb") as image_file:
                file = client.files.create(
                    file=image_file,
                    purpose="vision"
                )
            

                threead_id = AutenticateAgent.create_or_auth_thread(key, Upload_1_file_in_thread, vectorstore_in_Thread, code_interpreter_in_thread)
                #flag = Agent_files.upload_image_for_vision_in_thread(Upload_1_image_for_vision_in_thread, threead_id)
                #print(flag)

                message = client.beta.threads.messages.create(
                    thread_id=threead_id,
                    role="user",
                    content=[
                            {
                                "type": "text",
                                "text": f"""{mensagem}"""
             
                            },
                            {
                                "type": "image_file",
                                "image_file": {"file_id": file.id} 
                            }
                        ]
,
                    #attachments=[{ "file_id": file.id }]  
                )



        if Upload_1_file_in_message:
            code_interpreter_in_thread = None
            message_file = client.files.create(
                file=open(Upload_1_file_in_message, "rb"), purpose="assistants"
            )
            threead_id = AutenticateAgent.create_or_auth_thread(key, Upload_1_file_in_thread, vectorstore_in_Thread, code_interpreter_in_thread)


            message = client.beta.threads.messages.create(
                thread_id=threead_id,
                role="user",
                content=mensagem,
                attachments=[{ "file_id": message_file.id }]  
            )
            


        elif Upload_1_file_in_thread:
            code_interpreter_in_thread = None
            message_file = client.files.create(
                file=open(Upload_1_file_in_thread, "rb"), purpose="assistants"
            )
            file_in_thread = message_file.id 
            threead_id = AutenticateAgent.create_or_auth_thread(key, file_in_thread, vectorstore_in_Thread, code_interpreter_in_thread)

            if Upload_1_image_for_vision_in_thread:
                flag = Agent_files.upload_image_for_vision_in_thread(Upload_1_image_for_vision_in_thread, threead_id)
                print(flag)

        elif Upload_list_for_code_interpreter_in_thread:
            list_file_id = []
            for path in Upload_list_for_code_interpreter_in_thread:
                file = client.files.create(
                    file=open(path, "rb"),
                    purpose='assistants'
                )
                list_file_id.append(file.id)
            code_interpreter_in_thread = list_file_id
            file_in_thread = None
            threead_id = AutenticateAgent.create_or_auth_thread(key, file_in_thread, vectorstore_in_Thread, code_interpreter_in_thread)

            if Upload_1_image_for_vision_in_thread:
                flag = Agent_files.upload_image_for_vision_in_thread(Upload_1_image_for_vision_in_thread, threead_id)
                print(flag)

        #if Uploadfile_in_message is None or Uploadfile_in_thread is None or Uploadfile_in_message and Uploadfile_in_thread is None:
        else:
            code_interpreter_in_thread = None
            threead_id = AutenticateAgent.create_or_auth_thread(key, Upload_1_file_in_thread, vectorstore_in_Thread, code_interpreter_in_thread)
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
        tool_outputs = []
        while True:
            time.sleep(2)
            run_status = client.beta.threads.runs.retrieve(
                thread_id=threead_id,
                run_id=run.id
            )
            try:

                print(run_status.usage.total_tokens)
                print(run_status.usage.prompt_tokens)
                print(run_status.usage.completion_tokens)
            except:
                pass
            if run_status.status == 'requires_action':
                for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
                    if tool_call.type == 'function':
                        
                        function_name = tool_call.function.name
                        function_arguments = tool_call.function.arguments
                        print(function_name)
                        print(function_arguments)
                        print(tool_call)
                        print(tool_call.id)

                        
                        _init_output_(function_name,
                                function_arguments,
                                tool_call,
                                threead_id,
                                client,
                                run)

            elif run_status.status == 'completed':
                break
            elif run_status.status == 'failed':
                pass
            elif run_status.status == 'in_progress':
                print("thinking...")
            else:
                contador += 1 
                if contador == 15:
                    break
                print("Aguardando a execução ser completada...")

        messages = client.beta.threads.messages.list(
            thread_id=threead_id
        )
        file_id = None
        contador23  = 0
        for message in messages:
            
            for mensagem_contexto in message.content:
                print(message.content)
                valor_texto = mensagem_contexto.text.value
                
                # try:
                    
                #     try:
                #         annotations = mensagem_contexto.text.annotations
                #     except:
                #         annotations = None
                # except:
                #     try:
                #         valor_texto = message.content.index(1)
                #     except:
                #         valor_texto = None
                #     try:
                #         annotations = mensagem_contexto.image_file.file_id
                #     except:
                #         annotations = None
                return valor_texto
            # contador23 += 1
            # if 
            #break


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

    def auth_or_create_vectorstore(name_for_vectorstore: str, file_paths=None, update1newfiles=None):
        """Create or auth or update 1 files in vector store \n 
        O tamanho máximo por arquivo é 512 MB. Cada arquivo deve conter no máximo 5.000.000 de tokens por arquivo (calculado automaticamente quando você anexa um arquivo).
        \n 
        name_for_vectorstore = "teste"\n 
        file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"]"""

        try:
            ref1 = db.reference(f'ai_org_vector_store/User_{name_for_vectorstore}', app=app1)
            data1 = ref1.get()
            vector_store_id = data1['vector_store_id']
            if update1newfiles:
                update1newfile = open(update1newfiles, "rb")
                client.beta.vector_stores.files.upload(
                    vector_store_id=vector_store_id, file=update1newfile
                )
            return str(vector_store_id)
        except:
            vector_store = client.beta.vector_stores.create(name=name_for_vectorstore)
            if update1newfiles:
                update1newfile = open(update1newfiles, "rb")
                client.beta.vector_stores.files.upload(
                    vector_store_id=vector_store.id, file=update1newfile
                )
            elif file_paths:
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

    def update_multiple_env_variables(updates, env):
        # Lê o conteúdo atual do .env
        with open(env, "r") as file:
            lines = file.readlines()
        
        # Abre o .env para escrita e modifica as linhas conforme necessário
        with open(env, "w") as file:
            for line in lines:
                # Extrai a chave de cada linha no .env
                key = line.split("=")[0]
                
                # Verifica se a chave precisa ser atualizada
                if key in updates:
                    file.write(f"{key}={updates[key]}\n")
                else:
                    file.write(line)
        return True

    def update_env_variable(key, value):
        # Lê o conteúdo atual do .env
        with open(".env", "r") as file:
            lines = file.readlines()
        
        # Modifica a linha que contém a variável
        with open(".env", "w") as file:
            for line in lines:
                if line.startswith(key + "="):
                    file.write(f"{key}={value}\n")
                else:
                    file.write(line)

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
        # Garantir que o diretório existe
        os.makedirs(os.path.dirname(filexname), exist_ok=True)
        
        # Salvar o conteúdo no arquivo
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
        except:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    return content
            except:
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
        except:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    return content
            except:
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        return content
                except UnicodeDecodeError:
                    try:
                        file_path = file_path.replace(" ", "").replace("\n", "")
                        with open(file_path, 'r', ) as file:
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
