
#########################################
# IMPORT SoftwareAI Agents
from CoreApp._init_agents_ import AgentInitializer
#########################################
# IMPORT SoftwareAI Libs 
from CoreApp._init_libs_ import *
#########################################

pr_number = 9
# for i in range(3):

repo_owner = "A-I-O-R-G"
branch_name = f"main1"
repo_name = "GeradorDeDescricaoDeCursos"
path_Software_Development_py = f"CoreApp/Work_Environment/cursodescricaoautomatica/Software_Development/python_software.py"


software_improvements = AgentInitializer.get_agent('software_improvements') 

SoftwareDevelopment_SignalMaster = AgentInitializer.get_agent('SoftwareDevelopment_SignalMaster') 


flag = software_improvements.AI_DataWeaver_improvements(path_Software_Development_py, "", "")
print(flag)

flag = SoftwareDevelopment_SignalMaster.AI_SignalMaster(path_Software_Development_py, repo_name, branch_name)
print(flag)



    # flag = quantumcore_review_pr(repo_owner, repo_name, pr_number)
    # print(flag)
    # pr_number = pr_number + 1
