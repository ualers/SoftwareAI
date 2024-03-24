# 🧠Automated software support with AI
* **💭Concept**:
The main concept is to replace the need to hire people to provide support and answer questions and problems from software customers

## 📎Creation of a custom assistant with the open ai assistants api
* **import keys and libraries**:
* pip install openai
* pip install python-telegram-bot
* you will probably have problems when trying to use the newest version of this python-telegram-bot library like I did, if this happens just download the version and I will make it available
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


* **7**: Now we have another important step of printing
  ```
  print(thread.id)
  print(assistant.id)
  ```
* we must also use the thread.id and assistant.id strings collected by print in the mini module
* remembering who the minimodule is:
  ```
  keys_def.py
  ```
* **8**: Now let's create the execution that will be used to define the instructions, tools and model for the second time and start our thread
```
run = client.beta.threads.runs.create(
    
    thread_id=thread.id,
    
    assistant_id=assistant.id, 
    
    instructions="you instructions", #your instructions on what rules artificial intelligence should follow for example (answer the questions asked based on the answers in the file)
    
    tools=[{"type": "retrieval"}],
    
    model="gpt-3.5-turbo-1106" 
)
```

* **9**:




