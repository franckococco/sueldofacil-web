# functions/main.py
import firebase_admin
from firebase_functions import https_fn

firebase_admin.initialize_app()

# UNA SOLA FUNCIÓN. UN HOLA MUNDO. NADA MÁS.
@https_fn.on_request(region="us-central1")
def api(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response("HOLA MUNDO DESDE LA PUTA NUBE")