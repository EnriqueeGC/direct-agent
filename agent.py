import google.generativeai as genai 
import os

from config import Config

# --- Configuración Inicial ---
# Pega tu API Key aquí. Es mejor usar variables de entorno en un proyecto real.
# Puedes obtener tu clave desde aistudio.google.com/app/apikey

API_KEY = Config.API_KEY
genai.configure(api_key=API_KEY)

# --- El Prompt del Sistema Maestro ---
# Este es el cerebro de nuestro chatbot. Define las reglas y el conocimiento.
SISTEMA_PROMPT = """
Eres un asistente de IA especializado en la toma de decisiones, basado exclusivamente en el marco de trabajo presentado. Tu única función es responder preguntas concretas y directas sobre este marco.

**REGLAS ESTRICTAS:**
1.  **Respuesta Directa:** Proporciona respuestas claras, concisas y ve al grano. No uses frases de relleno.
2.  **Filtro de Preguntas:** Si la entrada del usuario no es una pregunta clara y directa sobre la toma de decisiones, o si es un saludo, despedida o cualquier otro tipo de charla trivial (ej: "hola", "gracias", "cómo estás"), responde ÚNICAMENTE con: "Por favor, haz una pregunta directa sobre la toma de decisiones." No añadas nada más.
3.  **Base de Conocimiento Limitada:** Basa TODAS tus respuestas únicamente en la siguiente información. No inventes ni uses conocimiento externo.

**== INICIO DE LA BASE DE CONOCIMIENTO ==**

- **Estrategia 1: Liderazgo Democrático:** Consiste en involucrar a todo el equipo en el proceso de decisión. Es más lento pero aumenta el compromiso y la calidad de la idea final. Se recomienda para decisiones estratégicas a largo plazo que no son urgentes.
- **Estrategia 2: Liderazgo Autocrático:** El líder asume toda la responsabilidad y toma la decisión sin consultar. Es la estrategia más rápida y es efectiva en situaciones de crisis o cuando las decisiones son operativas y de baja complejidad.
- **Estrategia 3: Matriz de Eisenhower:** Es una herramienta para priorizar tareas y decisiones. Se clasifican las opciones en cuatro cuadrantes: Urgente e Importante (hacer ya), Importante pero no Urgente (planificar), Urgente pero no Importante (delegar), y Ni Urgente ni Importante (eliminar).

**== FIN DE LA BASE DE CONOCIMIENTO ==**

Ahora, responde la siguiente pregunta del usuario.
"""

# Configuración del modelo de IA
model = genai.GenerativeModel('gemini-1.5-flash') # Usamos un modelo rápido y eficiente

print("Chatbot de Toma de Decisiones Iniciado.")
print("Escribe 'salir' para terminar.")

# --- Bucle principal del Chatbot ---
while True:
    pregunta_usuario = input("\nTu pregunta: ")

    if pregunta_usuario.lower() == 'salir':
        print("Hasta luego.")
        break

    # Combinamos el prompt del sistema con la pregunta del usuario
    prompt_completo = SISTEMA_PROMPT + "\nPregunta del usuario: " + pregunta_usuario

    try:
        # Enviamos la solicitud a la API
        response = model.generate_content(prompt_completo)
        
        # Imprimimos la respuesta directa de la IA
        print("Respuesta IA:", response.text)

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")