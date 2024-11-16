
#########################################
# IMPORT SoftwareAI Libs 
from CoreApp._init_libs_ import *
#########################################


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


    # Adicionando colaborador com permissões de administrador
    collaborator_url = f"https://api.github.com/repos/A-I-O-R-G/{repo_name}/collaborators/NexGenCoder756"

    collaborator_data = {
        "permission": "admin"
    }

    collaborator_response = requests.put(collaborator_url, headers=headers, json=collaborator_data)

    if collaborator_response.status_code == 201 or collaborator_response.status_code == 204:
        print(f"Colaborador 'NexGenCoder756' adicionado com sucesso com permissões de administrador.")
    else:
        print(f"Falha ao adicionar colaborador. Status: {collaborator_response.status_code}, Resposta: {collaborator_response.json()}")
        return {"status": "error", "message": collaborator_response.json()}
    

    # Adicionando colaborador com permissões de administrador
    collaborator_url = f"https://api.github.com/repos/A-I-O-R-G/{repo_name}/collaborators/CloudArchitectt"

    collaborator_data = {
        "permission": "admin"
    }

    collaborator_response = requests.put(collaborator_url, headers=headers, json=collaborator_data)

    if collaborator_response.status_code == 201 or collaborator_response.status_code == 204:
        print(f"Colaborador 'CloudArchitectt' adicionado com sucesso com permissões de administrador.")
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


