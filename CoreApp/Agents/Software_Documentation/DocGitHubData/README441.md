
# Documentação para o GitHub

## Status da Documentação
- **Status**: Completa  

## Tabelas de Conteúdo  
- [Introdução](#introdução)  
- [Instalação](#instalação)  
- [Uso](#uso)  
- [Referência de API](#referência-de-api)  
- [Contribuição](#contribuição)  
- [Licença](#licença)  

## Introdução  
O **Organizador de Arquivos** é um script Python que organiza arquivos em um diretório com base em suas extensões. Ele cria pastas correspondentes para cada tipo de arquivo, move os arquivos para essas pastas e também remove arquivos duplicados. Este projeto é útil para manter a organização e facilitar o gerenciamento de arquivos.

## Instalação  
Para instalar e usar o Organizador de Arquivos, siga as instruções abaixo:

1. **Pré-requisitos**:  
   - Você precisa ter o Python instalado em sua máquina. Caso ainda não tenha, faça o download de uma versão recente em [python.org](https://www.python.org/downloads/).

2. **Download do Script**:  
   - Salve o código fornecido acima em um arquivo chamado `file_organizer.py`.

## Uso  
Para usar o Organizador de Arquivos, siga estes passos:

1. Execute o script em um terminal:  
   ```bash
   python file_organizer.py
   ```  

2. Quando solicitado, digite o caminho do diretório que você deseja organizar.

3. O script realizará as seguintes operações:  
   - Classificará os arquivos por extensões e os moverá para pastas específicas.  
   - Removerá arquivos duplicados encontrados no diretório.  
   - Gerará um relatório informando sobre a organização realizada.

## Referência de API  
- **FileOrganizer**: Classe principal responsável pela organização dos arquivos.  
    - `__init__(directory)`: Inicializa a classe com o diretório a ser organizado.  
    - `classify_files()`: Classifica e organiza os arquivos por extensão.  
    - `create_folders_and_move()`: Cria pastas para cada extensão de arquivo e move os arquivos para as pastas correspondentes.  
    - `remove_duplicates()`: Remove arquivos duplicados do diretório com base em seus nomes.  
    - `generate_report()`: Gera um relatório da organização realizada, informando quantas pastas foram criadas.

## Contribuição  
Se você deseja contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do repositório.  
2. Crie uma nova branch para suas alterações:  
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
5. Abra um pull request no GitHub para que suas alterações sejam revisadas.

## Licença  
Este projeto está licenciado sob a [MIT License](LICENSE). Para mais detalhes, consulte o arquivo LICENSE no repositório.