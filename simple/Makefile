OLLAMA_HOST ?= http://localhost:11434
OLLAMA_MODEL ?= gemma4
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: all setup run clean

all: setup

setup:
	@echo "Creando entorno virtual en $(VENV)..."
	python3.12 -m venv $(VENV)
	@echo "Instalando dependencias..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Setup completado correctamente."

run:
	@OLLAMA_HOST=$(OLLAMA_HOST) OLLAMA_MODEL=$(OLLAMA_MODEL) $(PYTHON) traductor.py

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Limpieza completada."
