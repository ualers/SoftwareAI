
tools_QuantumCore = [
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
    },
    
    {
        "type": "function",
        "function": {
            "name": "add_projectmap_to_github",
            "description": "Realiza o upload dos arquivos do projeto, incluindo documentação, timeline, roadmap e análises.",
            "parameters": {
                "type": "object",
                "properties": {
                    "repo_name": {
                        "type": "string",
                        "description": "Nome do repositório no GitHub."
                    },
                    "timeline_file_path": {
                        "type": "string",
                        "description": "Caminho do arquivo de timeline do projeto."
                    },
                    "spreadsheet_file_path": {
                        "type": "string",
                        "description": "Caminho da planilha do projeto."
                    },
                    "pre_project_file_path": {
                        "type": "string",
                        "description": "Caminho do arquivo de pré-projeto."
                    },
                    "Roadmap_file_path": {
                        "type": "string",
                        "description": "Caminho do arquivo de Roadmap do projeto."
                    },
                    "analise_file_path": {
                        "type": "string",
                        "description": "Caminho do arquivo de análise do projeto."
                    },
                    "token": {
                        "type": "string",
                        "description": "Token de autenticação do GitHub para realizar operações na API."
                    }
                },
                "required": [
                    "repo_name",
                    "timeline_file_path",
                    "spreadsheet_file_path",
                    "pre_project_file_path",
                    "Roadmap_file_path",
                    "analise_file_path",
                    "token"
                ]
            }
        }
    }
    
        
]