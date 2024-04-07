# 🧠Automated software support with AI
* **💭Concept**:
The main concept is to replace the need to hire people to provide support and answer questions and problems from software customers
## Index
- [Creation](#Creation)
- [Support](#Support)
- [Telegram-group-support](#Telegram-group-support)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Telegram group support
* **📎You can also support people in a Telegram group**:
  * **To do this, simply add your assistant to the desired group and give him admin**:
  * **With this he will be reading the group messages and will answer all the questions asked.**:

#
# Support
* **📎Support via Telegram using the library**:
  * **📂install libraries**:
  * pip install openai
  * pip install python-telegram-bot
  * you will probably have problems when trying to use the newest version of this python-telegram-bot library like I did, if this happens just download the version and I will make it available
    ```
      python-telegram-bot.rar
    ```
    ```
  * **📂import keys and libraries**:
    ```
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
    ```
  * **1**: The first function we will discuss is main()
    ```
    def main():
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
        updater.start_polling()
        updater.idle()
    if __name__ == '__main__':
        main()

    ```
    * **explaining**: the first line we call the Updater function of the telegram module we define our telegram bot token and then we define the context as True
    ```
    updater = Updater(TOKEN, use_context=True)
    ```
    * **BotFather**: To get your bot's TOKEN, you must open your Telegram and search in the magnifying glass for @BotFather or visit https://t.me/BotFather
    * **BotFather**: When accessing BotFather, just type /start, then you can create your bot with the command /newbot
    * **BotFather**: After that you define the name of your bot, it can be Assistant
    * **BotFather**: After defining the name of the bot you will have to define the @ ending with bot for example Assistant_bot
    * **BotFather**: if the message ''Done! Congratulations on your new bot.'' appears ready, your bot is created and you will have access to the token, just copy the token below the phrase ''Use this token to access the HTTP API:''
    * **BotFather**: now you have your TOKEN place it in the keys_def.py module in
    ```
        def keys_bot_telegram():
          TOKEN = "here"
          CHANNEL_ID = 'advanced'
          return TOKEN, CHANNEL_ID
    ```
   
    * **dp**: Now let's create an updater dispatcher
      ```
        dp = updater.dispatcher
      ```
      * **explaining**: will be used to capture text messages
    * **add_handler**: adding commands to the dispatcher
      ```
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
      ```
    * **start_polling**: now let's start
      ```
        updater.start_polling()
        updater.idle()
      ```
  * **2**: Now let's discuss the function that observes customer messages and responds based on our assistant that we created in creation
    ```
      def reply_message(update, context):
          user_message = update.message.text
          asst, threead_id = chaves.asst_e_threead()
          file_idx = chaves.file_id()
          ferramentas = chaves.ferramentas()
          modelo_de_IA = chaves.modelo_de_ia()
      
          openai_response = teste_mensagem_com_assistente_existente(user_message, threead_id, asst, file_idx, ferramentas, modelo_de_IA)
          openai_response_com_emog = enviar_resposta_com_emoji(openai_response)
          update.message.reply_text(openai_response_com_emog)
    ```
    * **user_message**: the first line is used to check if there is a message
    ```
      user_message = update.message.text
    ```
    * **assistant_id and threead_id**: Now let's get the assistant_id and threead_id that we created in creation
      ```
        asst, threead_id = chaves.asst_e_threead()
      ```
    * **explaining**: you must put the assistant_id and threead_id that we saved in that txt inside the key_def.py module in
      ```
        def asst_e_threead():
            asst = 'here'
            thread_id = 'here'
            return asst, thread_id
      ```
    * **file_id**: Now let's get the file_id that we created at creation 
      ```
        file_idx = chaves.file_id()
      ```
    * **explaining**: Now we will put the file_id saved in that txt that we created in creation in the key_def.py module in
      ```
          def file_id(): 
              file_id = ["here"]
              return file_id
      ```
    * **tools**: Now let's get the tools like the doc reading tool
      ```
        ferramentas = chaves.ferramentas()
      ```
    * **explaining**: By default, I have already added the doc reading function, so there is no need to touch this part of the key_def.py module:
      ```
      def ferramentas():
          tools = [{"type": "retrieval"}]
          return tools
      ```
    * **model**: Now let's get the model
      ```
        modelo_de_IA = chaves.modelo_de_ia()
      ```
    * **explaining**: By default, we will use the gpt-3.5-turbo-1106 template, so there is no need to touch this part of the key_def.py module:
      ```
        def modelo_de_ia():
            model = "gpt-3.5-turbo-1106"
            return model
      ```
    * **openai_response**: now let's pass the question if it is detected in user_message
      ```
            openai_response = teste_mensagem_com_assistente_existente(user_message, threead_id, asst, file_idx, ferramentas, modelo_de_IA)

      ```
    * **explaining**: This function receives the following arguments user_message, threead_id, asst, file_idx, tools, IA_model
    * **openai response with emoji**: let's pass the assistant's message to a function that will put emog
      ```
         openai_response_com_emog = enviar_resposta_com_emoji(openai_response)
         
      ```
     * **explaining**: This is the function that will add emoji to the message
      ```
       emojis = ['😊', '🤖', '🚀', '💡', '🎉']
       def enviar_resposta_com_emoji(resposta):
           emoji = random.choice(emojis)  
           resposta_com_emoji = f"{emoji} {resposta}"  
           return resposta_com_emoji
      ```
      
    * **reply_text**: finally now the message is ready to be sent to the customer
      ```
 update.message.reply_text(openai_response_com_emog)

      ```




  * **3**: let's discuss the function test_mensagem_com_assistant_existente which will be used to interact with the assistant that we created in the creation and give the answer to the client based on our instructions and the doc.csv
    ```
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
    ```
    * **message**: the first line we are creating a message
    ```
    message = client.beta.threads.messages.create(
        thread_id=threead_id,
        role="user",
        content=mensagem,
        file_ids=file_idx
    )
    ```
    * **explaining**: the first line we are creating within the thread a message specifying the threead_id of our message and finally passing our file_id
    * **run**: the first second line we are starting our thread
    ```
    run = client.beta.threads.runs.create(
        thread_id=threead_id,
        assistant_id=asst,
        tools=ferramentas,
        model=modelo_de_IA,
        
    )
    ```
    * **explaining**: the first second line we are starting our thread passing the arguments threead_id, assistant_id , tools and finally the model
    * **run_status**: Now let's wait for the status of our run to be ''completed''
    ```
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
    ```
    * **explaining**: We wait for the status of our run to be ''completed'' so we can get the message from our assistant
    * **messages**: message return
    ```
      messages = client.beta.threads.messages.list(
      thread_id=threead_id
      )
      for message in messages:
          for mensagem_contexto in message.content:
              valor_texto = mensagem_contexto.text.value
              
              return valor_texto
              
          break
    ```
    * **explaining**: Now that our assistant has responded, let's take the message and return it so we can add an emog before actually sending it to the customer
#
  * **4**: Last but not least, you can configure a specific command for your Telegram bot, example
    ```
     def start(update, context):
         update.message.reply_text('Olá meu nome é Usuporte! Como posso ajudar você?')
    ```
  * **5**: Now your assistant is 100% just run and do a test by opening your Telegram and asking your assistant a question that we created :}
    ```
     Openai+ Telegram Support Assistant.py
    ```
#
#
#
#
#
#
#
# Creation
* **📎Creation of a custom assistant with the open ai assistants api**:
* **📂import keys and libraries**:
* pip install openai
* pip install python-telegram-bot
* you will probably have problems when trying to use the newest version of this python-telegram-bot library like I did, if this happens just download the version and I will make it available
  ```
    python-telegram-bot.rar
  ```
  importing keys and libraries
  ```
  from openai import OpenAI
  from keys_def import chaves
  key_api = chaves.chaves_open_ai()
  client = OpenAI(
      api_key=key_api,
  )
  ```
* **You can find the keys_def mini module in**:
  ```
  keys_def.py
  ```
  
* **Creating the wizard**:
  ```
  Creating_the_wizard.py
  ```
* **1**:  we will create a .csv file which will be called doc.csv this will be the documentation that the software support will have, please note
  ```
  example content doc
  Customer question: Do you offer a free trial?
  Answer: yes 1 day
  ```
* **2**: now we will save (note you can use .txt but I had problems with documentation with more than 100 lines)
  ```
  doc.csv
  ```
* **3**: Now that we have created the content that our AI will use to read and respond to customers, we will configure it to use the doc.csv as documentation for our assistant

  ```
  def creating_new_assistant():
      file = client.files.create(
          file=open("doc.csv", "rb"),
          purpose='assistants'
      )
  ```
* **4**: Now that the documentation is defined, let's actually create our wizard
```
assistant = client.beta.assistants.create(
      name="Software support", #(You can give whatever name you want to your automated support artificial intelligence)
  
      instructions="you instructions", #your instructions on what rules artificial intelligence should follow for example (answer the questions asked based on the answers in the file)
  
      tools=[{"type": "retrieval"}], #(Note that this tool is crucial for the wizard to be able to retrieve the contents of the doc.csv file)
  
      model="gpt-3.5-turbo-1106", #(Note that you can use gpt4, gpt3.5 16k unfortunately does not support wizards)
  
      file_ids=[file.id] #Here is an important step defining the file id within a list (note that you can place more than 1 doc.csv file but I haven't had a good experience, it gets buggy when reading the content of the file)
  )
```

* **5**: Now an important step is to print the file id so that we can collect it and paste it into the minimodule
(this is quite archaic but it is functional for the first versions)
```
print([file.id])
```
remembering who the minimodule is:
```
keys_def.py
```

* **6**: Now our agent is created and we can start a thread so that we can send messages to it
```
thread = client.beta.threads.create()
```

* **7**: Now that we have created the thread variable, let's define the message patterns
```
message = client.beta.threads.messages.create(
  
    thread_id=thread.id, #(here we get the id of the created thread)
  
    role="user", #here is the definition of who is sending the message (do not change)
  
    content='''Hello!''', #(This is where we will define the first content of our conversation with our support AI (don't worry about typing anything relevant in this first content)
  
    file_ids=[file.id] #Here is an important step defining the file id within a list (note that you can place more than 1 doc.csv file but I haven't had a good experience, it gets buggy when reading the content of the file)
)
```


* **8**: Now we have another important step of printing
  ```
  print(thread.id)
  print(assistant.id)
  ```
* we must also use the thread.id and assistant.id strings collected by print in the mini module
* remembering who the minimodule is:
  ```
  keys_def.py
  ```
* **9**: Now let's create the execution that will be used to define the instructions, tools and model for the second time and start our thread
```
run = client.beta.threads.runs.create(
    
    thread_id=thread.id,
    
    assistant_id=assistant.id, 
    
    instructions="you instructions", #your instructions on what rules artificial intelligence should follow for example (answer the questions asked based on the answers in the file)
    
    tools=[{"type": "retrieval"}],
    
    model="gpt-3.5-turbo-1106" 
)
```

* **10**: Now let's wait for the status to be complete so we can capture the agent's message
```
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
```
* **11**: Now that the status is complete we are ready to fetch the last message from the created topic
```
    for message in messages:
        for mensagem_contexto in message.content:  
            valor_texto = mensagem_contexto.text.value
            print(valor_texto)
        break
```
* **11.5**: You can also save the thread_id and assistant_id and file_id so that we can use it in the version already created in our assistant
* I recommend you save
```
    for message in messages:
        for mensagem_contexto in message.content:  
            valor_texto = mensagem_contexto.text.value
            print(valor_texto)
            thread_id = thread.id
            assistant_id = assistant.id
            file_1 = file.id
            run_id = run.id
            name = "Assistente"
            diretorio_script = os.path.dirname(os.path.abspath(__file__))
            nome_arquivo_gerenciador = os.path.join(diretorio_script, 'gerenciador_agente_1.txt')
            with open('gerenciador_agente_1.txt', 'a') as arquivo:
                arquivo.write(f'Nome: {name} \n')
                arquivo.write(f'thread_id:{thread_id}\n')
                arquivo.write(f'assistant_id:{assistant_id}\n')
                arquivo.write(f'file_id:{file_1}\n')
                arquivo.write(f'------------------------\n')
        break

```
* **12**: Finally our agent is created and ready to be used, let's see how it works :}
