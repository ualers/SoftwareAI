
# Documentação Detalhada

## 1. Introdução
Este software permite transcrever o áudio de vídeos do YouTube e gerar um arquivo PDF contendo a transcrição. Ele utiliza a biblioteca `whisper` para a transcrição do áudio, `pytube` para baixar o áudio do vídeo e `FPDF` para a criação do PDF.

## 2. Instalação
Para instalar as bibliotecas necessárias, utilize o seguinte comando:
```bash
pip install pytube pydub torch torchvision torchaudio fpdf
```
**Nota:** O `whisper` pode ser instalado diretamente com `pip install git+https://github.com/openai/whisper.git` se não estiver disponível via pip.

## 3. Uso
- Execute o script.
- O programa solicitará a URL do vídeo do YouTube que você deseja processar.
- O PDF resultante será salvo como `Transcricao_Tutorial_YouTube.pdf`.

Exemplo de como rodar o script:
```bash
python script.py
```

## 4. Referência de API
- **PDFGenerator**: Classe responsável pela criação de PDFs.
  - `__init__(self, title)`: Inicializa o PDF com um título.
  - `add_text(self, text)`: Adiciona texto ao PDF.
  - `save(self, filename)`: Salva o PDF com o nome especificado.

- `download_audio(youtube_url)`: Baixa o áudio de um vídeo do YouTube e retorna o caminho do arquivo de áudio.
  - Parâmetro: `youtube_url` (str): URL do vídeo do YouTube.

- `transcribe_audio(audio_path)`: Transcreve o áudio utilizando o modelo Whisper e retorna o texto transcrito.
  - Parâmetro: `audio_path` (str): Caminho do arquivo de áudio.

## 5. Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer fork do repositório e enviar suas melhorias.

## 6. Licença
Este projeto é licenciado sob a MIT License. Veja o arquivo LICENSE para mais informações.