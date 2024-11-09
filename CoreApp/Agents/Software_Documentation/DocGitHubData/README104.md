
# Documentação para o GitHub

## Introdução
O **Gerador de PDF em Python** é uma ferramenta que permite aos usuários criar arquivos PDF personalizados de forma fácil e prática. Este projeto é útil para gerar documentos que precisam de formatação e estrutura, como relatórios, propostas e currículos.

## Instalação
Para instalar e usar o Gerador de PDF, siga estes passos:

1. **Pré-requisitos**:
   - É necessário ter o Python instalado em seu sistema. Você pode fazer o download em [python.org](https://www.python.org/downloads/).

2. **Instalação da biblioteca `fpdf`**:
   - Abra o terminal e execute o seguinte comando para instalar a biblioteca `fpdf`:
   
   ```bash
   pip install fpdf
   ```

## Uso
Para utilizar o Gerador de PDF, execute o script `gerador_pdf.py`:

```bash
python gerador_pdf.py
```

1. Quando solicitado, forneça o nome do arquivo PDF que deseja criar (exemplo: `documento.pdf`). O sistema acrescentará a extensão `.pdf` automaticamente, se necessário.

2. Em seguida, digite o título do seu documento.

3. Você pode adicionar seções ao PDF, fornecendo um título e o conteúdo correspondente. Para encerrar a adição de seções, digite a palavra "sair".

## Referência de API
- **PDFGenerator**: Classe utilizada para gerar PDFs.
    - `__init__()`: Inicializa a instância do PDF com configurações padrão.
    - `add_title(title)`: Adiciona um título ao PDF, centralizado em negrito.
    - `add_section(section_title, content)`: Adiciona uma nova seção com título e conteúdo ao PDF.
    - `save_pdf(filename)`: Salva o conteúdo gerado em um arquivo PDF com o nome fornecido.

## Contribuição
Contribuições são bem-vindas! Para contribuir com o projeto, siga as etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações:
   
   ```bash
   git checkout -b minha-contribuicao
   ```

3. Realize suas modificações e faça um commit:
   
   ```bash
   git commit -m "Descrição das suas alterações"
   ```

4. Envie sua branch para o repositório:
   
   ```bash
   git push origin minha-contribuicao
   ```

5. Abra um pull request no GitHub para que suas alterações sejam revisadas.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE). Consulte o arquivo LICENSE para mais informações sobre direitos e limitações.