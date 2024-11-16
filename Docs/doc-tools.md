# Documentação das Ferramentas
Funções Disponíveis

## analyze_file
Analisa o conteúdo de um arquivo de texto.

### Parâmetros
- `file_path` (string, obrigatório): Caminho completo incluindo o nome do arquivo a ser analisado.

```
    {
        "type": "function",
        "function": {
            "name": "analyze_file",
            "description": "Analiza um arquivo txt",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Caminho com nome do arquivo"
                    }
                },
                "required": [
                    "file_path"
                ]
            }
        }
    },
```

## update_readme_to_github

Atualiza o arquivo README.md de um repositório no GitHub.

### Parâmetros
- `file_path_readme_improvements` (string, obrigatório): Caminho do arquivo README melhorado
- `repo_name` (string, obrigatório): Nome do repositório no GitHub
- `token` (string, obrigatório): Token de autenticação do GitHub para acesso à API
```
{
    "type": "function",
    "function": {
        "name": "update_readme_to_github",
        "description": "Atualiza o Readme do repositorio no github",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path_readme_improvements": {
                    "type": "string",
                    "description": "O Caminho do readme melhorado"
                },
                "repo_name": {
                    "type": "string",
                    "description": "O nome do repositorio do github"
                },
                "token": {
                    "type": "string",
                    "description": "Token de autenticação do GitHub para realizar operações na API."
                }

            },
            "required": [
                "file_path_readme_improvements",
                "repo_name",
                "token"
            ]
        }
    }
},
```


## save_TXT

Salva conteúdo em um arquivo de texto com diferentes modos de escrita.

### Parâmetros
- `string` (string, obrigatório): Conteúdo a ser salvo no arquivo
- `filexname` (string, obrigatório): Nome do arquivo
- `letra` (string, obrigatório): Modo de escrita
  - `'w'`: Cria novo arquivo ou sobrescreve existente
  - `'x'`: Cria novo arquivo, falha se já existir
  - `'a'`: Anexa conteúdo ao final do arquivo
- `path` (string, obrigatório): Diretório onde o arquivo será salvo
```

    {
        "type": "function",
        "function": {
            "name": "save_TXT",
            "description": "Salva um arquivo txt",
            "parameters": {
                "type": "object",
                "properties": {
                    "string": {
                        "type": "string",
                        "description": "O conteudo do txt"
                    },
                    "filexname": {
                        "type": "string",
                        "description": "O nome do txt"
                    },
                    "letra": {
                        "type": "string",
                        "description": " letra 'w' abre para escrita truncando o arquivo primeiro, letra 'x' cria um novo arquivo e abre-o para escrita, letra 'a' abre para escrita anexando ao final do arquivo se existir"
                    },
                    "path": {
                        "type": "string",
                        "description": "o caminho onde o txt sera salvo "
                    }

                },
                "required": [
                    "string",
                    "filexname",
                    "letra",
                    "path"
                ]
            }
        }
    },

```

## save_code

Salva arquivos de código em diferentes linguagens.

### Parâmetros
- `code_string` (string, obrigatório): Conteúdo do código
- `name_script` (string, obrigatório): Nome do arquivo
- `file_type` (string, obrigatório): Tipo do arquivo
  - Valores aceitos: `"html"`, `"js"`, `"css"`, `"py"`
- `path` (string, obrigatório): Diretório onde o arquivo será salvo
```
    {
        "type": "function",
        "function": {
            "name": "save_code",
            "description": "Salva 4 tipos de codigos html, js, css, py",
            "parameters": {
                "type": "object",
                "properties": {
                    "code_string": {
                        "type": "string",
                        "description": "O conteudo do codigo"
                    },
                    "name_script": {
                        "type": "string",
                        "description": "O nome do codigo"
                    },
                    "file_type": {
                        "type": "string",
                        "description": "o tipo de arquivo sendo eles html, js, css ou py "
                    },
                    "path": {
                        "type": "string",
                        "description": "o caminho onde o codigo sera salvo "
                    }

                },
                "required": [
                    "code_string",
                    "name_script",
                    "file_type",
                    "path"
                ]
            }
        }
    },
```

## execute_python_code

Executa um script Python.

### Parâmetros
- `filename` (string, obrigatório): Caminho completo do arquivo Python a ser executado
```
    {
        "type": "function",
        "function": {
            "name": "execute_python_code",
            "description": "Executa codigos py",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "O caminho junto ao nome do .py"
                    }
                },
                "required": [
                    "filename"
                ]
            }
        }
    }
```


## get_current_datetime

Retorna a data e hora atual em formato padronizado.

### Retorno
- String no formato "YYYY-MM-DD HH:MM:SS"
```
    {
        "type": "function",
        "function": {
            "name": "get_current_datetime",
            "description": "Retorna a data e hora atual no formato YYYY-MM-DD HH:MM:SS.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
```

## create_github_repo_and_upload

Cria um novo repositório no GitHub e faz upload inicial de documentação e código.

### Parâmetros
- `repo_name` (string, obrigatório): Nome do novo repositório
- `repo_description` (string, obrigatório): Descrição do repositório
- `readme_file_path` (string, obrigatório): Caminho do arquivo README.md
- `code_file_paths` (array de strings, obrigatório): Lista de caminhos dos arquivos Python
- `token` (string, obrigatório): Token de autenticação do GitHub
```
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

```

## add_projectmap_to_github

Realiza o upload de documentos de planejamento e análise do projeto para um repositório GitHub.

### Parâmetros
- `repo_name` (string, obrigatório): Nome do repositório
- `timeline_file_path` (string, obrigatório): Caminho do arquivo de timeline
- `spreadsheet_file_path` (string, obrigatório): Caminho da planilha do projeto
- `pre_project_file_path` (string, obrigatório): Caminho do arquivo de pré-projeto
- `Roadmap_file_path` (string, obrigatório): Caminho do arquivo de Roadmap
- `analise_file_path` (string, obrigatório): Caminho do arquivo de análise
- `token` (string, obrigatório): Token de autenticação do GitHub

```
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
```


## improve_code_and_create_pull_request

Implementa melhorias no código e cria um Pull Request no GitHub.

### Parâmetros
- `repo_owner` (string, obrigatório): Nome do proprietário do repositório
- `repo_name` (string, obrigatório): Nome do repositório
- `branch_name` (string, obrigatório): Nome da branch para as alterações
- `file_path` (string, obrigatório): Caminho do arquivo a ser melhorado
- `commit_message` (string, obrigatório): Mensagem descritiva do commit
- `improvements` (string, obrigatório): Código melhorado
- `pr_title` (string, obrigatório): Título do Pull Request
- `token` (string, obrigatório): Token de autenticação do GitHub
```
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
                    "pr_title": {
                        "type": "string",
                        "description": "Titulo do Pull request."
                    },
                    "token": {
                        "type": "string",
                        "description": "Token de autenticação do GitHub."
                    }
                },
                "required": ["repo_owner", "repo_name", "branch_name", "file_path", "commit_message", "improvements", "pr_title",  "token"]
            }
        }
    }

```