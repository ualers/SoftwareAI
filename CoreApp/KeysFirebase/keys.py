#########################################
# IMPORT SoftwareAI Libs 
from CoreApp._init_libs_ import *
#########################################

class chaves_ia:
    def chaves_ia_openai():
        "Key Open ai"
        str_key = "youkey"
        return str_key
    


def keys_app_2():
    "Firebase APP 2"

    cred1 = {
    "type": "",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "",
    "universe_domain": "googleapis.com"
    }
    credt1 = credentials.Certificate(cred1)
    app2 = initialize_app(credt1, {
            'storageBucket': 'YOU.appspot.com',
            'databaseURL': 'https://YOU-default-rtdb.firebaseio.com'
    }, name='app2')

    return app2



def keys_app_1():
    "Firebase APP 1"    

    cred1 = {
    "type": "",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "",
    "universe_domain": "googleapis.com"
    }
    credt1 = credentials.Certificate(cred1)
    app1 = initialize_app(credt1, {
            'storageBucket': 'YOU.appspot.com',
            'databaseURL': 'https://YOU-default-rtdb.europe-west1.firebasedatabase.app'
    }, name='app1')
    bucket = storage.bucket(app=app1)

    return app1, bucket