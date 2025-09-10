import os
from dotenv import load_dotenv

# Carga las variables del archivo .env en el entorno
load_dotenv()

# Obtiene la API key del entorno
API_KEY = os.getenv("API_KEY")

# Verificación de seguridad: si no encuentra la API key, detiene el programa
if not API_KEY:
    raise ValueError("❌ No se encontró la GOOGLE_API_KEY. Asegúrate de crear un archivo .env con tu clave.")