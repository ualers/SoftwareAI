########################################################################
## IMPORTS Libs
import sys
import os
import subprocess
from typing import Dict, Any
import time
import psutil
import GPUtil
import math
import hashlib
from typing import Dict, Any
import os
import subprocess
import platform
from firebase_admin import credentials, initialize_app, storage, db, delete_app
import concurrent.futures
########################################################################


########################################################################
# IMPORT FirebaseKeys
# from FirebaseKeys.key import keys_app_2 
# app2 = keys_app_2()
########################################################################

########################################################################
# IMPORT .qrc
from src import icons_interpreter
########################################################################

########################################################################
# IMPORT GUI 
from src.ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomModals import QCustomModals
########################################################################

########################################################################
# IMPORT Pyside2
from PySide2extn.RoundProgressBar import roundProgressBar #IMPORT THE EXTENSION LIBRARY
from PySide2.QtCore import QTimer, Signal, QThread

########################################################################

########################################################################
# IMPORT CoreApp

########################################################################



########################################################################


########################################################################
# MainWindow Media Cuts
class Main_Window_Media_Cuts(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style.json"})
        
        #QAppSettings.updateAppSettings(self)
 




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main_Window_Media_Cuts()
    MainWindow.show()
    sys.exit(app.exec())