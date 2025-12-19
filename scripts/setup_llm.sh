#!/bin/bash

echo ">>> Instalando Ollama y modelo IA (4GB Mistral 7B)..."
sleep 1

# Detectar SO
OS=$(uname -s)

echo ">>> Detectando sistema operativo..."
if [ "$OS" = "Linux" ]; then
    echo ">>> Sistema Linux detectado."

    # Comprobar si ollama existe
    if command -v ollama >/dev/null 2>&1; then
        echo ">>> Ollama ya está instalado."
    else
        echo ">>> Descargando Ollama..."
        curl -fsSL https://ollama.com/install.sh | sh

        if [ $? -ne 0 ]; then
            echo "ERROR: No se pudo instalar Ollama."
            exit 1
        fi
    fi

    echo ">>> Iniciando servicio de Ollama..."
    sudo systemctl enable ollama
    sudo systemctl start ollama
    sleep 2

else
    echo "ERROR: Sistema operativo no soportado por este instalador."
    exit 1
fi

echo ">>> Descargando modelo Mistral 7B Instruct (4GB)..."
ollama pull mistral:instruct

if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo descargar el modelo."
    exit 1
fi

echo ">>> Verificando modelo..."
RESPUESTA=$(echo "Hola" | ollama run mistral:instruct)

if [[ "$RESPUESTA" == "" ]]; then
    echo "ERROR: El modelo no responde."
    exit 1
fi

echo ">>> Modelo listo y funcional."
echo ">>> Instalación completada."
exit 0
