#########################################
# IMPORT SoftwareAI Agents
from CoreApp._init_agents_ import AgentInitializer
#########################################
# IMPORT SoftwareAI Libs 
from CoreApp._init_libs_ import *
#########################################


byte_manager = AgentInitializer.get_agent('ByteManager') 

mensagem = "solicito um script para Criar pdf com base em tutoriais do youtube o objetivo é extrair audio do video e transcrever utilizando whisper local modelo small e criar o pdf com base nos audios dos tutoriais  "
owner_response = byte_manager.AI_1_ByteManager_Company_Owners(mensagem)
print(owner_response)

