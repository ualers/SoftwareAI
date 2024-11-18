# IMPORT SoftwareAI Libs 
from ._init_libs_ import *
#########################################
# IMPORT SoftwareAI All Paths 
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "environment.env"))
load_dotenv(find_dotenv('environment.env'), override=True)
#########################################
