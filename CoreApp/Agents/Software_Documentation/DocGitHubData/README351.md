
# Documentação para o GitHub

## Introdução
O **Organizador de Arquivos** é um script Python que facilita a organização de arquivos em um diretório. Ele classifica arquivos com base em suas extensões, criando pastas correspondentes para cada tipo de arquivo e também remove duplicatas no diretório especificado.

## Instalação
Para instalar e executar o Organizador de Arquivos, siga as etapas abaixo:

1. **Pré-requisitos**:
   - Você deve ter o Python instalado em seu sistema. Caso não tenha, baixe a versão mais recente em [python.org](https://www.python.org/downloads/).

2. **Download do script**:
   - Faça o download do script `file_organizer.py` e salve-o em um diretório de sua escolha.

## Uso
Para utilizar o Organizador de Arquivos:

1. Execute o script através do terminal:
   ```bash
   python file_organizer.py
   ```

2. Insira o caminho do diretório que você deseja organizar quando solicitado.

3. O script irá:
   - Classificar os arquivos no diretório, movendo-os para pastas baseadas em suas extensões.
   - Remover arquivos duplicados do diretório.

## Referência de API
- **FileOrganizer**: Classe principal responsável pela organização de arquivos.
   - `__init__(directory)`: Inicializa a instância da classe, definindo o diretório a ser organizado.
   - `classify_files()`: Classifica e move arquivos com base em suas extensões.
   - `create_folders_and_move()`: Cria pastas para cada tipo de arquivo e move os arquivos para suas respectivas pastas.
   - `remove_duplicates()`: Remove arquivos duplicados do diretório.

## Contribuição
Contribuições são bem-vindas! Para contribuir com o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Realize suas modificações e faça um commit:
   ```bash
   git commit -m "Descrição das suas alterações"
   ```
4. Envie sua branch:
   ```bash
   git push origin minha-contribuicao
   ```
5. Abra um pull request para que suas alterações sejam revisadas.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE). Para mais detalhes, consulte o arquivo `LICENSE` no repositório.