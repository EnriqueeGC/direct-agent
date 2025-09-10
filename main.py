from chatbot.agents import agente_analista_de_intencion, agente_experto_en_contenido

def main():
    print(" Sistema de IA para Toma de Decisiones Iniciado.")
    print("   Escribe 'salir' para terminar.")

    while True:
        entrada_usuario = input("\n> ")

        if entrada_usuario.lower() == 'salir':
            print("👋 Hasta luego.")
            break

        # 1. El Agente 1  clasifica la entrada.
        intencion = agente_analista_de_intencion(entrada_usuario)
        print(f"[DEBUG: Intención detectada -> {intencion}]")

        # 2. El programa decide qué hacer basado en la intención.
        if intencion == "PREGUNTA_VÁLIDA":
            # 3. Si es válida, se activa el Agente 2 (Experto).
            respuesta_final = agente_experto_en_contenido(entrada_usuario)
            print("🤖 Respuesta:", respuesta_final)
        elif intencion == "TRIVIAL":
            print("🤖 Respuesta: Por favor, haz una pregunta directa sobre la toma de decisiones.")
        else: # INDEFINIDO
            print("🤖 Respuesta: No he entendido tu solicitud. Por favor, formula una pregunta más clara.")

if __name__ == "__main__":
    main()