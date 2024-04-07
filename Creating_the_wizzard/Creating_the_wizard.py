
from openai import OpenAI
import requests



from selenium_stealth import stealth
from distutils.dir_util import copy_tree
import pygetwindow as gw
import requests
import undetected_chromedriver as uc
import threading
import random
import subprocess
import psutil
import os
import json
import sys
import hashlib
import string
import platform
import pyautogui
import time
import re
import base64
import uuid
import shutil
import time
from datetime import datetime

import telegram
from telegram.ext import Updater, CommandHandler, JobQueue
from telegram.ext import Updater, CommandHandler, Job
from firebase_admin import credentials, initialize_app, storage
from keys_def import chaves

bot_token, CANAL_ID = chaves.keys_bot_telegram()
key_api = chaves.chaves_open_ai()
client = OpenAI(
    api_key=key_api,
)

### Module creating new assistant ###    
def creating_new_assistant():
    file = client.files.create(
        file=open("doc.csv", "rb"),
        purpose='assistants'
    )
    assistant = client.beta.assistants.create(
        name="Suporte do software", 
        instructions="responda as perguntas feitas com base nas respostas do arquivo  responda somente oque foi perguntado pelos clientes e nao todas as perguntas do arquivo  se o cliente perguntar algo que nao está no arquivo peça desculpas e diga que ainda nao temos respostas.",
        tools=[{"type": "retrieval"}],
        model="gpt-3.5-turbo-1106",
        file_ids=[file.id]
    )
    print([file.id])
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content='''oi''',
        file_ids=[file.id]
    )
    print(thread.id)
    print(assistant.id)
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="responda as perguntas feitas com base nas respostas do arquivo  responda somente oque foi perguntado pelos clientes e nao todas as perguntas do arquivo  se o cliente perguntar algo que nao está no arquivo peça desculpas e diga que ainda nao temos respostas.",
        tools=[{"type": "retrieval"}],
        model="gpt-3.5-turbo-1106"
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run_status.status == 'completed': 
            break
        else:
            print("Aguardando a execução ser completada...")
        time.sleep(2)  
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    for message in messages:
        for mensagem_contexto in message.content:  
            valor_texto = mensagem_contexto.text.value
            print(valor_texto)
            thread_id = thread.id
            assistant_id = assistant.id
            run_id = run.id
            name = "Assistente"
            diretorio_script = os.path.dirname(os.path.abspath(__file__))
            nome_arquivo_gerenciador = os.path.join(diretorio_script, 'gerenciador_agente_1.txt')
            with open('gerenciador_agente_1.txt', 'a') as arquivo:
                arquivo.write(f'Nome: {name} \n')
                arquivo.write(f'thread_id:{thread_id}\n')
                arquivo.write(f'assistant_id:{assistant_id}\n')
                arquivo.write(f'------------------------\n')
        break


### Modulo teste 1 ###
def teste_mensagem_com_assistente_existente(mensagem, threead_id, asst):
    message = client.beta.threads.messages.create(
        thread_id=threead_id,
        role="user",
        content=mensagem
    )
    run = client.beta.threads.runs.create(
        thread_id=threead_id,
        assistant_id=asst,
        
    )
    while True:
        time.sleep(2)  
        run_status = client.beta.threads.runs.retrieve(
        thread_id=threead_id,
        run_id=run.id
        )
        if run_status.status == 'completed': 
            break
        elif run_status.status == 'failed': 
            print("Falha")
            break
        elif run_status.status == 'in_progress': 
            print("in_progress")
            
        else:
            print("Aguardando a execução ser completada...")
        
    messages = client.beta.threads.messages.list(
    thread_id=threead_id
    )
    for message in messages:
        for mensagem_contexto in message.content:
            valor_texto = mensagem_contexto.text.value
            
            return valor_texto
            
        break

asst = 'asst_pmiTNPaRaHZpMtBrFwjTJsKg'
threead_id = 'thread_Ip7LB65PIgB3CJoyRvUqJImF'

pergunta_do_cliente = "o modo download funciona?"
#resposta_do_funcionario = teste_mensagem_com_assistente_existente(pergunta_do_cliente, threead_id, asst)
#print(resposta_do_funcionario)

criando_um_novo_assistente()








