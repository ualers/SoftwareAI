# Gerador de PDF em Python

Um simples gerador de PDF em Python que permite criar documentos organizados em seções, com títulos e conteúdo customizáveis. 

## Instalação

Para utilizar este software, você precisará ter Python instalado e a biblioteca FPDF. Siga os passos abaixo:

1. Instale a biblioteca FPDF usando o seguinte comando:

   ```bash
   pip install fpdf
   ```

## Uso

1. Execute o script:

   ```bash
   python nome_do_script.py
   ````

2. Siga as instruções exibidas no terminal:
   - Digite o nome do arquivo para salvar (ex: `documento.pdf`).
   - Insira o título do seu documento.
   - Para adicionar seções, digite o título da seção e o conteúdo. Para finalizar a adição de seções, digite 'sair'.

## Referência de API

### PDFGenerator

- **Construtor**: `PDFGenerator()`
  - Inicializa uma nova instância do gerador de PDF e configura a página automática com margem.

- **Método**: `add_title(title)`
  - `title`: (str) O título do documento a ser adicionado ao PDF.

- **Método**: `add_section(section_title, content)`
  - `section_title`: (str) O título da seção que será adicionada ao documento.
  - `content`: (str) O conteúdo que será incluído na seção.

- **Método**: `save_pdf(filename)`
  - `filename`: (str) O nome do arquivo para salvar o PDF. Exibe uma mensagem de confirmação ao salvar.

## Contribuição

Contribuições são bem-vindas! Você pode contribuir de várias maneiras, incluindo melhorias de código, correções de bugs, ou adicionando novos recursos. Sinta-se à vontade para fazer um fork do repositório e enviar pull requests.

### Instruções para Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b minha-feature`).
3. Faça as suas alterações e commit (`git commit -m 'Adicionei uma nova feature'`).
4. Faça push para a branch (`git push origin minha-feature`).
5. Abra uma pull request.

## Licença

Esse projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE.md para mais detalhes.
