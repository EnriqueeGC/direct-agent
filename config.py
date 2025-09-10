import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Carga la clave API desde una variable de entorno
    API_KEY = os.getenv("API_KEY")