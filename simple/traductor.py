import json
import sys
import os
from strands import Agent, tool
from strands.models.ollama import OllamaModel

@tool
def consultar_diccionario(palabra_o_frase: str) -> str:
    """
    Busca palabras o modismos argentinos en el diccionario y devuelve su equivalente en chileno.
    """
    try:
        with open("diccionario_arg_chi.json", "r", encoding="utf-8") as f:
            diccionario = json.load(f)

        palabra_lower = palabra_o_frase.lower().strip()
        if palabra_lower in diccionario:
            return f"La traducción de '{palabra_o_frase}' al chileno es '{diccionario[palabra_lower]}'."

        return f"La palabra '{palabra_o_frase}' no se encontró en el diccionario."
    except Exception as e:
        return f"Error consultando el diccionario: {e}"

def main():
    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    ollama_model = os.getenv("OLLAMA_MODEL", "gemma4")

    modelo_local = OllamaModel(
        host=ollama_host,
        model_id=ollama_model
    )

    agente = Agent(
        model=modelo_local,
        tools=[consultar_diccionario],
        system_prompt=(
            "Eres un traductor experto de español argentino a español chileno. "
            "Tu objetivo es transformar la jerga y la estructura para que suene natural en Chile. "
            "Usa la herramienta 'consultar_diccionario' para validar modismos específicos. "
            "REGLA CRÍTICA: Responde SIEMPRE con UNA SOLA FRASE. No uses párrafos, "
            "ni explicaciones, ni etiquetas de 'Traducción:'. Solo el texto final."
        )
    )

    print(f"\n--- Traductor CLI (Ollama: {ollama_host}) ---")
    print("Escribe 'salir' para finalizar.\n")

    while True:
        try:
            frase_ingresada = input("frase a traducir: ")

            if frase_ingresada.lower().strip() in ['salir', 'exit', 'quit']:
                break

            if not frase_ingresada.strip():
                continue

            respuesta = agente(f"Traduce esta frase: {frase_ingresada}")

            output = str(respuesta).replace('\n', ' ').strip()
            print(f"frase resultado: {output}\n")

        except KeyboardInterrupt:
            print("\nProceso finalizado.")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
