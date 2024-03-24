# Automated software support with AI
* **Concept**:
The main concept is to replace the need to hire people to provide support and answer questions and problems from software customers

## 🖥️Creation of a custom assistant with the open ai assistants api
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
          name="Software support", (You can give whatever name you want to your automated support artificial intelligence)
          instructions="answer the questions asked based on the answers in the file answer only what was asked by customers and not all the questions in the file if the customer asks something that is not in the file apologize and say that we do not yet have answers.",
          tools=[{"type": "retrieval"}], (Note that this tool is crucial for the wizard to be able to retrieve the contents of the doc.csv file)
          model="gpt-3.5-turbo-1106", (Note that you can use gpt4, gpt3.5 16k unfortunately does not support wizards)
          file_ids=[file.id]
      )
  ```

* **5**: Now an important step is to print the file id so that we can collect it and paste it into the minimodule
(this is quite archaic but it is functional for the first versions)

```
keys_def.py
```
