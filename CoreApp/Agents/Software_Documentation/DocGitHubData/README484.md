
# Documentação para o GitHub

## Status da Documentação
- **Status:** Completa

## Seções da Documentação
1. **Introdução**
2. **Instalação**
3. **Uso**
4. **Referência de API**
5. **Contribuição**
6. **Licença**

## Introdução
O **Organizador de Arquivos** é um script Python que ajuda a organizar arquivos em um diretório, classificando-os com base em suas extensões. Além disso, o software remove arquivos duplicados e gera um relatório das operações realizadas. Essa ferramenta é útil para manter a ordem em pastas cheias de arquivos variados.

## Instalação
Para instalar e usar o Organizador de Arquivos, siga estas etapas:

1. **Pré-requisitos**:
   - Certifique-se de que você tem o Python instalado no seu sistema. Se necessário, baixe a última versão em [python.org](https://www.python.org/downloads/).

2. **Download do Script**:
   - Salve o código do script acima em um arquivo chamado `file_organizer.py`.

## Uso
Para utilizar o Organizador de Arquivos, siga estes passos:

1. Execute o script no terminal:
   ```bash
   python file_organizer.py
   ```

2. Quando solicitado, insira o caminho do diretório que deseja organizar.

3. O script executará as seguintes operações:
   - Classificará os arquivos no diretório, movendo-os para pastas com base em suas extensões.
   - Removerá arquivos duplicados encontrados.
   - Gerará um relatório simples mostrando quantos arquivos foram organizados.

## Referência de API
- **FileOrganizer**: Classe principal responsável pela organização dos arquivos.
    - `__init__(directory)`: Inicializa a classe com o diretório fornecido.
    - `classify_files()`: Classifica os arquivos no diretório por suas extensões.
    - `create_folders_and_move()`: Cria pastas para cada extensão encontrada e move os arquivos para suas respectivas pastas.
    - `remove_duplicates()`: Remove arquivos duplicados do diretório.
    - `generate_report()`: Gera um relatório simples sobre as operações realizadas.

## Contribuição
Se você deseja contribuir com este projeto, siga as etapas abaixo:

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
5. Abra um pull request no GitHub.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE). Consulte o arquivo LICENSE para mais informações sobre direitos e limitações.