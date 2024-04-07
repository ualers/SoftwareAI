
import time
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, Filters
from openai import OpenAI
from keys_def import chaves
key_api = chaves.chaves_open_ai()
TOKEN, CHANNEL_ID = chaves.keys_bot_telegram()

client = OpenAI(
    api_key=key_api,
)

emojis = ['😊', '🤖', '🚀', '💡', '🎉']
def enviar_resposta_com_emoji(resposta):
    emoji = random.choice(emojis)  
    resposta_com_emoji = f"{emoji} {resposta}"  
    return resposta_com_emoji

def start(update, context):
    update.message.reply_text('Olá meu nome é Usuporte! Como posso ajudar você?')

def reply_message(update, context):
    user_message = update.message.text
    asst, threead_id = chaves.asst_e_threead()
    file_idx = chaves.file_id()
    ferramentas = chaves.ferramentas()
    modelo_de_IA = chaves.modelo_de_ia()

    openai_response = teste_mensagem_com_assistente_existente(user_message, threead_id, asst, file_idx, ferramentas, modelo_de_IA)
    openai_response_com_emog = enviar_resposta_com_emoji(openai_response)
    update.message.reply_text(openai_response_com_emog)

def teste_mensagem_com_assistente_existente(mensagem, threead_id, asst, file_idx, ferramentas, modelo_de_IA):

    message = client.beta.threads.messages.create(
        thread_id=threead_id,
        role="user",
        content=mensagem,
        file_ids=file_idx
    )
    run = client.beta.threads.runs.create(
        thread_id=threead_id,
        assistant_id=asst,
        tools=ferramentas,
        model=modelo_de_IA,
        
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
            return "ocorreu um erro no servidor pergunte novamente"
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

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
    
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
