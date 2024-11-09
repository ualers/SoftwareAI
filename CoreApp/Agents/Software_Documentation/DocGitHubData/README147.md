
# Documentação para o GitHub

## Introdução
O **Gerador de PDF em Python** é uma ferramenta simples que permite aos usuários criar arquivos PDF personalizados com facilidade. Utilizando a biblioteca `fpdf`, o software possibilita a adição de títulos e seções, facilitando a organização do conteúdo em documentos formatados.

## Instalação
Para instalar e usar o Gerador de PDF, siga as etapas abaixo:

1. **Pré-requisitos**:
   - Certifique-se de que o Python está instalado na sua máquina. Caso não tenha, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. **Instalação da biblioteca `fpdf`**:
   - Execute o seguinte comando no terminal para instalar a biblioteca:
   
   ```bash
   pip install fpdf
   ```

## Uso
Para utilizar o Gerador de PDF:

1. Execute o script `gerador_pdf.py` no terminal:
   
   ```bash
   python gerador_pdf.py
   ```

2. Quando solicitado, informe o nome do arquivo em que deseja salvar (exemplo: `documento.pdf`). O sistema irá garantir que a extensão `.pdf` seja adicionada, se não estiver presente.

3. Insira o título do documento quando solicitado.

4. Você pode adicionar seções ao PDF digitando o título da seção e o conteúdo correspondente. Para encerrar a adição de seções, digite "sair".

## Referência de API
- **PDFGenerator**: Classe principal que gerencia a criação do PDF.
    - `__init__()`: Inicializa a instância do gerador de PDF com configurações padrão.
    - `add_title(title)`: Adiciona um título ao PDF, centralizado e em negrito.
    - `add_section(section_title, content)`: Adiciona uma nova seção com um título e conteúdo ao PDF.
    - `save_pdf(filename)`: Salva o PDF gerado com o nome especificado.

## Contribuição
Contribuições são bem-vindas! Para contribuir com o projeto, siga estas etapas:

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
5. Abra um pull request para que suas alterações sejam revisadas.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE). Para mais informações sobre direitos e limitações, consulte o arquivo `LICENSE` no repositório.