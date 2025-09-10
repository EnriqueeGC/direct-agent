import google.generativeai as genai
from .config import API_KEY 

genai.configure(api_key=API_KEY)

# uso del modelo Gemini 1.5
model = genai.GenerativeModel('gemini-1.5-flash')

def agente_analista_de_intencion(texto_usuario: str) -> str:
    """"
    Agente que clasifica la intención del usuario.
    Devuelve: PREGUNTA_VÁLIDA, TRIVIAL, o INDEFINIDO.
    (Este agente no necesita cambios)
    """
    prompt_analista = f"""
    Tu única tarea es analizar y clasificar el siguiente texto de un usuario.
    Responde con UNA SOLA PALBRA. Las categorías son:

    1. PREGUNTA_VÁLIDA: Si el texto es una pregunta clara sobre inteligencia artificial, negocios, toma de decisiones o tecnología.
    2. TRIVIAL: Si el texto es un saludo, una despedida, un agradecimiento o una conversación casual (ej: "hola", "gracias", "cómo estás?").
    3. INDEFINIDO: Si no encaja en las categorías anteriores o es ambiguo.

    Texto a analizar: "{texto_usuario}"
    
    Clasificación:
    """
    response = model.generate_content(prompt_analista)
    return response.text.strip().upper()

def agente_experto_en_contenido(pregunta_usuario: str) -> str:
    """
        Agente que responde a una pregunta validada basándose en su conocimiento.
        (*** ESTE PROMPT HA SIDO MODIFICADO ***)
        """
    prompt_experto = f"""
        Eres un motor de IA para la toma de decisiones estratégicas. Tu único propósito es proporcionar una respuesta directa, concisa y accionable, formulada como una estrategia o recomendación.

        **REGLAS ESTRICTAS DE FORMATO:**
        1.  **SIN RELLENO:** No uses introducciones ni frases de relleno como "La mejor estrategia es..." o "Te recomiendo que...".
        2.  **RESPUESTA ACCIONABLE:** La respuesta DEBE empezar directamente con un verbo en infinitivo (ej: Implementar, Analizar, Desarrollar) que represente la acción principal a tomar.
        3.  **CONCISIÓN MÁXIMA:** La respuesta debe ser una única frase clara y potente.

        **EJEMPLO CLAVE DE FORMATO (One-Shot):**
        - Pregunta de ejemplo: ¿Cuál es la mejor estrategia para aumentar las ventas en un trimestre?
        - Respuesta de ejemplo: Implementar campañas de marketing digital segmentadas y optimizar la experiencia del cliente en línea.

        **BASE DE CONOCIMIENTO (Usa solo esta información):**
        == INICIO DE LA BASE DE CONOCIMIENTO ==
        - La Inteligencia Artificial (IA) expande las capacidades cognitivas para resolver problemas usando grandes volúmenes de datos.
        - Tipos de IA para decisión: Edición Lógica, Algoritmos de Optimización, Algoritmos Probabilísticos.
        - Ramas de IA aplicadas: Gestión de Decisiones, Analítica Predictiva, Optimización Matemática.
        - Modelos de empoderamiento: Consejero Autónomo, Subcontratista Autónomo, Empleado Autónomo, Autonomía Total.
        - Beneficios empresariales: Procesamiento de Datos Masivos, Servicio 24/7 con chatbots, Experiencia de Usuario Personalizada, Reducción de Errores con robots, Aumento de Velocidad en cálculos, Ejecución de Tareas Peligrosas.
        - Limitaciones: La IA carece de percepción y afecto humano, que siguen siendo cruciales.
        == FIN DE LA BASE DE CONOCIMIENTO ==

        Ahora, aplica estas reglas estrictamente a la siguiente pregunta del usuario.

        Pregunta: "{pregunta_usuario}"
        Respuesta:
        """
    response = model.generate_content(prompt_experto)
    return response.text