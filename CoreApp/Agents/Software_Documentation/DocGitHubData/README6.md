
# Documentação para o GitHub

## Status da Documentação
- **Status**: Completa

## Seções da Documentação
- Introdução
- Instalação
- Uso
- Referência de API
- Contribuição
- Licença

### Introdução
O **Gerador de PDF em Python** é uma ferramenta que permite gerar arquivos PDF de forma dinâmica e personalizada. Com este gerador, você pode adicionar títulos e seções, facilitando a criação de documentos formatados.

### Instalação
Para instalar e utilizar o Gerador de PDF, siga os passos abaixo:

1. **Pré-requisitos**:
   - Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do [site oficial do Python](https://www.python.org/downloads/).

2. **Instalação da biblioteca**:
   - Instale a biblioteca `fpdf` que é necessária para a criação de PDFs com o seguinte comando:
   
   ```bash
   pip install fpdf
   ```

### Uso
Para utilizar o gerador de PDF, execute o seguinte comando no terminal:

```bash
python gerador_pdf.py
```

Siga as instruções exibidas no console:
1. Quando solicitado, informe o nome do arquivo em que deseja salvar (exemplo: `documento.pdf`).
2. Em seguida, forneça um título para o seu documento.
3. Você pode adicionar diversas seções digitando o título e conteúdo desejados para cada uma. Para finalizar a adição de seções, digite "sair".

### Referência de API
- **PDFGenerator**: Classe responsável pela criação do PDF.
    - `__init__()`: Inicializa um novo documento PDF com configurações iniciais.
    - `add_title(title)`: Adiciona um título centralizado ao PDF.
    - `add_section(section_title, content)`: Adiciona uma seção com título e conteúdo ao PDF.
    - `save_pdf(filename)`: Salva o arquivo PDF com o nome especificado.

### Contribuição
Contribuições são bem-vindas! Se você deseja contribuir com o projeto, siga estes passos:
1. Fork o repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Realize suas modificações e faça um commit:
   ```bash
   git commit -m "Descreva suas alterações"
   ```
4. Envie sua branch:
   ```bash
   git push origin minha-contribuicao
   ```
5. Abra um pull request no GitHub para que suas alterações sejam revisadas.

### Licença
Este projeto é licenciado sob a [MIT License](LICENSE). Consulte o arquivo `LICENSE` para mais detalhes sobre os direitos e limitações.