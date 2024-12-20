
#########################################
# IMPORT SoftwareAI Core
from ..._init_core_ import *
#########################################
# IMPORT SoftwareAI Libs 
from ..._init_libs_ import *
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




class SoftwareDevelopment_NexGenCoder:
    def __init__(self):
        pass


        ##############################################################################################
    def AI_NexGenCoder(
                    self,
                    repo_name,
                    pr_number,
                    ):

        key = "AI_NexGenCoder_Desenvolvedor_Senior_de_Software_em_Python"
        nameassistant = "AI NexGenCoder Desenvolvedor Senior de Software em Python"
        model_select = "gpt-4o-mini-2024-07-18"


        Upload_1_file_in_thread = None
        Upload_1_file_in_message = None
        Upload_1_image_for_vision_in_thread = None
        vectorstore_in_assistant = None
        vectorstore_in_Thread = None
        Upload_list_for_code_interpreter_in_thread = None

        github_username, github_token = GithubKeys.NexGenCoder_github_keys()

        AI_NexGenCoder = AutenticateAgent.create_or_auth_AI(key, instructionNexGenCoder, nameassistant, model_select, tools_NexGenCoder, vectorstore_in_assistant)
        

        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Buscar informações do pull request
        pr_url = f"https://api.github.com/repos/A-I-O-R-G/{repo_name}/pulls/{pr_number}"
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

            # Fazer a análise de melhoria via NexGenCoder
            analysis_message = f"""
            Analisar este commit e decidir se o código está adequado ou se requer melhorias:
            Commit: {commit_message}
            URL: {commit_url}
            """
            response = ResponseAgent.ResponseAgent_message_with_assistants(analysis_message,
                                                                    Upload_1_file_in_thread, Upload_1_file_in_message,
                                                                    Upload_1_image_for_vision_in_thread,
                                                                    Upload_list_for_code_interpreter_in_thread,
                                                                    vectorstore_in_Thread,
                                                                    tools_NexGenCoder,  AI_NexGenCoder, model_select, adxitional_instructions_NexGenCoder, key)
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
            print("NexGenCoder encontrou melhorias necessárias.")
            return {
                "status": "improvement_needed",
                "message": improvements
            }
        else:
            review_url = f"https://api.github.com/repos/A-I-O-R-G/{repo_name}/pulls/{pr_number}/reviews"
            review_data = {
                "body": f"""Aprovado por NexGenCoder.\n 
                        {response}
                """,
                "event": "APPROVE"
            }
            review_response = requests.post(review_url, json=review_data, headers=headers)
            if review_response.status_code == 200:
                print("Pull request aprovado com sucesso!")
                resultado = self.merge_pull_request("A-I-O-R-G", repo_name, pr_number, github_token)
                return {"status": "approved", "message": f"Pull request aprovado com sucesso. {resultado}"}
            else:
                print(f"Erro ao aprovar o PR. Status: {review_response.status_code}")
                return {"status": "error", "message": review_response.json()}
        











    def merge_pull_request(self, repo_owner: str, repo_name: str, pr_number: int, token: str):
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
            "commit_message": "Merge realizado automaticamente pelo NexGenCoder.",
            "merge_method": "merge"  # ou 'squash' ou 'rebase', se preferir outros métodos de merge
        }

        merge_response = requests.put(merge_url, json=merge_data, headers=headers)

        if merge_response.status_code == 200:
            print("Merge realizado com sucesso!")
            return {"status": "merged", "message": "Pull request foi mergeado com sucesso."}
        else:
            print(f"Erro ao fazer merge. Status: {merge_response.status_code}")
            return {"status": "error", "message": merge_response.json()}