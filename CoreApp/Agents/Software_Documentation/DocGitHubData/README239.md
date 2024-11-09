
### Documentação para o GitHub

#### Status da Documentação
A documentação está completa e abrange todos os aspectos necessários para o entendimento e uso do projeto.

#### Seções da Documentação
- **Introdução**  
- **Instalação**  
- **Uso**  
- **Referência de API**  
- **Contribuição**  
- **Licença**  

#### Introdução
O **Gerador de PDF em Python** é uma ferramenta que permite a criação de documentos PDF personalizados. Através deste software, os usuários podem facilmente adicionar títulos e seções, proporcionando uma formatação organizada para relatórios, propostas e outros documentos.

#### Instalação
Para instalar e usar o Gerador de PDF, siga as instruções abaixo:

1. **Pré-requisitos**:  
   - Você deve ter o Python instalado no seu sistema. Caso ainda não tenha, faça o download em [python.org](https://www.python.org/downloads/).

2. **Instalação da biblioteca `fpdf`**:  
   - Instale a biblioteca necessária utilizando o comando a seguir no terminal:
   ```bash
   pip install fpdf
   ```

#### Uso
Para utilizar o Gerador de PDF:

1. Execute o script Python no terminal:
   ```bash
   python gerador_pdf.py
   ```

2. Quando solicitado, insira o nome do arquivo para salvar o PDF (exemplo: `documento.pdf`). O sistema garantirá que a extensão `.pdf` seja adicionada.

3. Forneça o título do seu documento quando solicitado.

4. Adicione seções ao documento digitando o título e o conteúdo correspondente. Para finalizar a entrada de seções, digite "sair".

#### Referência de API
- **PDFGenerator**: Classe responsável pela criação do PDF.  
    - `__init__()`: Inicializa o gerador de PDF com configurações padrão.  
    - `add_title(title)`: Adiciona um título ao PDF, centralizado e em negrito.  
    - `add_section(section_title, content)`: Adiciona uma seção ao PDF com um título e conteúdo especificados.  
    - `save_pdf(filename)`: Salva o PDF no disco com o nome fornecido e exibe uma mensagem de sucesso.

#### Contribuição
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
5. Abra um pull request no GitHub.

#### Licença
Este projeto está licenciado sob a [MIT License](LICENSE). Para mais detalhes, consulte o arquivo `LICENSE` no repositório.