import struct
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Mensagem_receive(QThread):
    message_received =  Signal(str)

    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        self.running = True

    def run(self):
        
        while self.running:
            try:
                # Primeiro, recebemos o tamanho da mensagem (4 bytes para um inteiro)
                message_size = self.receive_message_size(self.sock)
                if message_size:
                    full_message = self.receive_full_message(self.sock, message_size)
                    if full_message:
                        self.message_received.emit(f'<div style="display: flex; justify-content: flex-start;">'
                        f'<div style="color: black; padding: 8px; border-radius: 8px; '
                        f'margin: 5px; max-width: 70%;"><b>Chat:</b> {full_message}</div>'
                        f'</div>')
                        #self.message_received.emit(full_message)
            except Exception as e:
                print(f"Erro: {e}")
                self.running = False

    def receive_message_size(self, sock):
        """Recebe os primeiros 4 bytes, que contêm o tamanho da mensagem."""
        raw_size = sock.recv(4)
        if not raw_size:
            return None
        # Descompacta os 4 bytes em um inteiro
        message_size = struct.unpack('!I', raw_size)[0]  # '!I' -> Unsigned int (4 bytes, network byte order)
        return message_size

    def receive_full_message(self, sock, message_size):
        """Recebe a mensagem completa com base no tamanho fornecido."""
        chunks = []
        bytes_received = 0

        while bytes_received < message_size:
            chunk = sock.recv(min(1024, message_size - bytes_received))
            if not chunk:
                break
            chunks.append(chunk)
            bytes_received += len(chunk)

        return b''.join(chunks).decode('utf-8')

    def stop(self):
        self.running = False
        self.quit()
        self.wait()
