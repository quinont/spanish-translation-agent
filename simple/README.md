# Traductor Argentino-Chileno (Strands Agents + Ollama)

Este proyecto es un agente inteligente desarrollado con **Strands Agents** que utiliza el modelo **Gemma 4** (vía Ollama) para traducir frases con modismos argentinos a español chileno natural.

## Requisitos Previos

- Python 3.11 o superior.
- Acceso a un servidor de **Ollama** con el modelo `gemma4` descargado.

## Instalación

Para preparar el entorno virtual e instalar las dependencias necesarias, simplemente ejecuta:

```bash
make setup
```

## Configuración y Uso

El script utiliza variables de entorno para conectarse al servidor de Ollama. Puedes ejecutarlos con los valores por defecto (localhost y gemma4) o especificar un servidor remoto.

### Ejecución estándar:

```Bash
make run
```

### Ejecución con servidor remoto:

```Bash
make run OLLAMA_HOST="http://TU_HERMOSA_IP:11434" OLLAMA_MODEL="gemma4:latest"
```

## Diccionario

Puedes modificar el archivo diccionario_arg_chi.json para agregar nuevos modismos o ajustar las traducciones. El agente consultará este archivo antes de generar la respuesta final.

## Limpieza

Para eliminar el entorno virtual y los archivos generados:

```Bash
make clean
```


---

### 4. `diccionario_arg_chi.json`

El archivo externo para los modismos.

```json
{
  "che": "oye",
  "copado": "bacán",
  "laburo": "pega",
  "quilombo": "cacho",
  ...
}
```

---

### 5. Frases para probar

unas frases para hacer un testing:

- "Che, el laburo con los CI/CD pipelines de hoy fue un quilombo."
- "Ese chabón se gastó toda la guita en unas zapatillas nuevas."
- "El pibe se tomó el bondi equivocado para ir al centro."
- "Boludo, la automatización que armaste quedó re copada."

